# NSCSmatmul
# Compute high pass (hard threshold) filtered output
#
# INPUTS:
# v = LxC sound matrix, where C is the number of channels
# t = frequncy threshold
#
# OUTPUT:
# vtil = high pass filtered output of the same size as v
#
# AUTHOR:
# Emily J. King https://www.math.colostate.edu/~king/

import numpy as np

def NSCSmatmul(v,t):
    [L,C]=v.shape
    V=np.fft.fft(v.T)
    vtil=np.fft.ifft(np.hstack((np.zeros([C,t+1]),V[:,t+1:L-t],np.zeros([C,t])))).T
    return vtil