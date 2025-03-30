<<<<<<< HEAD
from step1 import overscan, double_phase_mode
from step3 import splice_rows
from step4 import single_diff_pol, intensity
from step5 import dedither
from step6 import binning
from astropy.io import fits
import numpy as np
import datetime as dt

number = '4_00_16.456'
#number = '4_01_13.284'
file = str('ESO-test-data/SPHER.2016-03-31T0{0}.fits'.format(number))
    

zero    = double_phase_mode(file)[0]
pi      = double_phase_mode(file)[1]

#ord_0 = splice_rows(overscan(zero), phase="cow")[0]
#assert(0)

ord_0 = splice_rows(overscan(zero), phase="0")[0]
ext_0 = splice_rows(overscan(zero), phase="0")[1]

ord_pi = splice_rows(overscan(pi), phase="pi")[0]
ext_pi = splice_rows(overscan(pi), phase="pi")[1]

thing1 = single_diff_pol(ord_0, ord_pi, ext_0, ext_pi)
thing2 = intensity(ord_0, ord_pi, ext_0, ext_pi)

"""
hdu1 = fits.PrimaryHDU(data=thing1)
hdu1.writeto('manipulated-data/step4/SPHER.2016-03-31T0{0}--{1}-singdiff_test.fits'.format(number, dt.date.today()), overwrite=True)
hdu2 = fits.PrimaryHDU(data=thing2)
hdu2.writeto('manipulated-data/step4/SPHER.2016-03-31T0{0}--{1}-intensity.fits'.format(number, dt.date.today()), overwrite=True)
"""

#print(thing1.shape)

thing3 = dedither(thing1, file)
thing4 = dedither(thing2, file)
"""
hdu1 = fits.PrimaryHDU(data=thing3)
hdu1.writeto('manipulated-data/step5/SPHER.2016-03-31T0{0}--{1}.fits'.format(number, dt.date.today()), overwrite=True)
"""
thing5 = binning(thing3)
thing6 = binning(thing4)

hdu1 = fits.PrimaryHDU(data=thing5)
hdu1.writeto('manipulated-data/step6/SPHER.2016-03-31T0{0}--{1}-sing_diff_square_no_dither.fits'.format(number, dt.date.today()), overwrite=True)
hdu2 = fits.PrimaryHDU(data=thing6)
hdu2.writeto('manipulated-data/step6/SPHER.2016-03-31T0{0}--{1}-intensity_square_no_dither.fits'.format(number, dt.date.today()), overwrite=True)



"""I put these lines in to output the fits files after I had spliced apart the individual polarisation
directions, to see if they made any sense."""

"""
hdu1 = fits.PrimaryHDU(data=ord_0)
hdu1.writeto('manipulated-data/step3/SPHER.2016-03-31T0{0}--{1}-0-ord.fits'.format(number, dt.date.today()), overwrite=True)
hdu2 = fits.PrimaryHDU(data=ext_0)
hdu2.writeto('manipulated-data/step3/SPHER.2016-03-31T0{0}--{1}-0-ext.fits'.format(number, dt.date.today()), overwrite=True)

hdu3 = fits.PrimaryHDU(data=ord_pi)
hdu3.writeto('manipulated-data/step3/SPHER.2016-03-31T0{0}--{1}-pi-ord.fits'.format(number, dt.date.today()), overwrite=True)
hdu4 = fits.PrimaryHDU(data=ext_pi)
hdu4.writeto('manipulated-data/step3/SPHER.2016-03-31T0{0}--{1}-pi-ext.fits'.format(number, dt.date.today()), overwrite=True)
"""
=======
from step1 import overscan, double_phase_mode
from step3 import splice_rows
from step4 import single_diff_pol, intensity
from step5 import dedither
from step6 import binning
from astropy.io import fits
import numpy as np
import datetime as dt

number = '4_00_16.456'
#number = '4_01_13.284'
file = str('ESO-test-data/SPHER.2016-03-31T0{0}.fits'.format(number))
    

zero    = double_phase_mode(file)[0]
pi      = double_phase_mode(file)[1]

#ord_0 = splice_rows(overscan(zero), phase="cow")[0]
#assert(0)

ord_0 = splice_rows(overscan(zero), phase="0")[0]
ext_0 = splice_rows(overscan(zero), phase="0")[1]

ord_pi = splice_rows(overscan(pi), phase="pi")[0]
ext_pi = splice_rows(overscan(pi), phase="pi")[1]

thing1 = single_diff_pol(ord_0, ord_pi, ext_0, ext_pi)
thing2 = intensity(ord_0, ord_pi, ext_0, ext_pi)

"""
hdu1 = fits.PrimaryHDU(data=thing1)
hdu1.writeto('manipulated-data/step4/SPHER.2016-03-31T0{0}--{1}-singdiff_test.fits'.format(number, dt.date.today()), overwrite=True)
hdu2 = fits.PrimaryHDU(data=thing2)
hdu2.writeto('manipulated-data/step4/SPHER.2016-03-31T0{0}--{1}-intensity.fits'.format(number, dt.date.today()), overwrite=True)
"""

#print(thing1.shape)

thing3 = dedither(thing1, file)
thing4 = dedither(thing2, file)
"""
hdu1 = fits.PrimaryHDU(data=thing3)
hdu1.writeto('manipulated-data/step5/SPHER.2016-03-31T0{0}--{1}.fits'.format(number, dt.date.today()), overwrite=True)
"""
thing5 = binning(thing3)
thing6 = binning(thing4)

hdu1 = fits.PrimaryHDU(data=thing5)
hdu1.writeto('manipulated-data/step6/SPHER.2016-03-31T0{0}--{1}-sing_diff_square_no_dither.fits'.format(number, dt.date.today()), overwrite=True)
hdu2 = fits.PrimaryHDU(data=thing6)
hdu2.writeto('manipulated-data/step6/SPHER.2016-03-31T0{0}--{1}-intensity_square_no_dither.fits'.format(number, dt.date.today()), overwrite=True)



"""I put these lines in to output the fits files after I had spliced apart the individual polarisation
directions, to see if they made any sense."""

"""
hdu1 = fits.PrimaryHDU(data=ord_0)
hdu1.writeto('manipulated-data/step3/SPHER.2016-03-31T0{0}--{1}-0-ord.fits'.format(number, dt.date.today()), overwrite=True)
hdu2 = fits.PrimaryHDU(data=ext_0)
hdu2.writeto('manipulated-data/step3/SPHER.2016-03-31T0{0}--{1}-0-ext.fits'.format(number, dt.date.today()), overwrite=True)

hdu3 = fits.PrimaryHDU(data=ord_pi)
hdu3.writeto('manipulated-data/step3/SPHER.2016-03-31T0{0}--{1}-pi-ord.fits'.format(number, dt.date.today()), overwrite=True)
hdu4 = fits.PrimaryHDU(data=ext_pi)
hdu4.writeto('manipulated-data/step3/SPHER.2016-03-31T0{0}--{1}-pi-ext.fits'.format(number, dt.date.today()), overwrite=True)
"""
>>>>>>> origin
