import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns

# read in app_usage data into vpn_df
vpn_df = pd.read_csv('app_usage1.csv')

#look at the shape of the dataframe
print(vpn_df.shape)
#look at the column names
print(vpn_df.columns)
#show the first 5 records
print(vpn_df.head(5))

# Create a histogram of Remote VPN Access
plt.figure(figsize=(8, 5))
plt.hist(vpn_df['RemoteAccess'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Remote VPN Access')
plt.xlabel('Remote Access Usage')
plt.ylabel('Frequency')
plt.show()

# RemoteAccess is the target (Y), X is all other columns
Y = vpn_df['RemoteAccess']
X = vpn_df.drop('RemoteAccess', axis=1)

print(X.head(5))
print(Y.head(5))

tf.random.set_seed(0)

model1 = Sequential()

# We use 'relu' activation for hidden layers because it helps the model learn
# non-linear patterns efficiently.
model1.add(Dense(64, input_dim=X.shape[1], activation='relu'))
model1.add(Dropout(0.18)) # Dropout rate between 0.15 and 0.20 to prevent overfitting

model1.add(Dense(64, activation='relu'))
model1.add(Dropout(0.18))

model1.add(Dense(54, activation='relu'))
model1.add(Dropout(0.18))

model1.add(Dense(40, activation='relu'))
model1.add(Dropout(0.18))

# Output layer: 1 unit with no activation function.
# We don't use activation here because this is a regression task,
# and we need the model to output a continuous number.
model1.add(Dense(1))

model1.summary()

# split the dataset: 80% for training and 20% for testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=42)

# Loss Function: MSE (Mean Squared Error) is chosen because it is the standard
# for regression problems to minimize the distance between predicted and actual values.
# Metric: MAE (Mean Absolute Error) is used to see the average error in original units.
model1.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Train for 200 epochs as requested
history1 = model1.fit(X_train, Y_train, epochs=200, verbose=0)
print("Model 1 training finished.")

# predict and calculate the R-Squared score
Y_pred1 = model1.predict(X_test)
print(f"Model 1 R-Squared: {r2_score(Y_test, Y_pred1)}")

# --- Model 2: Simpler Architecture ---
model2 = Sequential([
    Dense(32, input_dim=X.shape[1], activation='relu'),
    Dense(1)
])
model2.compile(optimizer='adam', loss='mse')
history2 = model2.fit(X_train, Y_train, epochs=200, verbose=0)

# --- Model 3: Different Layer Setup ---
model3 = Sequential([
    Dense(128, input_dim=X.shape[1], activation='relu'),
    Dense(64, activation='relu'),
    Dense(1)
])
model3.compile(optimizer='adam', loss='mse')
history3 = model3.fit(X_train, Y_train, epochs=200, verbose=0)

# Comparison
r2_m2 = r2_score(Y_test, model2.predict(X_test))
r2_m3 = r2_score(Y_test, model3.predict(X_test))

print(f"Model 2 R2: {r2_m2}")
print(f"Model 3 R2: {r2_m3}")

# History Plot
plt.plot(history1.history['loss'], label='Model 1 (5 Layers)')
plt.plot(history2.history['loss'], label='Model 2 (Simple)')
plt.plot(history3.history['loss'], label='Model 3 (Wide)')
plt.title('Loss History Comparison')
plt.xlabel('Epochs')
plt.ylabel('MSE Loss')
plt.legend()
plt.show()

# Analysis: Model 1 includes dropout which prevents overfitting but might take
# longer to converge. Model 3 usually performs better because it has more neurons
# to capture data complexity.
