<<<<<<< HEAD
"""This module contains step 1, splitting the raw data cube into the two components of the double phase mode,
and step 2, subtracting the prescan and overscan areas and performing bias correction."""
from astropy.io import fits
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

### Step 1

def double_phase_mode(filename, detector:str):
    """This function splits the images from a .fits data cube into 0 and pi phase mode cubes.
    
    It returns a tuple where the 1st element is the 0 data cube and the 2nd is the pi data cube
    
    ## **Input parameters:**

    **`filename`**: Name of the .fits file to be split.
    
    **`detector`**: Name of the detector that the images are taken from.
    
    ## **Outputs:**
    
    **0 -`image_data_0`**: Data from the file that was recorded in the zero phase mode
    
    **1 -`image_data_pi`**: Data from the file that was recorded in the pi phase mode"""

    # hdu stands for Header Data Unit
    # hdul stands for Header Data Unit List
    hdul = fits.open(filename)

    if detector=="Callas":
        image_data = hdul[1].data
    elif detector=="Bartoli":
        image_data = hdul[2].data
    else:
        raise Exception("Invalid detector entered. Detector must be \"Callas\" or \"Bartoli\".")

    hdul.close()
    image_data_0    = image_data[::2,  :, :]
    image_data_pi   = image_data[1::2, :, :]

    return image_data_0, image_data_pi

### Step 2

def overscan(image):
    """Removes the prescan and overscan area from the images. 

    Subtracts the average value of the pixels in the lefthand prescan and overscan area from the left 
    side of the image, subtracts the average value of the pixels in the righthand prescan and overscan 
    area from the right side of the image. 
    
    Sticks the left hand and right hand side of the image back together.
    
    **Input:**
    
    `image`: The image that the overscan area is to be subtracted from
    
    **Output:**
    
    `fin_img`: The resulting image with the prescan and overscan areas subtracted"""

    image = np.array(image)
    M = image.shape[0]
    N = image.shape[1]

    lh_prescan  = image[:,:, 0:25]
    lh_overscan = image[:,:, 537:578]
    rh_overscan = image[:,:, 578:619]
    rh_prescan  = image[:,:, -25:]

    lh = np.append(lh_prescan, lh_overscan, axis=2)
    rh = np.append(rh_prescan, rh_overscan, axis=2)

    image_lhs = image[:,:, 25:537].astype('float64')
    image_rhs = image[:,:, 619:-25].astype('float64')

    for i in range(M):
        for j in range(N):
            lh_avg = (np.average(lh[i,j]))
            rh_avg = (np.average(rh[i,j]))
            image_lhs[i,j] -= lh_avg
            image_rhs[i,j] -= rh_avg
    
    fin_img = np.append(image_lhs, image_rhs, axis=2)

    return fin_img

"""
file = "SPHER.2016-03-31T02_34_12.814"
yoke = overscan(double_phase_mode("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/ESO-test-data/SPHER.2016-03-31T02_34_12.814.fits", "Callas"))

hdu = fits.PrimaryHDU(data=yoke)
hdu.writeto('manipulated-data/steps2ndreader/{0}-'.format(dt.date.today()) + file +'-01-zero_no_overscan.fits', overwrite=True)
"""

