import astropy
from astropy.io import fits
import numpy as np

def func1(filename):
    """This funtion actually does much more than just opening a FITS file now. At the moment, it removes the
    vertical bar from the middle of the ZIMPOL data and creates two images from the two orthogonal polarisation
    directions."""
    fits_image_filename = 'ESO-test-data/{0}.fits'.format(filename)

    hdul = fits.open(fits_image_filename)

    print(repr(hdul[2].header[:11]))
    image_data = hdul[2].data
    hdul.close()

    #---------------------------------------------------------------------------------------------------------
    # Removing the vertical bar from the centre of the image

    #print(type(image_data))
    #print(image_data.shape)
    #print(image_data)
    #print("")
    bar_3d = image_data[:, :, 537:619]  # This should probably be given as an optional output of the function
                                        # or saved somewhere.
    #bar_3d = image_data[:, :, 534:540]
    #print(bar_3d)
    no_bar_3d = np.delete(image_data, range(537,619), axis=2)
    """A Boolean mask might be better than using np.delete. The Numpy documentation itself says this
    so it might be worth looking into."""
    #print(no_bar_3d.shape)

    hdu = fits.PrimaryHDU(data=no_bar_3d)
    hdu.writeto('manipulated-data/bar-removed/{0}_no_bar.fits'.format(filename), overwrite=True)

    #---------------------------------------------------------------------------------------------------------
    # Splicing individual polarisation directions

    im_pol1 = no_bar_3d[:,  ::2, :]
    im_pol2 = no_bar_3d[:, 1::2, :]
    #print(im_pol1.shape)
    #print(im_pol2.shape)

    hdu1 = fits.PrimaryHDU(data=im_pol1)
    hdu2 = fits.PrimaryHDU(data=im_pol2)
    hdu1.writeto('manipulated-data/polarisation-directions/{0}_pol1.fits'.format(filename), overwrite=True)
    hdu2.writeto('manipulated-data/polarisation-directions/{0}_pol2.fits'.format(filename), overwrite=True)

    #with fits.open(fits_image_filename) as hdul:
        #hdul.info()

number = '2_30_30.441'
func1('SPHER.2016-03-31T0{0}'.format(number))  
"""The parts that are common to each filename could also be put inside the function as well. This might make it 
too specific to the files that I'm currently using though."""