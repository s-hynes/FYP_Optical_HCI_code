import numpy as np
from photutils.aperture import CircularAperture, ApertureStats, CircularAnnulus
import matplotlib.pyplot as plt
from astropy.io import fits
import datetime as dt

c_x, c_y = 255.75, 255.5

def inst_pol(diff_im, int_im, Rin, Rout):

    deg_pol = diff_im / int_im

    c_x, c_y = 255.75, 255.5

    """
    pixels_in_circle = []

    for i in range(deg_pol.shape[0]):
        for j in range(deg_pol.shape[1]):
            if (i - c_x)**2 + (j - c_y)**2 <= R**2:
                pixels_in_circle.append(deg_pol[i,j])

    median = np.median(pixels_in_circle)

    print("\nMedian using Numpy method = {0}".format(median))

    """

    aper = CircularAnnulus( (c_x, c_y), Rin, Rout)
    aperstats = ApertureStats(deg_pol, aper)
    median = aperstats.median

    print(median)

    #print("Median using photutils.ApertureStats = {0}".format(aperstats.median))

    IP_corrected = diff_im - median * int_im

    #circle = plt.Circle( (c_x, c_y), R, color='green', fill=False)

    """
    plt.figure(1)
    plt.imshow(diff_im, origin ='lower', cmap='hot', norm='symlog')
    aper.plot(color='green', lw = 1);
    plt.colorbar()

    plt.figure(2)
    plt.imshow(int_im, origin ='lower', cmap='hot', norm='symlog')
    aper.plot(color='green', lw = 1);
    plt.colorbar()
    
    plt.figure(3)
    #fig, ax = plt.subplots()
    plt.imshow(deg_pol, origin ='lower', cmap='hot', norm='symlog')
    # I added this line to show the circle, to make sure that I'm putting it in the right place.
    aper.plot(color='green', lw = 1);
    plt.colorbar()
    #ax.add_patch(circle)
    plt.show()
    """

    return IP_corrected


hdu_list_Q = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step7/2025-03-06-Callas-Q.fits')
#hdu_list_Q.info()
image_Q = hdu_list_Q[0].data
hdu_list_Q.close()

hdu_list_Qint = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step7/2025-03-06-Callas-Q_intensity.fits')
image_Qint = hdu_list_Qint[0].data
hdu_list_Qint.close()

hdu_list_U = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step7/2025-03-06-Callas-U.fits')
image_U = hdu_list_U[0].data
hdu_list_U.close()

hdu_list_Uint = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step7/2025-03-06-Callas-U_intensity.fits')
image_Uint = hdu_list_Uint[0].data
hdu_list_Uint.close()

hdu_list_tot_int = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step7/2025-03-06-Callas-total_intensity.fits')
image_tot_int = hdu_list_tot_int[0].data
hdu_list_tot_int.close()

hdu_list_Pint = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step7/2025-03-06-Callas-polarised_intensity.fits')
pol_int = hdu_list_Pint[0].data
hdu_list_Pint.close()


radii_step = 0.5
inner_radii = np.arange(5, 7+radii_step, radii_step)

for r_in in inner_radii:
    outer_radii = np.arange(r_in+radii_step, 13 + radii_step, radii_step)
    for r_out in outer_radii:
        Q_IP_corrected = inst_pol(image_Q, image_tot_int, Rin=r_in, Rout=r_out)
        U_IP_corrected = inst_pol(image_U, image_tot_int, Rin=r_in, Rout=r_out)

        pol_int_IP_corr = np.sqrt(Q_IP_corrected**2 + U_IP_corrected**2)

        plt.figure(4)
        plt.imshow(pol_int, origin ='lower', cmap='hot',  norm='symlog')
        plt.title("Polarised Intensity with R_out = {0}".format(r_out))
        aper = CircularAnnulus( (c_x, c_y), r_in, r_out)
        aper.plot(color='green', lw = 1);
        plt.colorbar()

        plt.figure(5)
        plt.imshow(pol_int_IP_corr, origin ='lower', cmap='hot',  norm='symlog')
        plt.title("IP Corrected Polarised Intensity with R_out = {0}".format(r_out))
        aper.plot(color='green', lw = 1);
        plt.colorbar()
        #plt.show()

        """
        for i in range(radii.shape[0]):
            Aper = CircularAperture( (c_x, c_y), radii[i])
            plt.figure(4)
            Aper.plot(color='blue', lw = 0.5, alpha=0.5);
            plt.figure(5)
            Aper.plot(color='blue', lw = 0.5, alpha=0.5);

        plt.figure(4)
        plt.imshow(pol_int, origin ='lower', cmap='hot',  norm='symlog')
        plt.title("Polarised Intensity with r_out = {0}".format(r_out))
        aper = CircularAperture( (c_x, c_y), r_out)
        aper.plot(color='green', lw = 1);
        plt.colorbar()

        plt.figure(5)
        plt.imshow(pol_int_IP_corr, origin ='lower', cmap='hot',  norm='symlog')
        plt.title("IP Corrected Polarised Intensity with r_out = {0}".format(r_out))
        aper = CircularAperture( (c_x, c_y), r_out)
        aper.plot(color='green', lw = 1);
        plt.colorbar()
        plt.show()
        """

        hdu = fits.PrimaryHDU(data=Q_IP_corrected)
        hdu.writeto("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step9" + "/{0}-".format(dt.date.today()) + "Callas-" + "Q_IP_corr_Rin={1}_Rout={0}".format(r_out, r_in)  + ".fits", overwrite=True)

        hdu = fits.PrimaryHDU(data=U_IP_corrected)
        hdu.writeto("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step9" + "/{0}-".format(dt.date.today()) + "Callas-" + "U_IP_corr_Rin={1}_Rout={0}".format(r_out, r_in)  + ".fits", overwrite=True)