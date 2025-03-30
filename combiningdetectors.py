<<<<<<< HEAD
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# So what I want to do here is make a function that flips images from Callas about the X-plane and flips images
# from Bartoli about the Y-plane, then about the X-plane.

def combine2(Callas_image, Bartoli_image):

    Callas_image = Callas_image.reshape(1,512,512)
    Bartoli_image_xflipped = np.fliplr(Bartoli_image).reshape(1,512,512)

    images_combined = np.average( np.append(Callas_image, Bartoli_image_xflipped, axis=0), axis=0)

    return images_combined


if __name__=="__main__":

    Q_phi_Callas    = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/steps_presentation/2025-03-17-Callas-40-Qphi_Rin=6_Rout=7.5.fits")[0].data
    Q_phi_Bartoli   = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/steps_presentation/2025-03-17-Bartoli-40-Qphi_Rin=6_Rout=7.5.fits")[0].data

    combined_image = combine2(Q_phi_Callas, Q_phi_Bartoli)

    plt.figure(1)
    plt.title("Original Callas image")
    plt.imshow(Q_phi_Callas,origin ='lower', cmap='cividis', norm='symlog')
    plt.colorbar()

    plt.figure(2)
    plt.title("Original Bartoli image")
    plt.imshow(Q_phi_Bartoli,origin ='lower', cmap='cividis', norm='symlog')
    plt.colorbar()

    plt.figure(3)
    plt.title("Two images combined")
    plt.imshow(combined_image,origin ='lower', cmap='cividis', norm='symlog')
    plt.colorbar()
    plt.show()

"""
Q_phi_Bartoli_xflipped = np.zeros_like(Q_phi_Bartoli)
# I think this for loop successfully mirrors the image about the y axis.
for i in range(Q_phi_Bartoli.shape[1]):
    Q_phi_Bartoli_xflipped[:,i] = Q_phi_Bartoli[:,-i-1]

# Using this numpy function is probably more efficient though ):
Q_phi_Bartoli_xflipped = np.fliplr(Q_phi_Bartoli)

plt.figure(1)
plt.title("Original Bartolis image")
plt.imshow(Q_phi_Bartoli,origin ='lower', cmap='cividis', norm='symlog')
plt.colorbar()

plt.figure(2)
plt.title("Bartoli image flipped in X-direction")
plt.imshow(Q_phi_Bartoli_xflipped,origin ='lower', cmap='cividis', norm='symlog')
plt.colorbar()

Q_phi_Bartoli_xyflipped = np.flipud(Q_phi_Bartoli_xflipped)

plt.figure(3)
plt.title("Bartoli image flipped in X and Y directions")
plt.imshow(Q_phi_Bartoli_xyflipped,origin ='lower', cmap='cividis', norm='symlog')
plt.colorbar()
#plt.show()
=======
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# So what I want to do here is make a function that flips images from Callas about the X-plane and flips images
# from Bartoli about the Y-plane, then about the X-plane.

def combine2(Callas_image, Bartoli_image):

    Callas_image = Callas_image.reshape(1,512,512)
    Bartoli_image_xflipped = np.fliplr(Bartoli_image).reshape(1,512,512)

    images_combined = np.average( np.append(Callas_image, Bartoli_image_xflipped, axis=0), axis=0)

    return images_combined


if __name__=="__main__":

    Q_phi_Callas    = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/steps_presentation/2025-03-17-Callas-40-Qphi_Rin=6_Rout=7.5.fits")[0].data
    Q_phi_Bartoli   = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/steps_presentation/2025-03-17-Bartoli-40-Qphi_Rin=6_Rout=7.5.fits")[0].data

    combined_image = combine2(Q_phi_Callas, Q_phi_Bartoli)

    plt.figure(1)
    plt.title("Original Callas image")
    plt.imshow(Q_phi_Callas,origin ='lower', cmap='cividis', norm='symlog')
    plt.colorbar()

    plt.figure(2)
    plt.title("Original Bartoli image")
    plt.imshow(Q_phi_Bartoli,origin ='lower', cmap='cividis', norm='symlog')
    plt.colorbar()

    plt.figure(3)
    plt.title("Two images combined")
    plt.imshow(combined_image,origin ='lower', cmap='cividis', norm='symlog')
    plt.colorbar()
    plt.show()

"""
Q_phi_Bartoli_xflipped = np.zeros_like(Q_phi_Bartoli)
# I think this for loop successfully mirrors the image about the y axis.
for i in range(Q_phi_Bartoli.shape[1]):
    Q_phi_Bartoli_xflipped[:,i] = Q_phi_Bartoli[:,-i-1]

# Using this numpy function is probably more efficient though ):
Q_phi_Bartoli_xflipped = np.fliplr(Q_phi_Bartoli)

plt.figure(1)
plt.title("Original Bartolis image")
plt.imshow(Q_phi_Bartoli,origin ='lower', cmap='cividis', norm='symlog')
plt.colorbar()

plt.figure(2)
plt.title("Bartoli image flipped in X-direction")
plt.imshow(Q_phi_Bartoli_xflipped,origin ='lower', cmap='cividis', norm='symlog')
plt.colorbar()

Q_phi_Bartoli_xyflipped = np.flipud(Q_phi_Bartoli_xflipped)

plt.figure(3)
plt.title("Bartoli image flipped in X and Y directions")
plt.imshow(Q_phi_Bartoli_xyflipped,origin ='lower', cmap='cividis', norm='symlog')
plt.colorbar()
#plt.show()
>>>>>>> origin
"""