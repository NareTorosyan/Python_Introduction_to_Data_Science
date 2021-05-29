import numpy as np
from numpy.linalg import det
#1 Write a NumPy program to compute the multiplication of two given matrixes
def mul(x,y):
    return x.dot(y)


def determinant(array):
    return np.linalg.det(array)


#3 Write a NumPy program to compute the sum of the diagonal element of a given array
def sum_of_diagonal_elements(array):
    return np.trace(array)


#4Write a NumPy program to compute the inverse of a given matrix
def inverse_matrix(array):
    return np.linalg.inv(array)


#5Write a NumPy program to generate matrix and write it to a file, then again read from file that matrix.

def create_file(array):
    np.save("some_array",array)
    return np.load("some_array.npy")


def main():
    arr = np.random.randint(5, size=(2, 4))
    x1 = np.array([[2, 2, 6], [1, 9, 10]])
    y1 = np.array([[2, 2], [1, 4], [5, 6]])
    print(mul(x1,y1))
    print(sum_of_diagonal_elements(x1))
    print(create_file(arr))
main()


