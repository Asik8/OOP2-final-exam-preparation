import numpy as np

# i. 
a = np.zeros((4, 3))
a[0] = np.arange(1, 4)
a[2] = np.arange(5, 8)
# print(a)

main_diagonal = np.diagonal(a)
above_diagonal = np.diagonal(a, offset=1)
below_diagonal = np.diagonal(a, offset=-1)

# print("Main diagonal:", main_diagonal)
# print("Above diagonal:", above_diagonal)
# print("Below diagonal:", below_diagonal)

# ---------------------------------------------------------------------
# II
b = a.reshape(3,4)
print(b)

mean_values = np.mean(b[:, 1:4], axis=0)
max_values = np.max(b[:, 1:4], axis=0)
variance_values = np.var(b[:, 1:4], axis=0)

print("Mean values:", mean_values)
print("Max values:", max_values)
print("Variance values:", variance_values)


# iii. Describe the difference
"""
NumPy arrays allow access to elements via indexing and slicing, and they provide
efficient operations on large data sets. Memory is contiguous, making operations fast.
NumPy arrays can be accessed in multiple dimensions and offer broadcasting, which
is not available in regular Python lists.
"""
