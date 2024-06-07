"""
Shallow Copy:
A shallow copy creates a new object, but inserts references into it to the objects found in the original. Thus, a shallow copy is not fully independent of the original.

Deep Copy:
A deep copy creates a new object and recursively copies all objects found in the original. Hence, a deep copy is fully independent of the original.
"""


import numpy as np

a = np.array([[[5,8,2],[6,3,9],[7,4,1]]])
print(a)