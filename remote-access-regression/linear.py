#import the needed packages
import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib 

# %%
# read in app_usage data into vpn_df

##############################################
## type your code here to create vpn dataframe
vpn_df = pd.read_csv('app_usage.csv')
##############################################

# %%
#oberve the data
#RemoteAccess is the target, we will build a model that
#takes all other columns as X to predict remote VPN usage

#look at the shape of the dataframe
print(vpn_df.shape)

#look at the column names
print(vpn_df.columns)

#show the first 5 records
print(vpn_df.head(5))

# %%
#1. See the distribtuion of Remote VPN Access

################################################################
## Create a histogram of VPN usage close to the display below####
plt.figure(figsize=(8, 5))
plt.hist(vpn_df['RemoteAccess'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Remote VPN Access')
plt.xlabel('RemoteAccess Score')
plt.ylabel('Frequency')
plt.show()
#################################################################


# %%
#2. See the correlation heat map

################################################################
## Create a correlation heatmap close to the display below  ####
plt.figure(figsize=(10, 8))
correlation_matrix = vpn_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
#################################################################


# %%
#We determine that this is supervised machine learning problem
#Linear Regression can be a good model
from sklearn import linear_model

# %%
#The function takes X, y and retrun the trained model and R squared
def train_model(X,y):
    model = linear_model.LinearRegression()
    model.fit(X, y)
    R_2 = model.score(X,y)
    return model, R_2
#create a function to calculate Adjusted R_square
# n is the number of sample, p is the number features
def cal_adjusted_R(R_2, p, n):
    R_adjusted = R_2-(1-R_2)*(p/(n-p-1))
    return R_adjusted

# %%
#R_2_array stores the R squared of all the features
R_2_array = np.array([])

#Calcuate the R_squared
for col_name in vpn_df.columns:
    if col_name == 'RemoteAccess':
        continue
    else:
        # add your code here:
        ################################################################
        ## call the train_model() function to calculate R squared   ####
        X_temp = vpn_df[[col_name]]
        y_temp = vpn_df['RemoteAccess']
        model_temp, r2_temp = train_model(X_temp, y_temp)
        R_2_array = np.append(R_2_array, r2_temp)
        #################################################################

# sorted_R_2_index stores the index numbers of R_2_array
sorted_R_2_index = np.argsort(R_2_array)[::-1]

#print out the sorted indexes
print("The order of index numbers are : \t", sorted_R_2_index)
 

# %%
#gradually build up our model and add R squared and adjusted R to the output

for i in range(len(sorted_R_2_index)):

    #the selected_features should be the top i most associated features
    selected_features = []

    #take the top 1 to ith features as X
    for j in range(i+1):

            #append a new column based on the sorted R value
            #take your time to digest this line
            selected_features.append(vpn_df.columns[sorted_R_2_index[j]])

    #verify we got the right features
    print(selected_features)

    # X
    X_feature = vpn_df[selected_features]

    # y
    target = vpn_df[['RemoteAccess']]

    # train the model
    model, R_2 = train_model(X_feature, target)

    #calculate adjusted R
    R_adjusted = cal_adjusted_R(R_2, i+1, vpn_df.shape[0])

    #print the output
    print("R2: ", R_2, "\t Ajusted R2: ", R_adjusted, "\n")

# %%
#let's build the model with all the features

y = vpn_df['RemoteAccess']
X = vpn_df.drop('RemoteAccess', axis=1)

from sklearn import linear_model

#create a linear regression model from linear_model package
model=linear_model.LinearRegression()

#Train the model with our data (X, y)
model.fit(X,y)

#Display the parameters
print('Intercept: \n', model.intercept_)
print('Coefficients: \n', model.coef_)

#use R squared to see how much variation is explained by the trained model
print('R_squared: \n', model.score(X,y))

# %%
# Should we reduce the number of features?



# %%
# 1. remove highly correlated features (>0.9)
##################################################################################
## modify the following code to remove the features you feel necessary
# Based on the heatmap, CloudDrive, ERP, and Webmail are very high. We keep CRM.
X = vpn_df.drop(['RemoteAccess', 'CloudDrive', 'ERP', 'Webmail', 'ITOps'], axis=1)
y = vpn_df['RemoteAccess']
#################################################################################

# 2. Lasso
best_score = 0
best_alpha = 0

for alpha in np.linspace(1, 0.2, 1000):
    model = linear_model.Lasso(alpha=alpha, max_iter=int(1e5))
    model.fit(X, y)

    # Find a model that uses exactly 3 features
    if np.count_nonzero(model.coef_) == 3:
        best_score = model.score(X, y)
        best_alpha = alpha
        break

print("The best R of my 3-feature model is:\t\t", best_score)
print("The alpha I used in Lasso to find my model is: \t", best_alpha)
  




if np.count_nonzero(model.coef_) == 3:
    print("Selected features:", X.columns[model.coef_ != 0].tolist())
