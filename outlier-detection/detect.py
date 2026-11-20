# %% [markdown]
# # Module 5: Anomaly Detection
# This notebook implements an iterative anomaly detection function based on the mean and standard deviation of a dataset.
# 
# ### Mathematical Definition of an Anomaly:
# An element $X$ in a dataset $D$ is defined as an anomaly if the difference between $X$ and the mean ($\mu$) of the dataset *without* $X$ is greater than three times the standard deviation ($\sigma$) of the dataset *without* $X$:
# $$|X - \mu_{D \setminus \{X\}}| > 3 \times \sigma_{D \setminus \{X\}}$$
# 
# The algorithm iteratively searches the dataset for the most significant anomaly, removes it, and repeats the process until no more anomalies are detected.

# %%
import numpy as np

def anomaly_detection(x):
    """
    Function to detect and remove anomalies iteratively.
    Input: numpy array or list (x)
    Logic: Compares each point X to the stats of the list excluding X.
    """
    # Convert input to a list so we can easily remove elements
    data_list = list(x)
    
    while len(data_list) >= 3:
        # We track the most extreme anomaly in each pass
        max_ratio = -1
        target_value = None
        
        # Iteratively check every element in the current list
        for i in range(len(data_list)):
            current_val = data_list[i]
            
            # Create a temporary subset excluding the current point (D without X)
            remaining_data = [data_list[j] for j in range(len(data_list)) if i != j]
            
            # Calculate mean (Mu) and standard deviation (STD) of the subset
            mu = np.mean(remaining_data)
            std = np.std(remaining_data) # Using population std (ddof=0)
            
            # Calculate the difference and its ratio to the standard deviation
            diff = abs(current_val - mu)
            ratio = diff / std if std > 0 else (float("inf") if diff > 0 else 0.0)
            
            # Rule: If difference > 3 * STD, it is a potential anomaly
            if ratio > 3 and ratio > max_ratio:
                max_ratio = ratio
                target_value = current_val
        
        # If an anomaly was found, remove it and print the required message
        if target_value is not None:
            print(f"Remove {target_value:.2f} from the list because it's {max_ratio:.2f} times of standard deviation of the list without it.")
            print(f"{target_value:.2f} is removed from the list!\n")
            
            # Remove the specific element and loop again
            data_list.remove(target_value)
        else:
            # If no point exceeds the 3xSTD threshold, the process ends
            print("No more anomaly is detected!")
            break

# Requirement 1: Read data from anomaly_detection.txt
try:
    # Open file and convert lines to a list of floats
    with open('anomaly_detection.txt', 'r') as file:
        raw_data = [float(line.strip()) for line in file if line.strip()]
    
    # Assign the data to a numpy array (x)
    x = np.array(raw_data)
    
    # Requirement 2: Call the function
    anomaly_detection(x)

except FileNotFoundError:
    print("Error: The file 'anomaly_detection.txt' was not found in the current directory.")
