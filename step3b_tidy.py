<<<<<<< HEAD
"""
Created on Thu Feb 13 17:38:41 2025

@author: Cjmul
"""
from step1 import overscan, double_phase_mode
from step3 import splice_rows
from astropy.io import fits
import numpy as np
import datetime as dt
import os
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
import scipy

def centre_star(image):

    m = image.shape[0]
    centred_star = np.zeros_like(image)

    for i in range(m):
        # Cuts out the point source from the data
        ps = image[i,:,206:-306]

        # Finds the max value of array that contains the point source
        maxval = np.array(ps).ravel()[np.argmax(ps)]

        # Finds the coordinates of this max value
        coords = np.unravel_index(np.argmax(ps), shape = np.array(ps).shape)

        # Defines Levenberg-Marquardt least squares fit
        fitter = fitting.LevMarLSQFitter()

        # Applies fitter
        y_shape = np.shape(ps)[1]
        x_shape = np.shape(ps)[0]
        y,x = np.mgrid[:y_shape,:x_shape]
        z = ps
        p_init = models.Gaussian2D(amplitude =maxval, x_mean=coords[1], y_mean=coords[0], x_stddev=4, y_stddev=4, theta=None)
        p = fitter(p_init, x, y, z)

        # prints values of location of most intensity
        #print("x-mean =", p.x_mean[0])
        #print("y-mean =", p.y_mean[0])

        # Shows the new Gaussian distributed image
        #plt.imshow(p(x, y), origin='lower', interpolation='nearest',  vmin = None, vmax =None)
        #plt.colorbar()
        #plt.show()

        # Using location of most intensity in Gaussian fit to centre star.
        x_shift = 511.5 - (p.x_mean[0] + 206)
        y_shift = 255.5 - p.y_mean[0]
        centred_star[i,:,:] = scipy.ndimage.shift(image[i,:,:], [y_shift, x_shift])

        #plt.imshow(centred_star,origin ='lower', cmap='hot', norm ='symlog')
        #plt.colorbar()
        #plt.plot(511.5, 255.5, 'bo')
        #plt.grid()
        #plt.show()
    
    return centred_star

# The centering of the star seems to take ages for some reason. Update 06/03/2025: I think it takes ages because with the current setup,
# it centres 8x120=960 images for the test data set.

if __name__ == '__main__':
    
    dir_in_str = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/ESO-test-data"
    saving_dir = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step7/fixing-butterfly"
    
    k = 0
    for file in os.listdir(dir_in_str):
        filename = os.fsdecode(file)
        if filename.endswith(".fits"):
            hdul = fits.open( dir_in_str + "/" + filename)
            hdul.close()

            zero    = double_phase_mode(dir_in_str + "/" + filename , "Callas")[0]
            pi      = double_phase_mode(dir_in_str + "/" + filename , "Callas")[1]
            zero_no_overscan = overscan(zero)
            pi_no_overscan   = overscan(pi)

            ord_0 = splice_rows(zero_no_overscan, phase="0")[0]
            ext_0 = splice_rows(zero_no_overscan, phase="0")[1]
            ord_pi = splice_rows(pi_no_overscan, phase="pi")[0]
            ext_pi = splice_rows(pi_no_overscan, phase="pi")[1]

            k += int(1)
            print("\nProcessing up to centering of star done for image {0}.".format(k))

            ord_0_centred   = centre_star(ord_0)
            ext_0_centred   = centre_star(ext_0)
            ord_pi_centred  = centre_star(ord_pi)
            ext_pi_centred  = centre_star(ext_pi)

            print("\nCentering of star done for image {0}.".format(k))

            """
            ord_0_centred   = centre_star(ord_0)
            print("Ordinary 0 centred for image {0}.".format(k))
            ext_0_centred   = centre_star(ext_0)
            print("Extraordinary 0 centred for image {0}.".format(k))
            ord_pi_centred  = centre_star(ord_pi)
            print("Ordinary pi centred for image {0}.".format(k))
            ext_pi_centred  = centre_star(ext_pi)
            print("Extraordinary pi centred for image {0}.".format(k))
            print("Shapes: ",ord_0_centred.shape,ext_0_centred.shape,ord_pi_centred.shape,ext_pi_centred.shape)
=======
"""
Created on Thu Feb 13 17:38:41 2025

