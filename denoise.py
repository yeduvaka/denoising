import numpy as np

def denoise(Y,A):
    reg_parameter = 1.0
    mu = calc_mean(Y,A,reg_parameter)
    sig = calc_variance(Y,A, reg_parameter)

    return mu,sig

def calc_mean(Y,A,reg_parameter):
    pass

def calc_variance(Y,A,reg_parameter):
    n = np.shape(Y)[0]
    sig = np.zeros((n,n))
    #calculations


    psd_sig = project_to_psd(sig)
    return psd_sig

def project_to_psd(sig):
    pass