if __name__ == "__main__":
    #print("step1.py is being run directly in the interpreter.")
    lhs = np.full((1024, 512), 33.5+35)
    rhs = np.full((1024, 512), 99.5+35)

    lh_prescan  = np.zeros((1024,25))
    lh_overscan = np.zeros((1024,41))
    rh_overscan = np.zeros((1024,41))
    rh_prescan  = np.zeros((1024,25))

    for i in range(lhs.shape[0]):
        # The mean of these two rows will be 67/2 = 33.5
        lh_prescan[i, :]    = np.arange(1, 26)
        lh_overscan[i, :]   = np.arange(26, 67)

        # The mean of these two rows will be  (132+67)/2 = 99.5
        rh_overscan[i,:] = np.arange(67,108)
        rh_prescan[i,:]  = np.arange(108, 133)

    img = np.append(lh_prescan, lhs, axis=1)
    img = np.append(img, lh_overscan, axis=1)
    img = np.append(img, rh_overscan, axis=1)
    img = np.append(img, rhs, axis=1)
    img = np.append(img, rh_prescan, axis=1).reshape(1,1024,1156)

    """
    lhs = np.full((1024, 512), 14)
    rhs = np.full((1024, 512), 16)

    lh_prescan  = np.zeros((1024,25))
    lh_overscan = np.zeros((1024,41))
    rh_overscan = np.zeros((1024,41))
    rh_prescan  = np.zeros((1024,25))

    for i in range(lhs.shape[0]):
        lh_prescan[i, :]    = np.full(lh_prescan.shape[1], 10)
        lh_overscan[i, :]   = np.full(lh_overscan.shape[1], 10)

        rh_overscan[i,:] = np.full(rh_overscan.shape[1], 12)
        rh_prescan[i,:]  = np.full(rh_prescan.shape[1], 12)

    img = np.append(lh_prescan, lhs, axis=1)
    img = np.append(img, lh_overscan, axis=1)
    img = np.append(img, rh_overscan, axis=1)
    img = np.append(img, rhs, axis=1)
    img = np.append(img, rh_prescan, axis=1).reshape(1,1024,1156)
    """

    #overscan(img)

    plt.figure(1)
    plt.title("Example \"Toy\" Image Before Overscan\n Removal and Bias Subtraction.")
    plt.imshow(img[0,:,:],origin ='lower', cmap='plasma')
    plt.colorbar()

    plt.figure(2)
    plt.title("Example \"Toy\" Image After Overscan\n Removal and Bias Subtraction.")
    plt.imshow(overscan(img)[0,:,:],origin ='lower', cmap='plasma')
    plt.colorbar()
=======
"""This module contains step 1, splitting the raw data cube into the two components of the double phase mode,
and step 2, subtracting the prescan and overscan areas and performing bias correction."""
from astropy.io import fits
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

### Step 1

def double_phase_mode(filename, detector:str):
    """This function splits the images from a .fits data cube into 0 and pi phase mode cubes.
    
    It returns a tuple where the 1st element is the 0 data cube and the 2nd is the pi data cube
    
    ## **Input parameters:**

    **`filename`**: Name of the .fits file to be split.
    
    **`detector`**: Name of the detector that the images are taken from.
    
    ## **Outputs:**
    
    **0 -`image_data_0`**: Data from the file that was recorded in the zero phase mode
    
    **1 -`image_data_pi`**: Data from the file that was recorded in the pi phase mode"""

    # hdu stands for Header Data Unit
    # hdul stands for Header Data Unit List
    hdul = fits.open(filename)

    if detector=="Callas":
        image_data = hdul[1].data
    elif detector=="Bartoli":
        image_data = hdul[2].data
    else:
        raise Exception("Invalid detector entered. Detector must be \"Callas\" or \"Bartoli\".")

    hdul.close()
    image_data_0    = image_data[::2,  :, :]
    image_data_pi   = image_data[1::2, :, :]

    return image_data_0, image_data_pi

### Step 2

