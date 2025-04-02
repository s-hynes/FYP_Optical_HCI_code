import numpy as np
from astropy.io import fits
import datetime as dt

hdu_list_Q = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step7/2025-03-06-Callas-Q.fits')
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

deg_pol_Q = image_Q / image_Qint

hdu = fits.PrimaryHDU(data=deg_pol_Q)
hdu.writeto("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step9" + "/" + "{0}-".format(dt.date.today()) + "Callas-" + "degree_of_polarisation_Q"  + ".fits", overwrite=True)

deg_pol_U = image_U / image_Uint

hdu = fits.PrimaryHDU(data=deg_pol_U)
hdu.writeto("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step9" + "/" + "{0}-".format(dt.date.today()) + "Callas-" + "degree_of_polarisation_U"  + ".fits", overwrite=True)