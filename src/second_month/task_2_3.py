import numpy as np
#1Write a program to find maximum and minimum values of multidimensional NumPY massive

arr = np.arange(1, 12, 2).reshape(2, 3)
def max_min(array):
    return np.max(array), np.min(array)
print(max_min(arr))

#2Write a program to find maximum and minimum values of the second column of multidimensional NumPY massive

arr = np.arange(1, 12, 2).reshape(2, 3)
def max_min_by_2nd_column(array):
    return np.max(array[:,2]),np.min(array[:,2])
print(max_min_by_2nd_column(arr))

#3Write a program to find the median of a multidimensional NumPY massive
arr = np.arange(1, 12, 2).reshape(2, 3)
def median(array):
    return np.median(array)
print(median(arr))

#4Create one-dimentional and multidimentional NumPy massives and multiply with each other
arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([[1,2,3],[8,9,10]])
arr1_reshaped = arr1.reshape((3,2))
print(np.dot(arr1_reshaped,arr2))

