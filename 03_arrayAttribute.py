#load numpy as np
import numpy as np
#We will treat shape & ndim

#shape
'''
object.shape

    dimension 1 => (d0,)
    dimension 2 => (d1,d0)
    dimension 3 => (d2,d1,d0)
    dimension 4 => (d3,d2,d1,d0)
'''

#show shape
a_array = np.array([1,2,3])
print(a_array.shape)
##(3,)

a_array = np.array([[1,2,3],[1,2,3]])
print(a_array.shape)
##(2,3)

a_array = np.array([[[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4]]])
print(a_array.shape)
##(2,2,4)

#reshape - method1
#(2,3) => (3,2)
a_array = np.array([[1,2,3],[4,5,6]])
a_array.shape = (3,2)
print(a_array)

'''
np.reshape(object, newshape, order)
'''

#reshap - method2
#(2,3) => (3,2)
a_array = np.array([[1,2,3],[4,5,6]])
b_array = np.reshape(a_array, (3,2))
print(b_array)

#ndim
'''
object.ndim

    dimension1 => 1
    dimension2 => 2
    dimension3 => 3
    dimension4 => 4
'''

#create evenly spaced numbers
a_array = np.arange(24)
print(a_array)
##[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
print(a_array.ndim)
##1
b_array = np.reshape(a_array, (2,4,3))
print(b_array)
##[[[ 0  1  2]  [ 3  4  5]  [ 6  7  8]  [ 9 10 11]] [[12 13 14]  [15 16 17]  [18 19 20]  [21 22 23]]]
print(b_array.ndim)
##3
