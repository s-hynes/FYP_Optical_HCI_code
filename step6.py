import numpy as np

def binning(arr):
    """"""

    Y = arr.shape[0]
    X = arr.shape[1]
    M = arr.size

    arr2 = arr.reshape((M//2, 2))
    #print("\narr2 = ", arr2)
    #print(arr2.shape)
    arr3 = np.mean(arr2, axis=1)
    #print(arr3.size)
    arr4 = arr3.reshape( (arr3.size)//Y,Y)
    #print("\narr4 = ", arr4, "\n")

    return arr4

if __name__ == "__main__":
    array = np.arange(1, 4097).reshape(32, 128)
    print("\n{0}\n".format(array))
    array2 = binning(array)

