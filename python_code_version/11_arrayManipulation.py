#load numpy as np
import numpy as np

#Changing shape
'''
1. np.reshape(object, newshape, order)
2. array.flatten(order)
'''

#reshape
a_array = np.arange(24)
'''
    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
'''
a_array = np.reshape(a_array, [4,6])
print(a_array)
'''
    [[ 0  1  2  3  4  5]
     [ 6  7  8  9 10 11]
     [12 13 14 15 16 17]
     [18 19 20 21 22 23]]
'''

#flatten
print(a_array.flatten())
'''
    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]

'''

print(a_array.flatten(order = 'F'))
'''
    [ 0  6 12 18  1  7 13 19  2  8 14 20  3  9 15 21  4 10 16 22  5 11 17 23]
'''

#Transpose operations
'''
1. np.transpose(arr, axes)
2. array.T
'''

a_array = np.arange(24).reshape(3,8)
'''
    [[ 0  1  2  3  4  5  6  7]
     [ 8  9 10 11 12 13 14 15]
     [16 17 18 19 20 21 22 23]]
'''

print(np.transpose(a_array))
'''
    [[ 0  8 16]
     [ 1  9 17]
     [ 2 10 18]
     [ 3 11 19]
     [ 4 12 20]
     [ 5 13 21]
     [ 6 14 22]
     [ 7 15 23]]
'''

print(a_array.T)
'''
    [[ 0  8 16]
     [ 1  9 17]
     [ 2 10 18]
     [ 3 11 19]
     [ 4 12 20]
     [ 5 13 21]
     [ 6 14 22]
     [ 7 15 23]]
'''

#Changing dimensions
'''
1. np.expand_dims(arr, axis)
'''

#expand dimensions
a_array = np.array([[1,2],[3,4]])
'''
    [[1 2]
     [3 4]]
'''
#shape: (2,2)

print(np.expand_dims(a_array,0))
'''
    [[[1 2]
      [3 4]]]
'''
#shape: (1,2,2)

print(np.expand_dims(a_array,1))
'''
    [[[1 2]]

     [[3 4]]]
'''
#shape: (2,1,2)

print(np.expand_dims(a_array,2))
'''
    [[[1]
      [2]]

     [[3]
      [4]]]
'''
#shape: (2,2,1)

#remove dimesion
a_array = np.arange(9).reshape(1,3,3)
'''
    [[[0 1 2]
      [3 4 5]
      [6 7 8]]]
'''
#shape: (1,3,3)

print(np.squeeze(a_array))
'''
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
'''
#shape: (3,3)
