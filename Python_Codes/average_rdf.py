import pandas as pd
import numpy as np

def calculate_weighted_avg(file, min_range, max_range):
    # Load data from text file into a pandas DataFrame
    data = pd.read_csv(file, sep="\s+", header=None)

    # Filter the data based on the range
    data_in_range = data[(data[0] >= min_range) & (data[0] <= max_range)]

    # Calculate the average of the first column (which is the distance)
    weighted_avg_distance = np.average(data_in_range[0], weights=data_in_range[1])

    print(f"The average distance for the data in {file} in range {min_range} to {max_range} is: {weighted_avg_distance}")

# Specify your file path and range
file = "cw-o3.txt"
min_range = 2.225
max_range = 2.775

calculate_weighted_avg(file, min_range, max_range)