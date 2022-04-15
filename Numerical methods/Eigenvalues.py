from sympy import *
import numpy as np
import sys as sys

def Hilbert(n):
    H=np.zeros(shape=(n,n))
    for i in range(n):
        for j in range (n):
            H[i][j]=1/((i+1)+(j+1)-1)

    return H



#outfile=open('data.txt', 'w')
#outfile.write(str(Hilbert(123)))
#outfile.close()

A = Matrix(Hilbert(123))
print("Eigenvalues: ")
print(list(A.eigenvals().keys()))

print("EigenVectors")
print([list(tup[2][0]) for tup in A.eigenvects()])
