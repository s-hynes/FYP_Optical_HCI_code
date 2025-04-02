#%% -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:38:41 2025

@author: Cjmul
"""
#%% Import ya libraries
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits 
from astropy.modeling import models, fitting

# open the  file
image = fits.open('C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step7/2025-02-23-Callas-total_intensity.fits')

# take data from image
hdu_list_new = image
hdu_list_new.info()
image_data = hdu_list_new[0].data

# close image to save memory
hdu_list_new.close()

#%% this just shows us the image (not necessary)
plt.imshow(image_data,origin ='lower', cmap='hot', norm ='symlog')
plt.colorbar()

plt.show()
#%% prints values from image
print('Min:  ', np.min(image_data))
print('Max:  ', np.max(image_data))
print('Mean: ', np.mean(image_data))
print('Stdev:', np.std(image_data))
#%% shows image with better scale
ADI = plt.imshow(image_data,origin ='lower',  cmap='hot', vmin = np.min(image_data)/255, vmax =np.max(image_data)/255)
plt.colorbar()
plt.show()
#%% cuts out the ps from the data
#ps = image_data[100:400,100:400] # Will this have to be changed for my data? I think so.
ps = image_data

plt.figure()
ps_zoom = plt.imshow(ps,origin ='lower',  cmap='hot', vmin = np.min(image_data)/255, vmax =np.max(image_data)/255)
plt.colorbar()
plt.show()
#%% finds max value of array that contains the ps
maxval = np.array(ps).ravel()[np.argmax(ps)]
print(maxval)
#np.max(ps) is the same thing
#%% finds coords of this max value
print(np.array(ps).shape)
coords = np.unravel_index(np.argmax(ps), shape = np.array(ps).shape)
print(coords)
#%%
plt.figure()
ps_zoom = plt.imshow(ps,origin ='lower',  cmap='hot', vmin = np.min(image_data)/255, vmax =np.max(image_data)/255)
plt.colorbar()
plt.plot(coords[1], coords[0], 'bo', label="Location of max value")
plt.legend()
plt.show()
#%% defines levenberg-marquardt Least squares fit
fitter = fitting.LevMarLSQFitter()

# applies fitter and shows the new gaussian distributed image
y_shape = np.shape(ps)[1]
x_shape = np.shape(ps)[0]
y,x = np.mgrid[:y_shape,:x_shape]
z = ps
p_init = models.Gaussian2D(amplitude =maxval, x_mean=coords[1], y_mean=coords[0], x_stddev=4, y_stddev=4, theta=None)
p = fitter(p_init, x, y, z)
plt.imshow(p(x, y), origin='lower', interpolation='nearest',  vmin = None, vmax =None)
plt.colorbar()
plt.show()

#%% prints values of location of most intensity
print("x-mean =", p.x_mean[0])
print("y-mean =", p.y_mean[0])