def overscan(image):
    """Removes the prescan and overscan area from the images. 

    Subtracts the average value of the pixels in the lefthand prescan and overscan area from the left 
    side of the image, subtracts the average value of the pixels in the righthand prescan and overscan 
    area from the right side of the image. 
    
    Sticks the left hand and right hand side of the image back together.
    
    **Input:**
    
    `image`: The image that the overscan area is to be subtracted from
    
    **Output:**
    
    `fin_img`: The resulting image with the prescan and overscan areas subtracted"""

    image = np.array(image)
    M = image.shape[0]
    N = image.shape[1]

    lh_prescan  = image[:,:, 0:25]
    lh_overscan = image[:,:, 537:578]
    rh_overscan = image[:,:, 578:619]
    rh_prescan  = image[:,:, -25:]

    lh = np.append(lh_prescan, lh_overscan, axis=2)
    rh = np.append(rh_prescan, rh_overscan, axis=2)

    image_lhs = image[:,:, 25:537].astype('float64')
    image_rhs = image[:,:, 619:-25].astype('float64')

    for i in range(M):
        for j in range(N):
            lh_avg = (np.average(lh[i,j]))
            rh_avg = (np.average(rh[i,j]))
            image_lhs[i,j] -= lh_avg
            image_rhs[i,j] -= rh_avg
    
    fin_img = np.append(image_lhs, image_rhs, axis=2)

    return fin_img

"""
file = "SPHER.2016-03-31T02_34_12.814"
yoke = overscan(double_phase_mode("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/ESO-test-data/SPHER.2016-03-31T02_34_12.814.fits", "Callas"))

hdu = fits.PrimaryHDU(data=yoke)
hdu.writeto('manipulated-data/steps2ndreader/{0}-'.format(dt.date.today()) + file +'-01-zero_no_overscan.fits', overwrite=True)
"""

if __name__ == "__main__":
    #print("step1.py is being run directly in the interpreter.")
    lhs = np.full((1024, 512), 33.5+35)
    rhs = np.full((1024, 512), 99.5+35)

    lh_prescan  = np.zeros((1024,25))
    lh_overscan = np.zeros((1024,41))
    rh_overscan = np.zeros((1024,41))
    rh_prescan  = np.zeros((1024,25))

    for i in range(lhs.shape[0]):
        # The mean of these two rows will be 67/2 = 33.5
        lh_prescan[i, :]    = np.arange(1, 26)
        lh_overscan[i, :]   = np.arange(26, 67)

        # The mean of these two rows will be  (132+67)/2 = 99.5
        rh_overscan[i,:] = np.arange(67,108)
        rh_prescan[i,:]  = np.arange(108, 133)

    img = np.append(lh_prescan, lhs, axis=1)
    img = np.append(img, lh_overscan, axis=1)
    img = np.append(img, rh_overscan, axis=1)
    img = np.append(img, rhs, axis=1)
    img = np.append(img, rh_prescan, axis=1).reshape(1,1024,1156)

    """
    lhs = np.full((1024, 512), 14)
    rhs = np.full((1024, 512), 16)

    lh_prescan  = np.zeros((1024,25))
    lh_overscan = np.zeros((1024,41))
    rh_overscan = np.zeros((1024,41))
    rh_prescan  = np.zeros((1024,25))

    for i in range(lhs.shape[0]):
        lh_prescan[i, :]    = np.full(lh_prescan.shape[1], 10)
        lh_overscan[i, :]   = np.full(lh_overscan.shape[1], 10)

        rh_overscan[i,:] = np.full(rh_overscan.shape[1], 12)
        rh_prescan[i,:]  = np.full(rh_prescan.shape[1], 12)

    img = np.append(lh_prescan, lhs, axis=1)
    img = np.append(img, lh_overscan, axis=1)
    img = np.append(img, rh_overscan, axis=1)
    img = np.append(img, rhs, axis=1)
    img = np.append(img, rh_prescan, axis=1).reshape(1,1024,1156)
    """

    #overscan(img)

    plt.figure(1)
    plt.title("Example \"Toy\" Image Before Overscan\n Removal and Bias Subtraction.")
    plt.imshow(img[0,:,:],origin ='lower', cmap='plasma')
    plt.colorbar()

    plt.figure(2)
    plt.title("Example \"Toy\" Image After Overscan\n Removal and Bias Subtraction.")
    plt.imshow(overscan(img)[0,:,:],origin ='lower', cmap='plasma')
    plt.colorbar()
>>>>>>> origin
    plt.show()