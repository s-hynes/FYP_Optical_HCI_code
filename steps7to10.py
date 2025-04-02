from step7 import double_diff
from step9_man_IP_corr import inst_pol, fix
from step10_azimuthal import azimuthal
from astropy.io import fits
import datetime as dt
import time
import numpy as np
from inputs import save_fits, save_steps, dir_in_str, saving_dir

#data_dir = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/ESO-test-data"
#save_dir = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/steps_presentation"

r_in, r_out = 6, 7.5

def itsready(data_dir:str, save_dir:str, detector:str, savesteps=False):

    hdu_array = double_diff(data_dir, save_dir, detector, savesteps=save_steps)

    Q_im, U_im, Int_Q, Int_U = hdu_array[0:4]

    Q_im_IPcorr = fix(inst_pol(Q_im, Int_Q, 6, 7.5), 100, 200)
    U_im_IPcorr = fix(inst_pol(U_im, Int_U, 6, 7.5), 100, 200)

    PolInt = np.sqrt( Q_im_IPcorr**2 + U_im_IPcorr**2)

    Q_phi, U_phi = azimuthal(Q_im_IPcorr, U_im_IPcorr)

    if savesteps==True:
        if save_fits["Q double difference corrected for instrumental polarisation"]==True:
            hdu = fits.PrimaryHDU(data=Q_im_IPcorr)
            hdu.writeto(save_dir + "/" + "{0}-{1}-".format(dt.date.today(),detector) + "37-Q_corrected_for_instrumental_polarisation_Rin={0}_Rout={1}".format(r_in, r_out)  + ".fits", overwrite=True)
        if save_fits["U double difference corrected for instrumental polarisation"]==True:
            hdu = fits.PrimaryHDU(data=U_im_IPcorr)
            hdu.writeto(save_dir + "/" + "{0}-{1}-".format(dt.date.today(),detector) + "38-U_corrected_for_instrumental_polarisation_Rin={0}_Rout={1}".format(r_in, r_out)  + ".fits", overwrite=True)
        if save_fits["polarised intensity corrected for instrumental polarisation"]==True:
            hdu = fits.PrimaryHDU(data=PolInt)
            hdu.writeto(save_dir + "/" + "{0}-{1}-".format(dt.date.today(),detector) + "39-polarised_intensity_corrected_for_instrumental_polarisation_Rin={0}_Rout={1}".format(r_in, r_out)  + ".fits", overwrite=True)
        if save_fits["Qphi (azimuthal Q)"]==True:
            hdu = fits.PrimaryHDU(data=Q_phi)
            hdu.writeto(save_dir + "/" + "{0}-{1}-".format(dt.date.today(),detector) + "40-Qphi_Rin={0}_Rout={1}".format(r_in, r_out)  + ".fits", overwrite=True)
        if save_fits["Uphi (azimuthal U)"]==True:
            hdu = fits.PrimaryHDU(data=U_phi)
            hdu.writeto(save_dir + "/" + "{0}-{1}-".format(dt.date.today(),detector) + "41-Uphi_Rin={0}_Rout={1}".format(r_in, r_out)  + ".fits", overwrite=True)

    return Q_im_IPcorr, U_im_IPcorr, PolInt, Q_phi, U_phi

def combine(save_dir:str, Callas_image, Bartoli_image, savesteps=False):

    Callas_image = Callas_image.reshape(1,512,512)
    Bartoli_image_xflipped = np.fliplr(Bartoli_image).reshape(1,512,512)

    images_combined = np.average( np.append(Callas_image, Bartoli_image_xflipped, axis=0), axis=0)

    return images_combined

if __name__=="__main__":

    print("\nScript started at: ", time.ctime())
    start_time = time.monotonic()

    data_dir = dir_in_str
    save_dir = saving_dir

    Callas_images = itsready(dir_in_str, saving_dir, "Callas", savesteps=save_steps)
    Bartoli_images = itsready(dir_in_str, saving_dir, "Bartoli", savesteps=save_steps)

    Q_IP_corr_combined = combine(saving_dir, Callas_images[0], Bartoli_images[0], savesteps=save_steps)
    U_IP_corr_combined = combine(saving_dir, Callas_images[1], Bartoli_images[1], savesteps=save_steps)
    PolInt_combined = combine(saving_dir, Callas_images[2], Bartoli_images[2], savesteps=save_steps)
    Q_phi_combined = combine(saving_dir, Callas_images[3], Bartoli_images[3], savesteps=save_steps)
    U_phi_combined = combine(saving_dir, Callas_images[4], Bartoli_images[4], savesteps=save_steps)

    if save_steps==True:
        if save_fits["Q double difference, average of two detectors"]==True:
            hdu = fits.PrimaryHDU(data=Q_IP_corr_combined)
            hdu.writeto(saving_dir + "/" + "{0}-".format(dt.date.today()) + "42-Q_IP_corrected_detectors_combined_Rin={0}_Rout={1}".format(r_in, r_out)  + ".fits", overwrite=True)
        if save_fits["U double difference, average of two detectors"]==True:
            hdu = fits.PrimaryHDU(data=U_IP_corr_combined)
            hdu.writeto(saving_dir + "/" + "{0}-".format(dt.date.today()) + "43-U_IP_corrected_detectors_combined_Rin={0}_Rout={1}".format(r_in, r_out)  + ".fits", overwrite=True)
        if save_fits["polarised intensity, average of two detectors"]==True:
            hdu = fits.PrimaryHDU(data=PolInt_combined)
            hdu.writeto(saving_dir + "/" + "{0}-".format(dt.date.today()) + "44-Polarised_intensity_detectors_combined_Rin={0}_Rout={1}".format(r_in, r_out)  + ".fits", overwrite=True)
        if save_fits["Qphi, average of two detectors"]==True:
            hdu = fits.PrimaryHDU(data=Q_phi_combined)
            hdu.writeto(saving_dir + "/" + "{0}-".format(dt.date.today()) + "45-Qphi_detectors_combined_Rin={0}_Rout={1}".format(r_in, r_out)  + ".fits", overwrite=True)
        if save_fits["Uphi, average of two detectors"]==True:
            hdu = fits.PrimaryHDU(data=U_phi_combined)
            hdu.writeto(saving_dir + "/" + "{0}-".format(dt.date.today()) + "46-Uphi_detectors_combined_Rin={0}_Rout={1}".format(r_in, r_out)  + ".fits", overwrite=True)

    end_time = time.monotonic()
    print("\nTime taken: ", dt.timedelta(seconds=end_time - start_time))
    print("\nScript finished at: \n", time.ctime())



