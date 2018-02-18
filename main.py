import numpy as np
import helper as hp
import input as ip
import denoise as dn

def estimate_covariance(input_images):
    Y = (lambda x: hp.fft(x),input_images)
    point_spread = ip.read_microscopy_spread()
    A = (lambda x: hp.fft(x),point_spread)
    # Might need to vectorize Y and A
    mu,sig = dn.denoise(Y,A)
    return mu,sig

def main(input_images):
    mu,sig = estimate_covariance(input_images)





