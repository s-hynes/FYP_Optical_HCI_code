<<<<<<< HEAD
import scipy.ndimage
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from inputs import saving_dir
 
def GGTau_padding(optical_image, IR_image):
    optical_image_zoomed = scipy.ndimage.zoom(optical_image, 7.2/12.251, order=5)

    IR_x_dim = IR_image.shape[1]
    IR_y_dim = IR_image.shape[0]

    optical_x_dim = optical_image_zoomed.shape[1]
    x_pad = IR_x_dim - optical_x_dim

    optical_y_dim = optical_image_zoomed.shape[0]
    y_pad = IR_y_dim - optical_y_dim

    x_pad_l = int(x_pad/2 + 1/2)
    x_pad_r = int(x_pad/2 - 1/2)
    y_pad_l = int(y_pad/2 + 1/2)
    y_pad_r = int(y_pad/2 - 1/2)

    optical_image_zoomed_padded         = np.pad(optical_image_zoomed, ((x_pad_l, x_pad_r), (y_pad_l, y_pad_r)))
    final_optical_image = np.flipud(optical_image_zoomed_padded)

    return final_optical_image

def GGTau_cropping(optical_image, IR_image):
    IR_image_zoomed = scipy.ndimage.zoom(optical_image, 12.251/7.2)

def normalize(img, cent_star_brightness):

    normalized_image = img / cent_star_brightness

    return normalized_image

if __name__=="__main__":

    hdul = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/The Important Ones/V_GG_Tau_2024-12-22_I_pol_star_pol_subtr-Yband.fits")
    IR_Y_image        = hdul[0].data
    hdul = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/The Important Ones/GGTauA_2016-11-19_I_pol_star_pol_subtr_Hband.fits")
    IR_H_image        = hdul[0].data
    hdul = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/The Important Ones/V_GG_Tau_2024-11-25_I_pol_star_pol_subtr_Kband.fits")
    IR_k_image        = hdul[0].data
    hdul = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/steps_presentation/2025-03-27-Callas-40-Qphi_Rin=6_Rout=7.5.fits")
    optical_image   = hdul[0].data
    hdul.close()

    optical_image_name  = "2025-03-27-Callas-40-Qphi_Rin=6_Rout=7.5"
    IR_y_image_name     = "V_GG_Tau_2024-12-22_I_pol_star_pol_subtr-Yband"
    IR_H_image_name     = "GGTauA_2016-11-19_I_pol_star_pol_subtr_Hband"
    IR_k_image_name     = "V_GG_Tau_2024-11-25_I_pol_star_pol_subtr_Kband"


    zoomed_flipped_optical_image = GGTau_padding(optical_image, IR_k_image)
    optical_image_normalised = normalize(zoomed_flipped_optical_image, 2963116.1)

    IR_Y_image_normalised = normalize(IR_Y_image,  6305964.128)
    IR_H_image_normalised = normalize(IR_H_image, 24163691.68)
    IR_k_image_normalised = normalize(IR_k_image, 29300722.83)



    hdu = fits.PrimaryHDU(data=optical_image_normalised)
    hdu.writeto(saving_dir + "/" + "{0}-".format(dt.date.today()) + optical_image_name + "zoomed_flipped_normalized.fits", overwrite=True)
    hdu = fits.PrimaryHDU(data=IR_Y_image_normalised)
    hdu.writeto(saving_dir + "/" + "{0}-".format(dt.date.today()) + IR_y_image_name + "normalized.fits", overwrite=True)
    hdu = fits.PrimaryHDU(data=IR_H_image_normalised)
    hdu.writeto(saving_dir + "/" + "{0}-".format(dt.date.today()) + IR_H_image_name + "normalized.fits", overwrite=True)
    hdu = fits.PrimaryHDU(data=IR_k_image_normalised)
    hdu.writeto(saving_dir + "/" + "{0}-".format(dt.date.today()) + IR_k_image_name + "normalized.fits", overwrite=True)

    plt.figure(1)
    plt.title("IR image")
    plt.imshow(IR_k_image_normalised, origin='lower', cmap='cividis', norm='symlog')

    plt.figure(2)
    plt.title("Optical image after zooming")
    plt.imshow(optical_image_normalised, origin='lower', cmap='cividis', norm='symlog')
    plt.colorbar()
    plt.show()

