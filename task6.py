import numpy as np
A=np.zeros((100,100))
def nonzero(A):
    nonzero_coordinates = np.nonzero(A)
    x = nonzero_coordinates[0][0]
    y = nonzero_coordinates[1][0]
    return x,y

A[56][70]=1

print(nonzero(A))
