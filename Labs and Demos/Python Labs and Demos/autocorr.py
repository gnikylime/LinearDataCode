# autocorr
# Compute cyclic autocorrelation of x.
#
# INPUT:
# x: A 1D array with d entries.
#
# OUTPUTS:
# X: The cycle autocorrelation of x. A 1D array with d entries.
#
# AUTHOR:
# Emily J. King

import numpy as np

def autocorr(x):
    X=np.real(np.fft.ifft(np.conj(np.fft.fft(x))*np.fft.fft(x)))
    return(X)
