import numpy as np

num_list = list(range(100))
# print(num_list)

a = np.array(num_list).reshape(10,10)
print(a)

col_sum = np.sum(a,axis=0) # axis 0 refers to column
print(col_sum)

# To know the row sum:
row_sum = np.sum(a,axis=1)
print(row_sum)