<<<<<<< HEAD
import numpy as np
from photutils.aperture import ApertureStats, CircularAnnulus
from astropy.io import fits
import datetime as dt

c_x, c_y = 255.75, 255.5

def inst_pol(diff_im, int_im, Rin, Rout):

    deg_pol = diff_im / int_im
    c_x, c_y = 255.75, 255.5

    """
    pixels_in_circle = []

    for i in range(deg_pol.shape[0]):
        for j in range(deg_pol.shape[1]):
            if (i - c_x)**2 + (j - c_y)**2 <= R**2:
                pixels_in_circle.append(deg_pol[i,j])

    median = np.median(pixels_in_circle)

    print("\nMedian using Numpy method = {0}".format(median))
    """

    aper = CircularAnnulus( (c_x, c_y), Rin, Rout)
    aperstats = ApertureStats(deg_pol, aper)
    median = aperstats.median

    IP_corrected = diff_im - median * int_im

    return IP_corrected

def fix(diff_im, Rin, Rout):

    c_x, c_y = 255.75, 255.5

    aper = CircularAnnulus( (c_x, c_y), Rin, Rout)
    aperstats = ApertureStats(diff_im, aper)
    median = aperstats.median

    fixed = diff_im - median

=======
import numpy as np
from photutils.aperture import ApertureStats, CircularAnnulus
from astropy.io import fits
import datetime as dt

c_x, c_y = 255.75, 255.5

def inst_pol(diff_im, int_im, Rin, Rout):

    deg_pol = diff_im / int_im
    c_x, c_y = 255.75, 255.5

    """
    pixels_in_circle = []

    for i in range(deg_pol.shape[0]):
        for j in range(deg_pol.shape[1]):
            if (i - c_x)**2 + (j - c_y)**2 <= R**2:
                pixels_in_circle.append(deg_pol[i,j])

    median = np.median(pixels_in_circle)

    print("\nMedian using Numpy method = {0}".format(median))
    """

    aper = CircularAnnulus( (c_x, c_y), Rin, Rout)
    aperstats = ApertureStats(deg_pol, aper)
    median = aperstats.median

    IP_corrected = diff_im - median * int_im

    return IP_corrected

def fix(diff_im, Rin, Rout):

    c_x, c_y = 255.75, 255.5

    aper = CircularAnnulus( (c_x, c_y), Rin, Rout)
    aperstats = ApertureStats(diff_im, aper)
    median = aperstats.median

    fixed = diff_im - median

>>>>>>> origin
    return fixed