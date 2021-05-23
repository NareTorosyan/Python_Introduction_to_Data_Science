import numpy as np
#1 Write a NumPy program to compute the multiplication of two given matrixes
x1=np.array([[2,2,6],[1,9,10]])
y1=np.array([[2,2],[1,4],[5,6]])
def mul(x,y):
    return x.dot(y)
print(mul(x1,y1))

from numpy.linalg import det,inv
#2 Write a NumPy program to compute the determinant of an array
arr=np.array([[1,2,4],[3,4,5],[3,4,9]])
def determinant(array):
    return det(array)
print(det(arr))

#3 Write a NumPy program to compute the sum of the diagonal element of a given array
arr=np.array([[1,2,4],[3,4,5],[3,4,9]])
def sum_of_diagonal_elements(array):
    return np.trace(array)
print(sum_of_diagonal_elements(arr))

#4Write a NumPy program to compute the inverse of a given matrix
arr=np.array([[1,2,4],[3,4,5],[3,4,9]])
def inverse_matrix(array):
    return inv(array)
print(inverse_matrix(arr))

#5Write a NumPy program to generate matrix and write it to a file, then again read from file that matrix.
arr=np.array([[1,2,4],[3,4,5],[3,4,9]])
def create_file(array):
    np.save("some_array",array)
    return np.load("some_array.npy")
print(create_file(arr))


def main():
    print(mul(np.array([[2,2,6],[1,9,10]]),np.array([[2,2],[1,4],[5,6]])))
    print(det(np.array([[1,2,4],[3,4,5],[3,4,9]])))
    print(np.array([[1,2,4],[3,4,5],[3,4,9]]))
    print(inverse_matrix(np.array([[1,2,4],[3,4,5],[3,4,9]])))
    print(create_file(np.array([[1,2,4],[3,4,5],[3,4,9]])))