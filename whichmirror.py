import os
import astropy
from astropy.io import fits

dir_in_str = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/ESO-test-data"

directory = os.fsdecode(dir_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".fits"):
        hdul = fits.open( directory + "/" + filename)
        hdul.close()

        print("POS2 = {0}, POS3 = {1}, POS4 = {2}, POS5 = {3}, POS6 = {4}, POS7 = {5} \n".format(hdul[0].header['HIERARCH ESO INS3 POS2 POS'], 
            hdul[0].header['HIERARCH ESO INS3 POS3 POS'], hdul[0].header['HIERARCH ESO INS3 POS4 POS'], hdul[0].header['HIERARCH ESO INS3 POS5 POS'],
            hdul[0].header['HIERARCH ESO INS3 POS6 POS'], hdul[0].header['HIERARCH ESO INS3 POS7 POS']))