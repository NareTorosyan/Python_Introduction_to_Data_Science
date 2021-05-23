import numpy as np
#1 Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
def convert(list):
    return np.array(list)
print(convert([1,2,3]))

#2 Write a NumPy program to create a NumPy array with values ranging from 2 to 10.
def create(a,b):
    return np.arange(a,b)
print(create(2,10))


#3 Write a NumPy program to create a null vector of size 10 and update sixth to eight values to 11.
def update(a,b,c):
    arr=np.zeros(a)
    arr[b:c]=11
    return arr
print(update(10,5,8))

#4 Write a NumPy program to test whether each element of a 1-D array is also present in a second array.
def check(arr1,arr2):
    return np.in1d(arr1,arr2)
print(check(np.array([1,2,3,4,7,8]),np.array([4,7,1])))

def main():
    print(convert([1,2,3]))
    print(create(2,10))
    print(update(10, 5, 8))
    print(check(np.array([1, 2, 3, 4, 7, 8]), np.array([4, 7, 1])))