# Patient Age Analysis Script
## Analyzes a list of patient ages to find statistics and filter by age grups

import numpy as np
from numpy import random as rd

# Create a lit of patients (Px) ages
# patient_ages = [7, 23, 56, 78, 43, 24, 12, 19, 34, 60]

px_ages = rd.randint(1,100, size=(10)) # 1-D array
print(px_ages)

# px_ages = px_ages.tolist() # array 2 list
# print(px_ages)

# Calculate average
avg_age = sum(px_ages)/len(px_ages)
print(f"the average age is: {avg_age}")

# Calculate average
# avg_age = np.mean(px_ages)
# print(f"the average age is: {avg_age}")

# Comprenhension list
ages_older_50 = [age for age in px_ages if age > 50]

# Filter method
ages_older_50 = list(filter(lambda age: age > 50, px_ages))

# Print results in a formatted way
print("=" * 40)
print("PATIENT AGE ANALYSIS")
print("=" * 40)
print(f"The total patient: {len(px_ages)}")
print(f"The average age is: {avg_age}")
print(f"The youngest patient: {min(px_ages)} years")
print(f"The oldest patient: {max(px_ages)} years")
print(f"The older patients than 50 are: {ages_older_50}")
print(f"Count: {len(ages_older_50)} patients ({len(ages_older_50)/ len(px_ages)*100:.1f}%)")
