# %% [markdown]
# This part of the notebook imports the tools needed to collect and organize data from the internet. It reads the supplied 2012 student score tables and cleans up the table so we can calculate the results.

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data from the local CSV files provided by the professor
math_df = pd.read_csv('Mathematics_.csv')
read_df = pd.read_csv('Reading_.csv')
sci_df = pd.read_csv('Science_.csv')

# 2. Rename columns to be standard: 'C' becomes 'Country', 'S' becomes the subject score
math_df = math_df.rename(columns={'C': 'Country', 'S': 'Math'})[['Country', 'Math']]
read_df = read_df.rename(columns={'C': 'Country', 'S': 'Reading'})[['Country', 'Reading']]
sci_df = sci_df.rename(columns={'C': 'Country', 'S': 'Science'})[['Country', 'Science']]

# 3. Clean the 'Country' column to remove hidden non-breaking spaces (\xa0) and whitespace
for d in [math_df, read_df, sci_df]:
    d['Country'] = d['Country'].str.replace(r'\s+', ' ', regex=True).str.strip()
    
# 4. Merge all three dataframes together based on the 'Country' column
df = math_df.merge(read_df, on='Country', how='outer').merge(sci_df, on='Country', how='outer')

# 5. Convert score columns to numeric (forces any weird text into NaN)
for col in ['Math', 'Reading', 'Science']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop any rows with missing values
df = df.dropna().reset_index(drop=True)

# 6. CALCULATE THE AVERAGE: This creates the missing 'Average' column required for the assignment!
df['Average'] = df[['Math', 'Reading', 'Science']].mean(axis=1)

print("Success! Data from CSVs loaded, merged, and 'Average' column calculated.")

# %% [markdown]
# This section creates a visual chart called a histogram to show how student scores are spread out. It overlays the math scores and average scores on the same graph with a green dotted grid to match the professor's sample.

# %%
"""
Requirement: Overlapping histograms with green dotted grid.
X-distribution = Average (Red), Y-distribution = Math (Blue)
"""
plt.figure(figsize=(8, 5))
sns.set_style("dark") 

# Plotting overlapping histograms with transparency (alpha) to match the sample
plt.hist(df['Average'], bins=15, color='red', alpha=0.7, label='x distribution', density=True, edgecolor='black', linewidth=0.5)
plt.hist(df['Math'], bins=15, color='blue', alpha=0.5, label='y distribution', density=True, edgecolor='black', linewidth=0.5)

# Applying the specific green dotted grid as required by the sample plot
plt.grid(color='green', linestyle=':', linewidth=1)

# Labels, Title, and Legend
plt.title('Assignment 6')
plt.xlabel('Value Range')
plt.ylabel('Probability')
plt.legend(loc='upper right')
plt.xticks(range(360, 660, 30))

plt.show()

# %% [markdown]
# This code creates a custom function that automatically identifies "outlier" countries with scores that are unusually high or low. It specifically flags any value that is more than 1.8 times the standard deviation away from the typical score.

# %%
def find_outlier(col_name):
    """
    Function logic: Find values more than 1.8 * Standard Deviation from the Mean.
    """
    mean_val = df[col_name].mean()
    std_val = df[col_name].std()
    
    # Calculate limits based on 1.8 standard deviations
    upper_limit = mean_val + (1.8 * std_val)
    lower_limit = mean_val - (1.8 * std_val)
    
    # Identify the outlier countries
    outliers = df[(df[col_name] > upper_limit) | (df[col_name] < lower_limit)]
    outlier_list = outliers['Country'].tolist()
    
    # Print formatted text matching outlier_function.png alignment (<11 ensures spacing is right)
    print(f"The outliers in {col_name:<11} are {outlier_list}")

# Testing the function for all score categories
find_outlier("Average")
find_outlier("Math")
find_outlier("Science")
find_outlier("Reading")
