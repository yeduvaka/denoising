import numpy as np

# Compute the 2D Fouier Tranform of a micrograph
def fft(x):
    return np.fft.fft2(x)