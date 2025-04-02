import numpy as np

# This is how reshaping an array works

#arr = np.arange(1,11)
#print("\narr = ", arr)

#arr2 = arr.reshape((2,5))

#print("\narr2 = ", arr2)

#-----------------------------------------------------------------
# I think this would work for pixel binning in the x-direction.
# I'm sure there's a function for it already but I haven't been able to find
# one quickly.

arr3 = np.array([   [1, 3, 2, 6, 1, 3, 2, 6],
                    [2, 6, 4, 12, 2, 6, 4, 12],
                    [1, 5, 4, 6, 1, 5, 4, 6],
                    [2, 4, 6, 12, 2, 4, 6, 12]])

Y = arr3.shape[0]
X = arr3.shape[1]
print("\narr3 =\n", arr3)
print(arr3.shape)
M = arr3.size

arr4 = arr3.reshape((M//2, 2))
print("\narr4 =\n", arr4)
print(arr4.shape)
arr5 = np.mean(arr4, axis=1)
print(arr5.size)
arr6 = arr5.reshape( (arr5.size)//Y,Y)
print("\narr6 =\ns", arr6, "\n")
