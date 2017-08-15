#load numpy as np
import numpy as np

a_array = np.arange(16).reshape(4,4)
'''
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]
     [12 13 14 15]]
'''

b_array = np.array([10,10,10,10])
'''
    [10 10 10 10]
'''

print(np.add(a_array,b_array))
'''
    [[10 11 12 13]
     [14 15 16 17]
     [18 19 20 21]
     [22 23 24 25]]
'''

print(np.subtract(a_array,b_array))
'''
    [[-10  -9  -8  -7]
     [ -6  -5  -4  -3]
     [ -2  -1   0   1]
     [  2   3   4   5]]
'''

print(np.multiply(a_array,b_array))
'''
    [[  0  10  20  30]
     [ 40  50  60  70]
     [ 80  90 100 110]
     [120 130 140 150]]
'''

print(np.divide(a_array,b_array))
'''
    [[ 0.   0.1  0.2  0.3]
     [ 0.4  0.5  0.6  0.7]
     [ 0.8  0.9  1.   1.1]
     [ 1.2  1.3  1.4  1.5]]
'''

#np.power()
a_array = np.array([10, 100, 1000])
b_array = np.array([1, 2, 3])
print(np.power(a_array,2)) ## [    100   10000 1000000]
print(np.power(a_array,b_array)) ## [        10      10000 1000000000]

#np.mod()
#np.remainder()
a_array = np.array([13])
b_array = np.array([1,2,3,4,5,6,7,8])

print(np.mod(a_array,b_array)) ## [0 1 1 1 3 1 6 5]
print(np.remainder(a_array,b_array)) ## [0 1 1 1 3 1 6 5]
