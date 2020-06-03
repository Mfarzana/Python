#NumPy is a python library used for working with arrays.
#NumPy stands for Numerical Python.
#pip standard package-management system used to install and manage software packages written in Python.

import numpy

arr =numpy.array([1,3,4,4,5])
print("1D array: ",arr)
arr2=numpy.array([[1,3,4,4,5],[2,5,6,7,7]])
print("2D Array ",arr2)
print(" 2nd element of 2nd dimension",arr2[1,1])

# arange
print(numpy.arange(10))
print(numpy.arange(2,10))
print(numpy.arange(2,10,2))
print(numpy.arange(2,10,2,dtype=float))
arr=numpy.arange(2,20,2)




