import numpy as np
array=np.array([[5, 8, 3],
                  [6, 9, 4],
                  [2, 7, 1]])

rowsums=np.sum(array,axis=1)
columnsums=np.sum(array,axis=0)
flattenedarray=array.flatten()
secondmaximum= np.sort(flattenedarray)[-2]
print("Original Array:")
print(array)
print("\nSum of all rows:")
print(rowsums)
print("\nSum of all columns:")
print(columnsums)
print("\nSecond maximum element:")
print(secondmaximum)