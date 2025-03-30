<<<<<<< HEAD
from step1 import overscan, double_phase_mode
from step3 import splice_rows
from step3b_tidy import centre_star
from step4 import single_diff_pol, intensity
from step5 import dedither
from step6 import binning
from astropy.io import fits
import numpy as np
import datetime as dt
from inputs import save_fits, save_steps, saving_dir, dir_in_str
import time

def func(data_dir:str, file:str, save_dir:str, detector:str, Stokes, savesteps=False): 
    """Placeholder terribly generic name for this function. It performs steps 1 to 6."""

    zero    = double_phase_mode(data_dir + "/" + file, detector)[0]
    pi      = double_phase_mode(data_dir + "/" + file, detector)[1]

    zero_no_overscan = overscan(zero)
    pi_no_overscan   = overscan(pi)

    ord_0 = splice_rows(zero_no_overscan, phase="0")[0]
    ext_0 = splice_rows(zero_no_overscan, phase="0")[1]

    ord_pi = splice_rows(pi_no_overscan, phase="pi")[0]
    ext_pi = splice_rows(pi_no_overscan, phase="pi")[1]

    ord_0_centred   = centre_star(ord_0)
    ext_0_centred   = centre_star(ext_0)
    ord_pi_centred  = centre_star(ord_pi)
    ext_pi_centred  = centre_star(ext_pi)
    """
    ord_0_centred   = ord_0
    ext_0_centred   = ext_0
    ord_pi_centred  = ord_pi
    ext_pi_centred  = ext_pi
    """

    # Complete fudge here to fix the Stokes Q single difference images. When I have more time I'll work out
    # what's actually going wrong.
    if Stokes=="Qplus" or Stokes=="Qminus":
        sing_diff_rectangular = -single_diff_pol(ord_0_centred, ord_pi_centred, ext_0_centred, ext_pi_centred)
    if Stokes=="Uplus" or Stokes=="Uminus":
        sing_diff_rectangular = single_diff_pol(ord_0_centred, ord_pi_centred, ext_0_centred, ext_pi_centred)
    int_rectangular = intensity(ord_0_centred, ord_pi_centred, ext_0_centred, ext_pi_centred) 

    #sing_diff_undithered = dedither(sing_diff_rectangular, data_dir + "/" + file)
    #int_undithered = dedither(int_rectangular, data_dir + "/" + file)

    sing_diff_square = binning(sing_diff_rectangular)
    int_square = binning(int_rectangular)

    if savesteps==True:
    
        hdul = fits.open( data_dir + "/" + file)
        Stokes = hdul[0].header['HIERARCH ESO OCS3 ZIMPOL POL STOKES']
        hdul.close()

        if save_fits["0 overscan removed"]==True:
            hdu = fits.PrimaryHDU(data=zero_no_overscan)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-03-zero_no_overscan.fits', overwrite=True)
        if save_fits["pi overscan removed"]==True:
            hdu = fits.PrimaryHDU(data=pi_no_overscan)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-04-pi_no_overscan.fits', overwrite=True)
        if save_fits["0 ordinary ray"]==True:
            hdu = fits.PrimaryHDU(data=ord_0)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-05-zero_ord.fits', overwrite=True)
        if save_fits["0 extraordinary ray"]==True:
            hdu = fits.PrimaryHDU(data=ext_0)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-06-zero_ext.fits', overwrite=True)
        if save_fits["pi ordinary ray"]==True:
            hdu = fits.PrimaryHDU(data=ord_pi)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-07-pi_ord.fits', overwrite=True)
        if save_fits["pi extraordinary ray"]==True:
            hdu = fits.PrimaryHDU(data=ext_pi)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-08-pi_ext.fits', overwrite=True)
        if save_fits["0 ordinary ray, star centered"]==True:
            hdu = fits.PrimaryHDU(data=ord_0_centred)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-09-zero_ord_centered.fits', overwrite=True)
        if save_fits["0 extraordinary ray, star centered"]==True:
            hdu = fits.PrimaryHDU(data=ext_0_centred)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-10-zero_ext_centered.fits', overwrite=True)
        if save_fits["pi ordinary ray, star centered"]==True:
            hdu = fits.PrimaryHDU(data=ord_pi_centred)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-11-pi_ord_centered.fits', overwrite=True)
        if save_fits["pi extraordinary ray, star centered"]==True:
            hdu = fits.PrimaryHDU(data=ext_pi_centred)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-12-pi_ext_centered.fits', overwrite=True)
        if save_fits["single difference 1024x512"]==True:
            hdu = fits.PrimaryHDU(data=sing_diff_rectangular)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-13-sing_diff_pol.fits', overwrite=True)
        if save_fits["intensity 1024x512"]==True:
            hdu = fits.PrimaryHDU(data=int_rectangular)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-14-sing_diff_int.fits', overwrite=True)
        if save_fits["single difference 512x512"]==True:
            hdu = fits.PrimaryHDU(data=sing_diff_square)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-15-sing_diff_pol_binned.fits', overwrite=True)
        if save_fits["intensity 512x512"]==True:
            hdu = fits.PrimaryHDU(data=int_square)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-16-sing_diff_int_binned.fits', overwrite=True)

    return sing_diff_square, int_square

