<<<<<<< HEAD
from step1 import overscan, double_phase_mode
from step3 import splice_rows
from astropy.io import fits
import numpy as np
import datetime as dt
import os

number = '4_00_16.456'
#number = '4_01_13.284'
directory = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/ESO-test-data"
file = str('ESO-test-data/SPHER.2016-03-31T0{0}.fits'.format(number))

dir_in_str = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/ESO-test-data"
saving_dir = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step7/fixing-butterfly"

zero    = double_phase_mode(dir_in_str + "/" + file, "Callas")[0]
pi      = double_phase_mode(dir_in_str + "/" + file, "Callas")[1]

zero_no_overscan = overscan(zero)
pi_no_overscan   = overscan(pi)

ord_0 = splice_rows(zero_no_overscan, phase="0")[0]
ext_0 = splice_rows(zero_no_overscan, phase="0")[1]


ord_pi = splice_rows(pi_no_overscan, phase="pi")[0]
ext_pi = splice_rows(pi_no_overscan, phase="pi")[1]


hdu = fits.PrimaryHDU(data=ord_0)
hdu.writeto('manipulated-data/step3/{0}-'.format(dt.date.today()) + file + 'zero_ord.fits', overwrite=True)
hdu = fits.PrimaryHDU(data=ext_0)
hdu.writeto('manipulated-data/step3/{0}-'.format(dt.date.today()) + file + 'zero_ext.fits', overwrite=True)

=======
from step1 import overscan, double_phase_mode
from step3 import splice_rows
from astropy.io import fits
import numpy as np
import datetime as dt
import os

number = '4_00_16.456'
#number = '4_01_13.284'
directory = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/ESO-test-data"
file = str('ESO-test-data/SPHER.2016-03-31T0{0}.fits'.format(number))

dir_in_str = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/ESO-test-data"
saving_dir = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step7/fixing-butterfly"

zero    = double_phase_mode(dir_in_str + "/" + file, "Callas")[0]
pi      = double_phase_mode(dir_in_str + "/" + file, "Callas")[1]

zero_no_overscan = overscan(zero)
pi_no_overscan   = overscan(pi)

ord_0 = splice_rows(zero_no_overscan, phase="0")[0]
ext_0 = splice_rows(zero_no_overscan, phase="0")[1]


ord_pi = splice_rows(pi_no_overscan, phase="pi")[0]
ext_pi = splice_rows(pi_no_overscan, phase="pi")[1]


hdu = fits.PrimaryHDU(data=ord_0)
hdu.writeto('manipulated-data/step3/{0}-'.format(dt.date.today()) + file + 'zero_ord.fits', overwrite=True)
hdu = fits.PrimaryHDU(data=ext_0)
hdu.writeto('manipulated-data/step3/{0}-'.format(dt.date.today()) + file + 'zero_ext.fits', overwrite=True)

>>>>>>> origin