=======
import scipy.ndimage
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from inputs import saving_dir
 
def GGTau_padding(optical_image, IR_image):
    optical_image_zoomed = scipy.ndimage.zoom(optical_image, 7.2/12.251, order=5)

    IR_x_dim = IR_image.shape[1]
    IR_y_dim = IR_image.shape[0]

    optical_x_dim = optical_image_zoomed.shape[1]
    x_pad = IR_x_dim - optical_x_dim

    optical_y_dim = optical_image_zoomed.shape[0]
    y_pad = IR_y_dim - optical_y_dim

    x_pad_l = int(x_pad/2 + 1/2)
    x_pad_r = int(x_pad/2 - 1/2)
    y_pad_l = int(y_pad/2 + 1/2)
    y_pad_r = int(y_pad/2 - 1/2)

    optical_image_zoomed_padded         = np.pad(optical_image_zoomed, ((x_pad_l, x_pad_r), (y_pad_l, y_pad_r)))
    final_optical_image = np.flipud(optical_image_zoomed_padded)

    return final_optical_image

def GGTau_cropping(optical_image, IR_image):
    IR_image_zoomed = scipy.ndimage.zoom(optical_image, 12.251/7.2)

def normalize(img, cent_star_brightness):

    normalized_image = img / cent_star_brightness

    return normalized_image

if __name__=="__main__":

    hdul = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/The Important Ones/V_GG_Tau_2024-12-22_I_pol_star_pol_subtr-Yband.fits")
    IR_Y_image        = hdul[0].data
    hdul = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/The Important Ones/GGTauA_2016-11-19_I_pol_star_pol_subtr_Hband.fits")
    IR_H_image        = hdul[0].data
    hdul = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/The Important Ones/V_GG_Tau_2024-11-25_I_pol_star_pol_subtr_Kband.fits")
    IR_k_image        = hdul[0].data
    hdul = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/steps_presentation/2025-03-27-Callas-40-Qphi_Rin=6_Rout=7.5.fits")
    optical_image   = hdul[0].data
    hdul.close()

    optical_image_name  = "2025-03-27-Callas-40-Qphi_Rin=6_Rout=7.5"
    IR_y_image_name     = "V_GG_Tau_2024-12-22_I_pol_star_pol_subtr-Yband"
    IR_H_image_name     = "GGTauA_2016-11-19_I_pol_star_pol_subtr_Hband"
    IR_k_image_name     = "V_GG_Tau_2024-11-25_I_pol_star_pol_subtr_Kband"


    zoomed_flipped_optical_image = GGTau_padding(optical_image, IR_k_image)
    optical_image_normalised = normalize(zoomed_flipped_optical_image, 2963116.1)

    IR_Y_image_normalised = normalize(IR_Y_image,  6305964.128)
    IR_H_image_normalised = normalize(IR_H_image, 24163691.68)
    IR_k_image_normalised = normalize(IR_k_image, 29300722.83)



    hdu = fits.PrimaryHDU(data=optical_image_normalised)
    hdu.writeto(saving_dir + "/" + "{0}-".format(dt.date.today()) + optical_image_name + "zoomed_flipped_normalized.fits", overwrite=True)
    hdu = fits.PrimaryHDU(data=IR_Y_image_normalised)
    hdu.writeto(saving_dir + "/" + "{0}-".format(dt.date.today()) + IR_y_image_name + "normalized.fits", overwrite=True)
    hdu = fits.PrimaryHDU(data=IR_H_image_normalised)
    hdu.writeto(saving_dir + "/" + "{0}-".format(dt.date.today()) + IR_H_image_name + "normalized.fits", overwrite=True)
    hdu = fits.PrimaryHDU(data=IR_k_image_normalised)
    hdu.writeto(saving_dir + "/" + "{0}-".format(dt.date.today()) + IR_k_image_name + "normalized.fits", overwrite=True)

    plt.figure(1)
    plt.title("IR image")
    plt.imshow(IR_k_image_normalised, origin='lower', cmap='cividis', norm='symlog')

    plt.figure(2)
    plt.title("Optical image after zooming")
    plt.imshow(optical_image_normalised, origin='lower', cmap='cividis', norm='symlog')
    plt.colorbar()
    plt.show()

>>>>>>> origin
