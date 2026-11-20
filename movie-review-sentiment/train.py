import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense, Dropout

"""**Step 1: Data Loading & Label EncodingIn**

This step, we read the training and testing datasets from CSV files. Since the output labels are text (positive/negative), we use a LabelEncoder to convert them into binary format ($1$ for positive, $0$ for negative).
"""

# Fixed Cell 2: Data Loading and Label Encoding
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1. Read the data (using your actual filename 'data-4.csv')
train_df = pd.read_csv('data.csv', header=None)
test_df = pd.read_csv('data_test.csv', header=None)

# 2. Rename columns by index so the rest of the code works
train_df.columns = ['review', 'label']
test_df.columns = ['review', 'label']

# 3. Convert labels into numbers (Positive/Negative -> 1/0)
label_encoder = LabelEncoder()
train_labels = label_encoder.fit_transform(train_df['label'])
test_labels = label_encoder.transform(test_df['label'])

print("Success: Data loaded and labels encoded!")
print(f"Classes found: {label_encoder.classes_}")

"""**Step 2: Text Vectorization**

To process text with a neural network, we must convert words into numbers. We use a Tokenizer to create a vocabulary of the top 10,000 words. We then apply Padding to ensure all sequences have a consistent length of 200, which is required for the input layer of our model.
"""

# Parameters for processing
vocab_size = 10000
max_length = 200

# Initialize and fit the Tokenizer
tokenizer = Tokenizer(num_words=vocab_size, oov_token="<OOV>")
tokenizer.fit_on_texts(train_df['review'])

# Convert to padded sequences
train_sequences = tokenizer.texts_to_sequences(train_df['review'])
train_padded = pad_sequences(train_sequences, maxlen=max_length, padding='post', truncating='post')

test_sequences = tokenizer.texts_to_sequences(test_df['review'])
test_padded = pad_sequences(test_sequences, maxlen=max_length, padding='post', truncating='post')

print("Text successfully converted to padded sequences.")

"""**Step 3: Model Architecture & Training**
We are using a Sequential model with the following layers:

Embedding Layer: To learn word relationships.

Global Average Pooling: To reduce the dimensionality of the text data.

Dense Layers: For deep learning and classification.

Dropout: To prevent overfitting.

Sigmoid Output: To produce a probability between 0 and 1.
"""

model = Sequential([
    Embedding(vocab_size, 16),
    GlobalAveragePooling1D(),
    Dense(24, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid') # Sigmoid is required for Positive/Negative classification
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training for 10 epochs
print("Starting training... please wait.")
model.fit(train_padded, train_labels, epochs=10, validation_split=0.2, verbose=1)

"""**Step 4: Final Evaluation**

We evaluate the trained model using the separate data_test.csv file. Our primary metric is Accuracy, representing the ratio of correct predictions to the total number of reviews.
"""

# Evaluate the model on the test data
loss, accuracy = model.evaluate(test_padded, test_labels)

print(f"\n--- Final Submission Results ---")
print(f"Accuracy Score: {accuracy:.4f}")
print(f"This represents the ratio: (Correct Predictions) / (Total Reviews)")
