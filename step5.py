"""This script carries out step 5, removing dithering from the images."""
import numpy as np
from astropy.io import fits
import scipy.ndimage 

def dedither(img, fits_file:str):

    hdul = fits.open(fits_file)

    x_shift = hdul[0].header['HIERARCH ESO INS3 POS4 POS']  # Finds the x-value for dithering in the fits file
    y_shift = hdul[0].header['HIERARCH ESO INS3 POS4 POS']  # Finds the y-value for dithering in the fits file
    hdul.close()

    shifted_img = scipy.ndimage.shift(img, [y_shift/2, x_shift])

    # In Christian's IRDIS pipeline: x_shift = [1024-1]/2 - x_star - x_dith
    # x_dith = hdul[0].header['HIERARCH ESO INS3 POS3 POS']

    return shifted_img

if __name__ == "__main__":
    pass