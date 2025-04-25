import pandas as pd
import numpy as np

data = {
    'Name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily'],
    'Score': [12.5, 9, 16.5, np.nan, 9],
    'Attempts': [1, 3, 2, np.nan, 2],
    'Qualify': ['yes', 'no', 'yes', 'no', np.nan]
}
df = pd.DataFrame(data)


print("Original DataFrame:")
print(df)


df['Score'].fillna(0, inplace=True)  
df['Attempts'].fillna(0, inplace=True)  
df['Qualify'].fillna('unknown', inplace=True)  

print("\nUpdated DataFrame after replacing missing values:")
print(df)