if __name__=="__main__":
    start_time = time.monotonic()
    print("\nScript started at: ", time.ctime())
    
    #Uplus
    # SPHER.2016-03-31T04_00_16.456
    #Qplus
    # SPHER.2016-03-31T04_03_03.433.fits

    #data_dir = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/ESO-test-data"
    #save_dir = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/steps_presentation"

    data_dir = dir_in_str
    save_dir = saving_dir
    filename = "SPHER.2016-03-31T04_06_44.299.fits"

    hdul = fits.open( data_dir + "/" + filename)
    Stokes = hdul[0].header['HIERARCH ESO OCS3 ZIMPOL POL STOKES']
    hdul.close()
    print("\nStokes = {0}\n".format(Stokes))


    func(data_dir, filename, save_dir, "Callas", Stokes,savesteps=save_steps)
    
    end_time = time.monotonic()
    print("\nTime taken: ", dt.timedelta(seconds=end_time - start_time))
=======
from step1 import overscan, double_phase_mode
from step3 import splice_rows
from step3b_tidy import centre_star
from step4 import single_diff_pol, intensity
from step5 import dedither
from step6 import binning
from astropy.io import fits
import numpy as np
import datetime as dt
from inputs import save_fits, save_steps, saving_dir, dir_in_str
import time

