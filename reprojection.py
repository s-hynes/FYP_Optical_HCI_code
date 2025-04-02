from reproject import reproject_interp
from astropy.io import fits

# Load the images (FITS format)
image1, header1 = fits.getdata("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/GG-Tau/The Important Ones/GGTauA_2016-11-19_I_pol_star_pol_subtr_Hband.fits", header=True)
image2, header2 = fits.getdata("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/GG-Tau-data/SPHER.2024-11-24T03_27_06.147.fits", header=True)

# Reproject image2 to match image1's WCS and pixel scale
reprojected_image, _ = reproject_interp((image1, header1), header2)

# Save the reprojected image
fits.writeto("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/GG-Tau/The Important Ones/GGTauA_2016-11-19_I_pol_star_pol_subtr_Hband_Reprojected.fits", reprojected_image, header1, overwrite=True)