@author: Cjmul
"""
from step1 import overscan, double_phase_mode
from step3 import splice_rows
from astropy.io import fits
import numpy as np
import datetime as dt
import os
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
import scipy

def centre_star(image):

    m = image.shape[0]
    centred_star = np.zeros_like(image)

    for i in range(m):
        # Cuts out the point source from the data
        ps = image[i,:,206:-306]

        # Finds the max value of array that contains the point source
        maxval = np.array(ps).ravel()[np.argmax(ps)]

        # Finds the coordinates of this max value
        coords = np.unravel_index(np.argmax(ps), shape = np.array(ps).shape)

        # Defines Levenberg-Marquardt least squares fit
        fitter = fitting.LevMarLSQFitter()

        # Applies fitter
        y_shape = np.shape(ps)[1]
        x_shape = np.shape(ps)[0]
        y,x = np.mgrid[:y_shape,:x_shape]
        z = ps
        p_init = models.Gaussian2D(amplitude =maxval, x_mean=coords[1], y_mean=coords[0], x_stddev=4, y_stddev=4, theta=None)
        p = fitter(p_init, x, y, z)

        # prints values of location of most intensity
        #print("x-mean =", p.x_mean[0])
        #print("y-mean =", p.y_mean[0])

        # Shows the new Gaussian distributed image
        #plt.imshow(p(x, y), origin='lower', interpolation='nearest',  vmin = None, vmax =None)
        #plt.colorbar()
        #plt.show()

        # Using location of most intensity in Gaussian fit to centre star.
        x_shift = 511.5 - (p.x_mean[0] + 206)
        y_shift = 255.5 - p.y_mean[0]
        centred_star[i,:,:] = scipy.ndimage.shift(image[i,:,:], [y_shift, x_shift])

        #plt.imshow(centred_star,origin ='lower', cmap='hot', norm ='symlog')
        #plt.colorbar()
        #plt.plot(511.5, 255.5, 'bo')
        #plt.grid()
        #plt.show()
    
    return centred_star

# The centering of the star seems to take ages for some reason. Update 06/03/2025: I think it takes ages because with the current setup,
# it centres 8x120=960 images for the test data set.

if __name__ == '__main__':
    
    dir_in_str = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/ESO-test-data"
    saving_dir = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step7/fixing-butterfly"
    
    k = 0
    for file in os.listdir(dir_in_str):
        filename = os.fsdecode(file)
        if filename.endswith(".fits"):
            hdul = fits.open( dir_in_str + "/" + filename)
            hdul.close()

            zero    = double_phase_mode(dir_in_str + "/" + filename , "Callas")[0]
            pi      = double_phase_mode(dir_in_str + "/" + filename , "Callas")[1]
            zero_no_overscan = overscan(zero)
            pi_no_overscan   = overscan(pi)

            ord_0 = splice_rows(zero_no_overscan, phase="0")[0]
            ext_0 = splice_rows(zero_no_overscan, phase="0")[1]
            ord_pi = splice_rows(pi_no_overscan, phase="pi")[0]
            ext_pi = splice_rows(pi_no_overscan, phase="pi")[1]

            k += int(1)
            print("\nProcessing up to centering of star done for image {0}.".format(k))

            ord_0_centred   = centre_star(ord_0)
            ext_0_centred   = centre_star(ext_0)
            ord_pi_centred  = centre_star(ord_pi)
            ext_pi_centred  = centre_star(ext_pi)

            print("\nCentering of star done for image {0}.".format(k))

            """
            ord_0_centred   = centre_star(ord_0)
            print("Ordinary 0 centred for image {0}.".format(k))
            ext_0_centred   = centre_star(ext_0)
            print("Extraordinary 0 centred for image {0}.".format(k))
            ord_pi_centred  = centre_star(ord_pi)
            print("Ordinary pi centred for image {0}.".format(k))
            ext_pi_centred  = centre_star(ext_pi)
            print("Extraordinary pi centred for image {0}.".format(k))
            print("Shapes: ",ord_0_centred.shape,ext_0_centred.shape,ord_pi_centred.shape,ext_pi_centred.shape)
>>>>>>> origin
            print(100*"-")"""