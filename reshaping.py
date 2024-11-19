import numpy as np

# Create a 1D array
od = np.array([1, 2, 3, 4, 5, 6])
print("Original array:")
print(od)

# Reshape the array to (2, 3)
rs = od.reshape(2, 3)
print("\nReshaped array (2, 3):")
print(rs)

# Reshape the array to (3, 2)
rd = od.reshape(3, 2)
print("\nReshaped array (3, 2):")
print(rd)

