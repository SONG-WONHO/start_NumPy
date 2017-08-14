#load numpy as np
import numpy as np

#method1 - use slice
a_array = np.arange(10) ##[0 1 2 3 4 5 6 7 8 9]
s = slice(2,7)
print(a_array[s]) ##[2 3 4 5 6]

#method2 - array[start, stop, step]
a_array = np.arange(10) ##[0 1 2 3 4 5 6 7 8 9]
print(a_array[2:7]) ##[2 3 4 5 6]

#step = 2
print(a_array[2:7:2]) ##[2 4 6]

#2 <= num < stop
print(a_array[2:]) ##[2 3 4 5 6 7 8 9]

#start <= num < 7
print(a_array[:7]) ##[0 1 2 3 4 5 6]

#-1 => first from behind
print(a_array[2:-1]) ##[2 3 4 5 6 7 8]

#it can also be applied to multi-dimensional ndarray
a_array = np.arange(24) ##[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
a_array = np.reshape(a_array, [4,6])
'''
    [[ 0  1  2  3  4  5]
     [ 6  7  8  9 10 11]
     [12 13 14 15 16 17]
     [18 19 20 21 22 23]]
'''

print(a_array[2:])
'''
    [[12 13 14 15 16 17]
     [18 19 20 21 22 23]]
'''

print(a_array[:,:2])
'''
    [[ 0  1]
     [ 6  7]
     [12 13]
     [18 19]]
'''

print(a_array[:2,-1:])
'''
    [[ 5]
     [11]]
'''

#if step == -1: reverse
print(a_array[::-1])
'''
    [[18 19 20 21 22 23]
     [12 13 14 15 16 17]
     [ 6  7  8  9 10 11]
     [ 0  1  2  3  4  5]]

'''

print(a_array[::-1,::-1])
'''
    [[23 22 21 20 19 18]
     [17 16 15 14 13 12]
     [11 10  9  8  7  6]
     [ 5  4  3  2  1  0]]
'''
