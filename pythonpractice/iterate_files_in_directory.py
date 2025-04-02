import os
import astropy
from astropy.io import fits

dir_in_str = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/ESO-Test-data"

directory = os.fsdecode(dir_in_str)
print(directory)
#os.listdir(directory)

Qplus   = 0 
Qminus  = 0
Uplus   = 0
Uminus  = 0
something_else = 0

Qplus_cyc   = 0 
Qminus_cyc  = 0
Uplus_cyc  = 0
Uminus_cyc  = 0
n_cycles = 0


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".fits"):
            hdul = fits.open( directory + "/" + filename)
            Stokes = hdul[0].header['HIERARCH ESO OCS3 ZIMPOL POL STOKES']
            #print("\n", hdul[0].header['ESO TEL PARANG END'], hdul[0].header['ESO TEL PARANG START'])
            hdul.close()

            
            if Stokes == "Qplus":
                  Qplus += 1
                  Qplus_cyc += 1
            elif Stokes == "Qminus":
                  Qminus += 1
                  Qminus_cyc += 1
            elif Stokes == "Uplus":
                  Uplus += 1
                  Uplus_cyc += 1
            elif Stokes == "Uminus":
                  Uminus += 1
                  Uminus_cyc += 1
            else:
                something_else +=1

            if (Qplus_cyc!=0 and Qminus_cyc!=0 and Uplus_cyc!=0 and Uminus_cyc!=0) and Stokes == "Qplus":
                  n_cycles += 1
                  if n_cycles != 1:
                        print("\n{0} full polarimetric cycles".format(n_cycles))
                  else:
                        print("\n{0} full polarimetric cycle".format(n_cycles))
                  Qplus_cyc   = 0 
                  Qminus_cyc  = 0
                  Uplus_cyc   = 0
                  Uminus_cyc  = 0


            print("\n", filename, " ", Stokes)

print("""Number of each type in test dataset:\n Qplus = {0}, Qminus = {1}, 
      Uplus = {2}, Uminus = {3}, something else = {4}""".format(Qplus, Qminus, Uplus, Uminus, something_else))
print("\nNumber of polarimetric cycles = ", n_cycles)