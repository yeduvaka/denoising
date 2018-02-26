import numpy as np
import helper as hp
import input as ip
import denoise as dn
import random


#Input images are a list of numpy 2D arrays (all same size?)
# Colored noise
def estimate_covariance(input_images):
    #Number of images and pixels
    n = len(input_images)
    p = np.size(input_images[0])
    low = 0.75
    hi = 1.5
    #what is this value
    noise_var = 1

    #Estimate the whitening filter
    #For uncolored noise set W to be identity
    W = dn.estimate_whitening_filter(input_images)

    #Fourier transform and multiply by random alpha
    Ys = (lambda x: random.uniform(low,hi)*hp.fft(x), input_images)

    # "Whitened images"
    WYs = (lambda x: W*x, Ys) #Check if this is matrix mul or element-wise
    wys = (lambda x:np.vectorize(x), WYs)

    #Read in the point spread and Fourier transform it
    point_spread = ip.read_microscopy_spread()
    As = (lambda x: hp.fft(x),point_spread)

    mu,sigw = dn.denoise(wys,As)
    sig = np.invert(W)*(sigw)*np.invert(np.transpose(W))

    def H(i):
        A = sig * np.transpose(As[i]) * np.transpose(W)
        B = W * As[i]*sig*np.transpose(As[i])*np.transpose(W)
        C = np.invert(B + noise_var*np.identity(p))
        return A*C

    Hs = [H(i) for i in range(0,n)]
    return Ys,mu,As,W,Hs

def apply_wiener_filter(Ys,mu,As,W,Hs):
    p = len(Ys[0])
    Xs = [((np.identity(p) - Hs[i]*W*As[i])*mu +Hs[i]*y) for i,y in enumerate(Ys)]
    return Xs

def main(input_images):
    Ys,mu,As,W,Hs = estimate_covariance(input_images)
    X_hats = apply_wiener_filter(Ys,mu,As,W,Hs)

    return None








