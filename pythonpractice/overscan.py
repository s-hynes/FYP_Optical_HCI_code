<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt

lhs = np.full((1024, 512), 33.5)
rhs = np.full((1024, 512), 33.5)

lh_prescan  = np.zeros((1024,25))
lh_overscan = np.zeros((1024,41))
rh_overscan = np.zeros((1024,41))
rh_prescan  = np.zeros((1024,25))

for i in range(lhs.shape[0]):
    # The mean of these two rows will be (67/2 = 33.5)
    lh_prescan[i, :]    = np.arange(1, 26)
    lh_overscan[i, :]   = np.arange(26, 67)

    # The mean of these two rows will be (67/2 = 33.5)
    rh_overscan[i,:] = np.arange(1,42)
    rh_prescan[i,:]  = np.arange(42, 67)


img = np.append(lh_prescan, lhs, axis=1)
img = np.append(img, lh_overscan, axis=1)
img = np.append(img, rh_overscan, axis=1)
img = np.append(img, rhs, axis=1)
img = np.append(img, rh_prescan, axis=1).reshape(1,1024,1156)

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

    # Is this bias correction correct?
    # Should it not be averaging an entire row of the left hand and right hand overscan areas,
    # then subtracting this from the same row of the left hand and right hand sides of the image,
    # respectively?

    # This is averaging the rows. The array `lh` has dimension 3, so `lh[i,j]` is an array of dimension 1,
    # i.e. one row of the image.
    for i in range(M):
        for j in range(N):
            lh_avg = (np.average(lh[i,j]))
            rh_avg = (np.average(rh[i,j]))
            image_lhs[i,j] -= lh_avg
            image_rhs[i,j] -= rh_avg
    
    fin_img = np.append(image_lhs, image_rhs, axis=2)

    return fin_img

overscan(img)

plt.figure(1)
plt.imshow(img[0,:,:],origin ='lower', cmap='hot')
plt.colorbar()

plt.figure(2)
plt.imshow(overscan(img)[0,:,:],origin ='lower', cmap='hot')
plt.colorbar()
plt.show()

=======
import numpy as np
import matplotlib.pyplot as plt

lhs = np.full((1024, 512), 33.5)
rhs = np.full((1024, 512), 33.5)

lh_prescan  = np.zeros((1024,25))
lh_overscan = np.zeros((1024,41))
rh_overscan = np.zeros((1024,41))
rh_prescan  = np.zeros((1024,25))

for i in range(lhs.shape[0]):
    # The mean of these two rows will be (67/2 = 33.5)
    lh_prescan[i, :]    = np.arange(1, 26)
    lh_overscan[i, :]   = np.arange(26, 67)

    # The mean of these two rows will be (67/2 = 33.5)
    rh_overscan[i,:] = np.arange(1,42)
    rh_prescan[i,:]  = np.arange(42, 67)


img = np.append(lh_prescan, lhs, axis=1)
img = np.append(img, lh_overscan, axis=1)
img = np.append(img, rh_overscan, axis=1)
img = np.append(img, rhs, axis=1)
img = np.append(img, rh_prescan, axis=1).reshape(1,1024,1156)

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

    # Is this bias correction correct?
    # Should it not be averaging an entire row of the left hand and right hand overscan areas,
    # then subtracting this from the same row of the left hand and right hand sides of the image,
    # respectively?

    # This is averaging the rows. The array `lh` has dimension 3, so `lh[i,j]` is an array of dimension 1,
    # i.e. one row of the image.
    for i in range(M):
        for j in range(N):
            lh_avg = (np.average(lh[i,j]))
            rh_avg = (np.average(rh[i,j]))
            image_lhs[i,j] -= lh_avg
            image_rhs[i,j] -= rh_avg
    
    fin_img = np.append(image_lhs, image_rhs, axis=2)

    return fin_img

overscan(img)

plt.figure(1)
plt.imshow(img[0,:,:],origin ='lower', cmap='hot')
plt.colorbar()

plt.figure(2)
plt.imshow(overscan(img)[0,:,:],origin ='lower', cmap='hot')
plt.colorbar()
plt.show()

>>>>>>> origin
