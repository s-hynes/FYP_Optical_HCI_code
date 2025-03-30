<<<<<<< HEAD
import numpy as np
from photutils.aperture import ApertureStats, CircularAnnulus
from astropy.io import fits
import matplotlib.pyplot as plt

c_x, c_y = 255.75, 255.5

def coeff(diff_im, int_im, Rin, Rout):

    deg_pol = diff_im / int_im
    c_x, c_y = 255.75, 255.5

    aper = CircularAnnulus( (c_x, c_y), Rin, Rout)
    aperstats = ApertureStats(deg_pol, aper)
    median = aperstats.median

    return median

hdu_list_Q = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/step7/2025-03-06-Callas-Q.fits')
image_Q = hdu_list_Q[0].data
hdu_list_Q.close()

hdu_list_Qint = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/step7/2025-03-06-Callas-Q_intensity.fits')
image_Qint = hdu_list_Qint[0].data
hdu_list_Qint.close()

hdu_list_U = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/step7/2025-03-06-Callas-U.fits')
image_U = hdu_list_U[0].data
hdu_list_U.close()

hdu_list_Uint = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/step7/2025-03-06-Callas-U_intensity.fits')
image_Uint = hdu_list_Uint[0].data
hdu_list_Uint.close()

hdu_list_tot_int = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/step7/2025-03-06-Callas-total_intensity.fits')
image_tot_int = hdu_list_tot_int[0].data
hdu_list_tot_int.close()

hdu_list_Pint = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/step7/2025-03-06-Callas-polarised_intensity.fits')
pol_int = hdu_list_Pint[0].data
hdu_list_Pint.close()

radii_step = 0.001
inner_radii = np.arange(6, 12+radii_step, radii_step)
r_in = 6

#for r_in in inner_radii:

outer_radii = np.arange(r_in+radii_step, 20 + radii_step, radii_step)
c_Q = np.zeros_like(outer_radii)
c_U = np.zeros_like(outer_radii)
i = 0

for r_out in outer_radii:
    c_Q[i] = coeff(image_Q, image_tot_int, r_in, r_out)
    c_U[i] = coeff(image_U, image_tot_int, r_in, r_out)
    i += 1

outer_radii_milliarcseconds = outer_radii*3.6

#print(c_Q)

vertical_lines_y = np.linspace(-0.003, 0.003, 5)

plt.figure(1)
plt.plot(outer_radii, c_Q, 'bo', label="$c_Q =$ median $Q/I$")
plt.plot(outer_radii, c_U, 'ro', label="$c_U =$ median $U/I$")
#plt.plot(np.full_like(vertical_lines_y, 6), vertical_lines_y, 'k--')
plt.plot(np.full_like(vertical_lines_y, 7.5), vertical_lines_y, 'k--')
plt.text(1.05*7.5, 1e-4, "Annulus outer radius used \nin pipeline = 7.5 pixels", fontsize=16)
plt.ylim(-0.0024, 0.0024)
plt.xlim(np.min(outer_radii), np.max(outer_radii))
plt.legend(fontsize=16)
plt.xlabel("Outer Radius of Annulus [Pixels]", fontsize=16)
plt.ylabel("Median Values $c_Q$ and $c_U$ [Dimensionless]", fontsize=16)
plt.title("Median Values of $Q/I$ and $U/I$ within Annulus\n as a Function of the Outer Radius of the Annulus", fontsize=16)
plt.grid()

inner_rad_milliarcsec = 6*3.6
outer_rad_milliarcsec = 7.5*3.6

plt.figure(2)
plt.plot(outer_radii_milliarcseconds, c_Q, 'bo', label="$c_Q =$ median $Q/I$")
plt.plot(outer_radii_milliarcseconds, c_U, 'ro', label="$c_U =$ median $U/I$")
#plt.plot(np.full_like(vertical_lines_y, inner_rad_milliarcsec), vertical_lines_y, 'k--')
plt.plot(np.full_like(vertical_lines_y, outer_rad_milliarcsec), vertical_lines_y, 'k--')
plt.text(1.05*outer_rad_milliarcsec, 1e-4, "Annulus outer radius used \nin pipeline = 27 mas", fontsize=16)
plt.ylim(-0.0024, 0.0024)
plt.xlim(np.min(outer_radii_milliarcseconds), np.max(outer_radii_milliarcseconds))
plt.legend(fontsize=16)
plt.xlabel("Outer Radius of Annulus [mas]", fontsize=16)
plt.ylabel("Median Values $c_Q$ and $c_U$ [Dimensionless]", fontsize=16)
plt.title("Median Values of $Q/I$ and $U/I$ within Annulus\n as a Function of the Outer Radius of the Annulus", fontsize=16)
plt.grid()
plt.show()
=======
import numpy as np
from photutils.aperture import ApertureStats, CircularAnnulus
from astropy.io import fits
import matplotlib.pyplot as plt

