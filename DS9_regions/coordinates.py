<<<<<<< HEAD
import numpy as np

image_height = 1023
coords = np.array((520.2576,498.4848,90.296888,70.992036,150.336,118.1952,0))
coords_halved = coords 
#print(coords_halved)
y_coords = coords_halved[1::2]
#print("\n",y_coords)
flipped_y_coords = image_height - y_coords
#print("\n", flipped_y_coords)

for i in range(flipped_y_coords.shape[0]):
    print(1+2*i)
    coords_halved[1+2*i] = flipped_y_coords[i]

print(coords_halved)

with open('GG-Tau_outer_disc_optical.reg', 'a') as file:
    file.write("\nellipse(")
    for i in range(coords_halved.shape[0]-1):
        file.write("{0},".format(coords_halved[i]))
=======
import numpy as np

image_height = 1023
coords = np.array((520.2576,498.4848,90.296888,70.992036,150.336,118.1952,0))
coords_halved = coords 
#print(coords_halved)
y_coords = coords_halved[1::2]
#print("\n",y_coords)
flipped_y_coords = image_height - y_coords
#print("\n", flipped_y_coords)

for i in range(flipped_y_coords.shape[0]):
    print(1+2*i)
    coords_halved[1+2*i] = flipped_y_coords[i]

print(coords_halved)

with open('GG-Tau_outer_disc_optical.reg', 'a') as file:
    file.write("\nellipse(")
    for i in range(coords_halved.shape[0]-1):
        file.write("{0},".format(coords_halved[i]))
>>>>>>> origin
    file.write("{0})".format(coords_halved[-1]))