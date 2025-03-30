<<<<<<< HEAD
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

hdul = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/The Important Ones/2025-03-10-Callas-Q_phi_Rin=6_Rout=7.5.fits")
image_data = hdul[0].data
hdul.close()

"""
flipped_image_data = np.zeros_like(image_data)

for i in range(int(image_data.shape[0]/2)+1):
    flipped_image_data[i,:]     = image_data[-i,:]
    flipped_image_data[-i,:]    = image_data[i,:]
"""
flipped_image_data = np.flipud(image_data)

hdu = fits.PrimaryHDU(data=flipped_image_data)
hdu.writeto("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/inverting_y/GG-Tau_inverted_y.fits", overwrite=True)

plt.figure(1)
plt.title("Original GG-Tau Image flipped")
plt.imshow(image_data,origin ='lower', cmap='cividis', norm ='symlog')
plt.colorbar()
plt.figure(2)
plt.title("GG-Tau Image flipped in Y direction")
plt.imshow(flipped_image_data,origin ='lower', cmap='cividis', norm ='symlog')
plt.colorbar()
plt.show()
=======
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

hdul = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/The Important Ones/2025-03-10-Callas-Q_phi_Rin=6_Rout=7.5.fits")
image_data = hdul[0].data
hdul.close()

"""
flipped_image_data = np.zeros_like(image_data)

for i in range(int(image_data.shape[0]/2)+1):
    flipped_image_data[i,:]     = image_data[-i,:]
    flipped_image_data[-i,:]    = image_data[i,:]
"""
flipped_image_data = np.flipud(image_data)

hdu = fits.PrimaryHDU(data=flipped_image_data)
hdu.writeto("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/inverting_y/GG-Tau_inverted_y.fits", overwrite=True)

plt.figure(1)
plt.title("Original GG-Tau Image flipped")
plt.imshow(image_data,origin ='lower', cmap='cividis', norm ='symlog')
plt.colorbar()
plt.figure(2)
plt.title("GG-Tau Image flipped in Y direction")
plt.imshow(flipped_image_data,origin ='lower', cmap='cividis', norm ='symlog')
plt.colorbar()
plt.show()
>>>>>>> origin
