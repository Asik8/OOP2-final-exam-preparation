import numpy as np

num_list = list(range(100))

# i
a= np.array(num_list)
print(a)

# ii
b = np.array(num_list).reshape(10,10)
print(b)


# iii
s = np.sum(b,axis=0)
print(s)
