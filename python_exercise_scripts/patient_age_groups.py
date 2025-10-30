"""
Patient Age Groups Analysis
Categorizes patients by age groups and provides statistics
"""

import numpy as np
from numpy import random as rd

px_ages = (rd.randint(1,100, size=(20))).tolist() # 1-D array
print(px_ages)

# Create dictionary with age group categories
age_groups = {
    'Children (0-12)': [],
    'Teenagers (13-17)': [],
    'Adults (18-59)': [],
    'Seniors (60+)': []
}

def categorize_by_age(age_list):
  """
  Categorizes a list of ages into age groups
  """

  for age in age_list:

    if age <= 12:
      age_groups["Children (0-12)"].append(age)

    elif 12 < age < 18:
      age_groups["Teenagers (13-17)"].append(age)

    elif 18 <= age < 60:
      age_groups["Adults (18-59)"].append(age)

    else:
      age_groups["Seniors (60+)"].append(age)


categorize_by_age(px_ages)

# # Function to categorize a single age
# def categorize_by_age(age):
#     """
#     Categorizes a single age into an age group
#     Returns the category name
#     """
#     if age <= 12:
#         return 'Children (0-12)'
#     elif age <= 17:
#         return 'Teenagers (13-17)'
#     elif age <= 59:
#         return 'Adults (18-59)'
#     else:
#         return 'Seniors (60+)'

# # Categorize all patients
# for age in px_ages:
#     category = categorize_by_age(age)
#     age_groups[category].append(age)  # This is how you add to the dictionary list!

print(age_groups)

# print("=" * 40)
# print("PATIENT AGE GROUPS ANALYSIS")
# print("=" * 40)
# print("\n")
# print("Total Patients:", len(px_ages))
# print("\n")
# print(f"Children (0-12):\n Count: {len(age_groups["Children (0-12)"])} patients \n Percentaje {len(age_groups["Children (0-12)"])/ len(px_ages)*100:.1f}% \n Ages: {age_groups['Children (0-12)']}")
# print("\n")
# print(f"Teenagers (13-17):\n Count: {len(age_groups["Teenagers (13-17)"])} patients \n Percentaje {len(age_groups["Teenagers (13-17)"])/ len(px_ages)*100:.1f}% \n Ages: {age_groups['Teenagers (13-17)']}")
# print("\n")
# print(f"Adults (18-59):\n Count: {len(age_groups["Adults (18-59)"])} patients \n Percentaje {len(age_groups["Adults (18-59)"])/ len(px_ages)*100:.1f}% \n Ages: {age_groups['Adults (18-59)']}")
# print("\n")
# print(f"Seniors (60+):\n Count: {len(age_groups["Seniors (60+)"])} patients \n Percentaje {len(age_groups["Seniors (60+)"])/ len(px_ages)*100:.1f}% \n Ages: {age_groups['Seniors (60+)']}")


for group_name, ages in age_groups.items():
  count = len(ages)
  percentage = count / len(px_ages) * 100
  print(f"{group_name}")
  print(f"Count: {count} patients")
  print(f"Percentage: {percentage:.1f}%")
  print(f"Ages: {sorted(ages)}")
  print("=" * 40)