def func(data_dir:str, file:str, save_dir:str, detector:str, Stokes, savesteps=False): 
    """Placeholder terribly generic name for this function. It performs steps 1 to 6."""

    zero    = double_phase_mode(data_dir + "/" + file, detector)[0]
    pi      = double_phase_mode(data_dir + "/" + file, detector)[1]

    zero_no_overscan = overscan(zero)
    pi_no_overscan   = overscan(pi)

    ord_0 = splice_rows(zero_no_overscan, phase="0")[0]
    ext_0 = splice_rows(zero_no_overscan, phase="0")[1]

    ord_pi = splice_rows(pi_no_overscan, phase="pi")[0]
    ext_pi = splice_rows(pi_no_overscan, phase="pi")[1]

    ord_0_centred   = centre_star(ord_0)
    ext_0_centred   = centre_star(ext_0)
    ord_pi_centred  = centre_star(ord_pi)
    ext_pi_centred  = centre_star(ext_pi)
    """
    ord_0_centred   = ord_0
    ext_0_centred   = ext_0
    ord_pi_centred  = ord_pi
    ext_pi_centred  = ext_pi
    """

    # Complete fudge here to fix the Stokes Q single difference images. When I have more time I'll work out
    # what's actually going wrong.
    if Stokes=="Qplus" or Stokes=="Qminus":
        sing_diff_rectangular = -single_diff_pol(ord_0_centred, ord_pi_centred, ext_0_centred, ext_pi_centred)
    if Stokes=="Uplus" or Stokes=="Uminus":
        sing_diff_rectangular = single_diff_pol(ord_0_centred, ord_pi_centred, ext_0_centred, ext_pi_centred)
    int_rectangular = intensity(ord_0_centred, ord_pi_centred, ext_0_centred, ext_pi_centred) 

    #sing_diff_undithered = dedither(sing_diff_rectangular, data_dir + "/" + file)
    #int_undithered = dedither(int_rectangular, data_dir + "/" + file)

    sing_diff_square = binning(sing_diff_rectangular)
    int_square = binning(int_rectangular)

    if savesteps==True:
    
        hdul = fits.open( data_dir + "/" + file)
        Stokes = hdul[0].header['HIERARCH ESO OCS3 ZIMPOL POL STOKES']
        hdul.close()

        if save_fits["0 overscan removed"]==True:
            hdu = fits.PrimaryHDU(data=zero_no_overscan)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-03-zero_no_overscan.fits', overwrite=True)
        if save_fits["pi overscan removed"]==True:
            hdu = fits.PrimaryHDU(data=pi_no_overscan)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-04-pi_no_overscan.fits', overwrite=True)
        if save_fits["0 ordinary ray"]==True:
            hdu = fits.PrimaryHDU(data=ord_0)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-05-zero_ord.fits', overwrite=True)
        if save_fits["0 extraordinary ray"]==True:
            hdu = fits.PrimaryHDU(data=ext_0)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-06-zero_ext.fits', overwrite=True)
        if save_fits["pi ordinary ray"]==True:
            hdu = fits.PrimaryHDU(data=ord_pi)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-07-pi_ord.fits', overwrite=True)
        if save_fits["pi extraordinary ray"]==True:
            hdu = fits.PrimaryHDU(data=ext_pi)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-08-pi_ext.fits', overwrite=True)
        if save_fits["0 ordinary ray, star centered"]==True:
            hdu = fits.PrimaryHDU(data=ord_0_centred)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-09-zero_ord_centered.fits', overwrite=True)
        if save_fits["0 extraordinary ray, star centered"]==True:
            hdu = fits.PrimaryHDU(data=ext_0_centred)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-10-zero_ext_centered.fits', overwrite=True)
        if save_fits["pi ordinary ray, star centered"]==True:
            hdu = fits.PrimaryHDU(data=ord_pi_centred)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-11-pi_ord_centered.fits', overwrite=True)
        if save_fits["pi extraordinary ray, star centered"]==True:
            hdu = fits.PrimaryHDU(data=ext_pi_centred)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-12-pi_ext_centered.fits', overwrite=True)
        if save_fits["single difference 1024x512"]==True:
            hdu = fits.PrimaryHDU(data=sing_diff_rectangular)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-13-sing_diff_pol.fits', overwrite=True)
        if save_fits["intensity 1024x512"]==True:
            hdu = fits.PrimaryHDU(data=int_rectangular)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-14-sing_diff_int.fits', overwrite=True)
        if save_fits["single difference 512x512"]==True:
            hdu = fits.PrimaryHDU(data=sing_diff_square)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-15-sing_diff_pol_binned.fits', overwrite=True)
        if save_fits["intensity 512x512"]==True:
            hdu = fits.PrimaryHDU(data=int_square)
            hdu.writeto(save_dir + '/{0}-'.format(dt.date.today()) + file + '--' + detector + '-' + Stokes + '-16-sing_diff_int_binned.fits', overwrite=True)

    return sing_diff_square, int_square

if __name__=="__main__":
    start_time = time.monotonic()
    print("\nScript started at: ", time.ctime())
    
    #Uplus
    # SPHER.2016-03-31T04_00_16.456
    #Qplus
    # SPHER.2016-03-31T04_03_03.433.fits

    #data_dir = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/ESO-test-data"
    #save_dir = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/steps_presentation"

    data_dir = dir_in_str
    save_dir = saving_dir
    filename = "SPHER.2016-03-31T04_06_44.299.fits"

    hdul = fits.open( data_dir + "/" + filename)
    Stokes = hdul[0].header['HIERARCH ESO OCS3 ZIMPOL POL STOKES']
    hdul.close()
    print("\nStokes = {0}\n".format(Stokes))


    func(data_dir, filename, save_dir, "Callas", Stokes,savesteps=save_steps)
    
    end_time = time.monotonic()
    print("\nTime taken: ", dt.timedelta(seconds=end_time - start_time))
>>>>>>> origin
    print("\nScript finished at: \n", time.ctime())