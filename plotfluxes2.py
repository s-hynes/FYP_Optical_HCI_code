<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np



wavelengths = np.array( [0.6459, 1.043, 1.625, 2.182])
inner_disk_flux_ratios = np.array( [0.00049999621, 0.00129735670, 0.00078994859, 0.00038472376])
outer_disk_flux_ratios = np.array( [0.0016442326, 0.0047801690, 0.0041092948, 0.0028910874])
inner_disk_stdev = np.array([0.000000000000812270, 0.000000811254000000, 0.000000587836000000, 0.000000292179000000])
outer_disk_stdev = np.array([0.0000007470520, 0.0000000693727, 0.0000000546424, 0.0000000399322])

inner_disk_pixels = 1367
outer_disk_pixels = 35671

#inner_disk_error = inner_disk_pixels * np.sqrt(inner_disk_stdev)
inner_disk_error = np.array([3.003202873290950E-11, 2.999446420240530E-05, 2.173403873371980E-05, 1.080272338403830E-05])
outer_disk_error = np.array([1.410939769944220E-04, 1.310226080358650E-05, 1.032018323827520E-05, 7.541901913302750E-06])
#outer_disk_error = outer_disk_pixels * np.sqrt(outer_disk_stdev)

plt.semilogy( wavelengths, inner_disk_flux_ratios, 'bo', label="Inner Disk")
plt.semilogy( wavelengths, outer_disk_flux_ratios, 'ro', label="Outer Disk")
plt.errorbar(wavelengths, inner_disk_flux_ratios, yerr=inner_disk_error, fmt='none', color='b', capsize=5)
plt.errorbar(wavelengths, outer_disk_flux_ratios, yerr=outer_disk_error, fmt='none', color='r', capsize=5)
plt.grid()
plt.xlabel("Wavelength (μm)", fontsize=16)
plt.ylabel("Disk Polarized Flux/Total Flux", fontsize=16)
plt.title("(Disk Polarized Flux/Total Flux) Versus Wavelength", fontsize=16)
plt.ylim(top=2e-2)
plt.xlim(0.5, 4)
plt.legend(fontsize=16)
plt.show()



=======
import matplotlib.pyplot as plt
import numpy as np



wavelengths = np.array( [0.6459, 1.043, 1.625, 2.182])
inner_disk_flux_ratios = np.array( [0.00049999621, 0.00129735670, 0.00078994859, 0.00038472376])
outer_disk_flux_ratios = np.array( [0.0016442326, 0.0047801690, 0.0041092948, 0.0028910874])
inner_disk_stdev = np.array([0.000000000000812270, 0.000000811254000000, 0.000000587836000000, 0.000000292179000000])
outer_disk_stdev = np.array([0.0000007470520, 0.0000000693727, 0.0000000546424, 0.0000000399322])

inner_disk_pixels = 1367
outer_disk_pixels = 35671

#inner_disk_error = inner_disk_pixels * np.sqrt(inner_disk_stdev)
inner_disk_error = np.array([3.003202873290950E-11, 2.999446420240530E-05, 2.173403873371980E-05, 1.080272338403830E-05])
outer_disk_error = np.array([1.410939769944220E-04, 1.310226080358650E-05, 1.032018323827520E-05, 7.541901913302750E-06])
#outer_disk_error = outer_disk_pixels * np.sqrt(outer_disk_stdev)

plt.semilogy( wavelengths, inner_disk_flux_ratios, 'bo', label="Inner Disk")
plt.semilogy( wavelengths, outer_disk_flux_ratios, 'ro', label="Outer Disk")
plt.errorbar(wavelengths, inner_disk_flux_ratios, yerr=inner_disk_error, fmt='none', color='b', capsize=5)
plt.errorbar(wavelengths, outer_disk_flux_ratios, yerr=outer_disk_error, fmt='none', color='r', capsize=5)
plt.grid()
plt.xlabel("Wavelength (μm)", fontsize=16)
plt.ylabel("Disk Polarized Flux/Total Flux", fontsize=16)
plt.title("(Disk Polarized Flux/Total Flux) Versus Wavelength", fontsize=16)
plt.ylim(top=2e-2)
plt.xlim(0.5, 4)
plt.legend(fontsize=16)
plt.show()



>>>>>>> origin
