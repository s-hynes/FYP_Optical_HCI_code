import matplotlib.pyplot as plt
import numpy as np

# Note: Alternatively, you can just use np.flipud() or np.fliplr() to do this.

L = 64

array1 = np.zeros([L,L])

for i in range(array1.shape[0]):
    array1[i, :]    = np.arange(1, L+1) + i

plt.figure(1)
plt.title("Original Image")
plt.imshow(array1,origin ='lower', cmap='cividis')
plt.colorbar()

array2 = np.zeros_like(array1)

# I think this for loop successfully mirrors the image about the x axis.
for i in range(array1.shape[0]):
    array2[i,:] = array1[-i-1,:]

plt.figure(2)
plt.title("Image with y coordinates flipped")
plt.imshow(array2,origin ='lower', cmap='cividis')
plt.colorbar()

array3 = np.zeros_like(array1)

for i in range(array1.shape[1]):
    array3[:,i] = array1[:,-i-1]

plt.figure(3)
plt.title("Image with x coordinates flipped")
plt.imshow(array3,origin ='lower', cmap='cividis')
plt.colorbar()
plt.show()