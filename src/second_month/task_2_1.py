import numpy as np
#1 Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
list=[1,2,3,4,5,6,7]
arr=np.array(list)
print(arr)

#2 Write a NumPy program to create a NumPy array with values ranging from 2 to 10.
arr=np.arange(2,10)
print(arr)


#3 Write a NumPy program to create a null vector of size 10 and update sixth to eight values to 11.
arr=np.zeros(10)
arr[6:9]=11
print(arr)

#3 Write a NumPy program to test whether each element of a 1-D array is also present in a second array.
arr1=np.array([1,2,3,4,7,8])
arr2=np.array([4,7,1])
print(np.in1d(arr1,arr2))