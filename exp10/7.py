import pandas as pd
import numpy as np


data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [15, 30, 45, 10],
    'Squared Values': [x**2 for x in [15, 30, 45, 10]],
    'Normalized Values': [x / sum([15, 30, 45, 10]) for x in [15, 30, 45, 10]]
}


df = pd.DataFrame(data)


print("Original Data Table:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

print("\nElement-wise Operations (Multiplying 'Values' by 2):")
df['Values'] *= 2
print(df)

print("\nSorting by 'Values' Column:")
sorted_df = df.sort_values(by='Values', ascending=False)
print(sorted_df)

print("\nGroup-by Example (Group by 'Category'):")
grouped = df.groupby('Category').sum()
print(grouped)