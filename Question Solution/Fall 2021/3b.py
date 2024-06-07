import numpy as np

def multiply(a, b):
    n_a = np.array(a)
    n_b = np.array(b)
    
    if n_a.shape != n_b.shape or n_a.shape[0] != n_a.shape[1]:
        print("Shape of those matrix is not same")
        return
    
    d1 = np.diagonal(n_a)
    d2 = np.diagonal(n_b)
    
    result = d1*d2
    
    print("Multiplied diagonal elements:", result)

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

multiply(a, b)
