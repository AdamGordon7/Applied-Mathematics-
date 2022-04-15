import numpy as np
from numpy.linalg import inv

def normalize(x):
    fac = abs(x).max()
    x_n = x / x.max()
    return fac, x_n

x = np.array([1, 1])
a = np.array([[-1,0],[0,1]])


a_inv = inv(a)

for i in range(100):
    x = np.dot(a_inv, x)
    lambda_1, x = normalize(x)
    
print('Eigenvalue:', lambda_1)
print('Eigenvector:', x)
