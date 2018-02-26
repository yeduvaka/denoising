# Denoising and determining particles and non-particles

## Structure
main.py contains most of the core logic. It estimates 
the covariance of the images and then applies the Wiener
filter using the obtained covariance matrix. 

## Input
'As' is the list of pxp matrices that represent the
Fourier transform of the point spread function.

'Ys' - images in Fourier co-ordinates

W - the whitening filter. 

