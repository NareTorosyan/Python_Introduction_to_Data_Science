import numpy as np
#1Write a program to find maximum and minimum values of multidimensional NumPY massive
def max_min(array):
    return np.max(array), np.min(array)


#2Write a program to find maximum and minimum values of the second column of multidimensional NumPY massive
def max_min_by_2nd_column(array):
    return np.max(array[:,2]),np.min(array[:,2])


#3Write a program to find the median of a multidimensional NumPY massive
arr = np.arange(1, 12, 2).reshape(2, 3)
def median(array):
    return np.median(array)


#4Create one-dimentional and multidimentional NumPy massives and multiply with each other
def mul(array1,array2):
    arr1_reshaped = array1.reshape((3, 2))
    return np.dot(arr1_reshaped,array2)


def main():
    arr = np.arange(1, 12, 2).reshape(2, 3)
    arr1 = np.array([1, 2, 3, 4, 5, 6])
    arr2 = np.array([[1, 2, 3], [8, 9, 10]])
    print(max_min(arr))
    print(max_min_by_2nd_column(arr))
    print(median(arr))
    print(mul(arr1,arr2))
main()