c_x, c_y = 255.75, 255.5

def coeff(diff_im, int_im, Rin, Rout):

    deg_pol = diff_im / int_im
    c_x, c_y = 255.75, 255.5

    aper = CircularAnnulus( (c_x, c_y), Rin, Rout)
    aperstats = ApertureStats(deg_pol, aper)
    median = aperstats.median

    return median

hdu_list_Q = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/step7/2025-03-06-Callas-Q.fits')
image_Q = hdu_list_Q[0].data
hdu_list_Q.close()

hdu_list_Qint = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/step7/2025-03-06-Callas-Q_intensity.fits')
image_Qint = hdu_list_Qint[0].data
hdu_list_Qint.close()

hdu_list_U = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/step7/2025-03-06-Callas-U.fits')
image_U = hdu_list_U[0].data
hdu_list_U.close()

hdu_list_Uint = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/step7/2025-03-06-Callas-U_intensity.fits')
image_Uint = hdu_list_Uint[0].data
hdu_list_Uint.close()

hdu_list_tot_int = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/step7/2025-03-06-Callas-total_intensity.fits')
image_tot_int = hdu_list_tot_int[0].data
hdu_list_tot_int.close()

hdu_list_Pint = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/step7/2025-03-06-Callas-polarised_intensity.fits')
pol_int = hdu_list_Pint[0].data
hdu_list_Pint.close()

radii_step = 0.001
inner_radii = np.arange(6, 12+radii_step, radii_step)
r_in = 6

#for r_in in inner_radii:

outer_radii = np.arange(r_in+radii_step, 20 + radii_step, radii_step)
c_Q = np.zeros_like(outer_radii)
c_U = np.zeros_like(outer_radii)
i = 0

for r_out in outer_radii:
    c_Q[i] = coeff(image_Q, image_tot_int, r_in, r_out)
    c_U[i] = coeff(image_U, image_tot_int, r_in, r_out)
    i += 1

outer_radii_milliarcseconds = outer_radii*3.6

#print(c_Q)

vertical_lines_y = np.linspace(-0.003, 0.003, 5)

plt.figure(1)
plt.plot(outer_radii, c_Q, 'bo', label="$c_Q =$ median $Q/I$")
plt.plot(outer_radii, c_U, 'ro', label="$c_U =$ median $U/I$")
#plt.plot(np.full_like(vertical_lines_y, 6), vertical_lines_y, 'k--')
plt.plot(np.full_like(vertical_lines_y, 7.5), vertical_lines_y, 'k--')
plt.text(1.05*7.5, 1e-4, "Annulus outer radius used \nin pipeline = 7.5 pixels", fontsize=16)
plt.ylim(-0.0024, 0.0024)
plt.xlim(np.min(outer_radii), np.max(outer_radii))
plt.legend(fontsize=16)
plt.xlabel("Outer Radius of Annulus [Pixels]", fontsize=16)
plt.ylabel("Median Values $c_Q$ and $c_U$ [Dimensionless]", fontsize=16)
plt.title("Median Values of $Q/I$ and $U/I$ within Annulus\n as a Function of the Outer Radius of the Annulus", fontsize=16)
plt.grid()

inner_rad_milliarcsec = 6*3.6
outer_rad_milliarcsec = 7.5*3.6

plt.figure(2)
plt.plot(outer_radii_milliarcseconds, c_Q, 'bo', label="$c_Q =$ median $Q/I$")
plt.plot(outer_radii_milliarcseconds, c_U, 'ro', label="$c_U =$ median $U/I$")
#plt.plot(np.full_like(vertical_lines_y, inner_rad_milliarcsec), vertical_lines_y, 'k--')
plt.plot(np.full_like(vertical_lines_y, outer_rad_milliarcsec), vertical_lines_y, 'k--')
plt.text(1.05*outer_rad_milliarcsec, 1e-4, "Annulus outer radius used \nin pipeline = 27 mas", fontsize=16)
plt.ylim(-0.0024, 0.0024)
plt.xlim(np.min(outer_radii_milliarcseconds), np.max(outer_radii_milliarcseconds))
plt.legend(fontsize=16)
plt.xlabel("Outer Radius of Annulus [mas]", fontsize=16)
plt.ylabel("Median Values $c_Q$ and $c_U$ [Dimensionless]", fontsize=16)
plt.title("Median Values of $Q/I$ and $U/I$ within Annulus\n as a Function of the Outer Radius of the Annulus", fontsize=16)
plt.grid()
plt.show()
>>>>>>> origin
