<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np



wavelengths = np.array( [0.6459, 1.043, 1.625, 2.182])
inner_disk_flux_ratios = np.array( [0.000855165209, 0.001117890771, 0.000667488529, 0.000320765865])
outer_disk_flux_ratios = np.array( [0.002417758994, 0.004780168962, 0.004109294819, 0.002891087312])

plt.semilogy( wavelengths, inner_disk_flux_ratios, 'bo', label="Inner Disk")
plt.semilogy( wavelengths, outer_disk_flux_ratios, 'ro', label="Outer Disk")
plt.grid()
plt.xlabel("Wavelength (μm)", fontsize=16)
plt.ylabel("Disk Polarized Flux/Total Flux", fontsize=16)
plt.title("Disk Polarized Flux/Total Flux Versus Wavelength", fontsize=16)
plt.ylim(top=1e-2)
plt.xlim(0.5, 4)
plt.legend(fontsize=16)
plt.show()



=======
import matplotlib.pyplot as plt
import numpy as np



wavelengths = np.array( [0.6459, 1.043, 1.625, 2.182])
inner_disk_flux_ratios = np.array( [0.000855165209, 0.001117890771, 0.000667488529, 0.000320765865])
outer_disk_flux_ratios = np.array( [0.002417758994, 0.004780168962, 0.004109294819, 0.002891087312])

plt.semilogy( wavelengths, inner_disk_flux_ratios, 'bo', label="Inner Disk")
plt.semilogy( wavelengths, outer_disk_flux_ratios, 'ro', label="Outer Disk")
plt.grid()
plt.xlabel("Wavelength (μm)", fontsize=16)
plt.ylabel("Disk Polarized Flux/Total Flux", fontsize=16)
plt.title("Disk Polarized Flux/Total Flux Versus Wavelength", fontsize=16)
plt.ylim(top=1e-2)
plt.xlim(0.5, 4)
plt.legend(fontsize=16)
plt.show()



>>>>>>> origin
