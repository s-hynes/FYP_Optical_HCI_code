import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import datetime as dt

def azimuthal(Q_val, U_val):
    
    phi = np.zeros_like(Q_val)
    
    for i in range(phi.shape[0]):
        for j in range((phi.shape[1])):
            # i corresponds to y, j corresponds to x
            phi[i,j] = np.atan( (255.75 - j)/(i - 255.5))

    #plt.imshow(phi, origin ='lower', cmap='hot')
    #plt.colorbar()
    #plt.show()

    Q_phi = -Q_val * np.cos(2*phi) - U_val * np.sin(2*phi)
    U_phi = +Q_val * np.sin(2*phi) - U_val * np.cos(2*phi)

    plt.figure(1)
    plt.imshow(Q_phi, origin ='lower', cmap='hot', norm='symlog')
    plt.colorbar()

    plt.figure(2)
    plt.imshow(U_phi, origin ='lower', cmap='hot', norm='symlog')
    plt.colorbar()
    #plt.show()

    return Q_phi, U_phi

radii_step = 0.5
inner_radii = np.arange(5, 7+radii_step, radii_step)

for r_in in inner_radii:
    outer_radii = np.arange(r_in+radii_step, 13 + radii_step, radii_step)
    for r_out in outer_radii:
        hdu_list_Q = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step9" + "/2025-03-10-Callas-Q_IP_corr_Rin={1}_Rout={0}".format(r_out, r_in)  + ".fits", overwrite=True)
        image_Q = hdu_list_Q[0].data
        hdu_list_Q.close()

        hdu_list_U = fits.open("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step9" + "/2025-03-10-Callas-U_IP_corr_Rin={1}_Rout={0}".format(r_out, r_in)  + ".fits", overwrite=True)
        image_U = hdu_list_U[0].data
        hdu_list_U.close()

        images = azimuthal(image_Q, image_U)

        hdu = fits.PrimaryHDU(data=images[0])
        hdu.writeto("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step10" + "/" + "{0}-".format(dt.date.today()) + "Callas-" + "Q_phi_Rin={1}_Rout={0}".format(r_out, r_in)  + ".fits", overwrite=True)
        hdu = fits.PrimaryHDU(data=images[1])
        hdu.writeto("C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/project-code/manipulated-data/step10" + "/" + "{0}-".format(dt.date.today()) + "Callas-" + "U_phi_Rin={1}_Rout={0}".format(r_out, r_in)  + ".fits", overwrite=True)