# makepcadata
# Generate random points in a subspace and add random noise. 
# For Lab 15 in DSCI 369 Fall 2021.
#
# INPUTS:
# basis: An NxK matrix whose columns are a basis of a K-dimensional
#   subspace of R^N
# numpts: How many points to generate
# sigma: The noise level. A higher number means the generated points are
#   spread more from the subspace.
#
# OUTPUTS:
# X: A Nx(numpts) matrix whose columns are the randomly generated data points.
#  This matrix is not yet zero-centered.
#
# AUTHOR:
# Emily J. King, https://www.math.colostate.edu/~king/

import numpy as np

def makepcadata(basis,numpts,sigma):
    X=(basis@np.random.normal(0, 1, size=(basis.shape[1], numpts)))+np.random.normal(0, sigma, size=(basis.shape[0], numpts))
    return(X)