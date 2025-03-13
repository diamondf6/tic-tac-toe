import pandas as pd
import os

def find_s_algorithm(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return None

    # Read the CSV file
    data = pd.read_csv(file_path)
    print("Training data:")
    print(data)

    # Define attributes and class label
    attributes = data.columns[:-1]
    class_label = data.columns[-1]
    
    # Initialize hypothesis
    hypothesis = ['?' for _ in attributes]

    # Apply Find-S Algorithm
    for index, row in data.iterrows():
        if row[class_label] == 'Yes':  # Consider only positive examples
            for i, value in enumerate(row[attributes]):
                if hypothesis[i] == '?' or hypothesis[i] == value:
                    hypothesis[i] = value
                else:
                    hypothesis[i] = '?'
    
    return hypothesis

# Set the correct file path
file_path = r"E:\python Programming\tic\training_data.csv"

# Run the function
hypothesis = find_s_algorithm(file_path)

# Print the final hypothesis if the file exists
if hypothesis:
    print("\nThe final hypothesis is:", hypothesis)
