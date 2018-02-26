import numpy as np

def denoise(Y,A):
    reg_parameter = 1.0
    mu = calc_mean(Y,A,reg_parameter)
    sig = calc_variance(Y,A, mu, reg_parameter)
    return mu,sig

def calc_mean(Ys,As,lbd):
    p = np.size(Ys[0])
    n = len(Ys)
    X = sum((lambda x:np.transpose(x)*x, As)) +lbd*np.identity(p)
    Y = sum([np.transpose(As[i])*Ys[i] for i in range(0,n)])
    return np.invert(X)*Y


def calc_variance(Ys,As,mu,reg_parameter):
    n = len(Ys)

    Cs = [(Ys[i]-As[i]*mu)*np.transpose((Ys[i]-As[i]*mu)) for i in range(0,n)]



    sig = np.zeros((n,n))
    #calculations



    psd_sig = project_to_psd(sig)
    return psd_sig

def project_to_psd(sig):
    pass
