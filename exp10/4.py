import pandas as pd
import numpy as np

data = {'X': [78, 85, 96, 80, 86], 
        'Y': [84, 94, 89, 83, 86], 
        'Z': [86, 97, 96, 72, 83]}
df = pd.DataFrame(data)


print("Original DataFrame:")
print(df)

powers_df = pd.DataFrame(
    {col: np.power(df[col], range(len(df[col]))) for col in df.columns}
)


print("\nElement-wise powers:")
print(powers_df)