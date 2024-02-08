import pandas as pd
import re

def total_rabbit_pairs_dynamic(n, m):
    # Initialize an array to store the number of rabbits for each month
    rabbits = [0] * (n + 1)
    
    # Set the initial conditions
    rabbits[1] = 1
    rabbits[2] = 1

    # Calculate the number of rabbits for each subsequent month
    for i in range(3, n + 1):
        rabbits[i] = rabbits[i - 1] + rabbits[i - 2] + rabbits[i - 3]
    
    return rabbits[n]

# Example usage of the function
n_example = 35
k_example = 5
total_pairs_example = total_rabbit_pairs_dynamic(n_example, k_example)

print(total_pairs_example)