# A function to run experiments testing power iteration.

# Input:
# A = DxD matrix
# xin = vector in R^D
# N = number of iterations

# Output:
# xout = vector in R^D which is the result of power iteration / von Mises
# iteration

# Emily J. King
# October 22, 2021

import numpy as np
from numpy.linalg import norm

def poweriter(A, xin, N):
    xout = xin  # initialize xout to be xin
    for ii in range(1,N+1):
        xout = A@xout/norm(A@xout)

    return(xout)    

# Better programming style would test how close consecutive xouts were to
# each other and exit the loop early if they were within some tolerance, but I wanted 
# to keep this as simple as possible since not everyone has seen a for loop.
