from astropy.io import fits
import os

#filename = os.path.join("C:","Users","Stephen","OneDrive - National University of Ireland, Galway", "24-25 FYP", "project-code", "ESO-test-data", "SPHER.2016-03-31T04_00_16.456")
#filename = os.path.join("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/ESO-test-data/SPHER.2016-03-31T04_00_16.456.fits")

def stokes(filename):
    hdul = fits.open(filename)

    #print(repr(hdul[0].header))

    #print("POS2 = ", hdul[0].header['HIERARCH ESO INS3 POS2 POS'])
    #print("POS3 = ", hdul[0].header['HIERARCH ESO INS3 POS3 POS'])
    #print("POS4 = ", hdul[0].header['HIERARCH ESO INS3 POS4 POS'])
    #print("POS5 = ", hdul[0].header['HIERARCH ESO INS3 POS5 POS'])
    #print("POS6 = ", hdul[0].header['HIERARCH ESO INS3 POS6 POS'])
    #print("POS7 = ", hdul[0].header['HIERARCH ESO INS3 POS7 POS'], "\n")
    #print(hdul[0].header['HIERARCH ESO OCS3 ZIMPOL POL STOKES'])

    print(hdul[0].header['HIERARCH ESO INS3 OPTI5 ID'])
    print(hdul[0].header['HIERARCH ESO INS3 OPTI5 NAME'])
    print(hdul[0].header['HIERARCH ESO INS3 OPTI5 NO'])
    print(hdul[0].header['HIERARCH ESO INS3 OPTI5 TYPE'])
    print(hdul[0].header['HIERARCH ESO INS3 OPTI6 ID'])
    print(hdul[0].header['HIERARCH ESO INS3 OPTI6 NAME'])  

    
    
    hdr = hdul[0].header
    #print(list(hdr.keys()))
    #print(repr(hdr))
    #print("\n", hdr['ESO TEL PARANG END'], hdr['ESO TEL PARANG START']) #Prints parallactic angle at end and start
    #print(hdul[0].header['MJD OBS'])
    hdul.close()

stokes("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/GG-Tau-data/SPHER.2024-11-24T03_27_06.147.fits")
