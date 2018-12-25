#load numpy as np
import numpy as np

'''
Iterating Over Array

np.nditer(object, flags, op_flags, op_dtypes, order, casting, op_axes, itershape, buffersize)
    -object: ndarray
    -op_flags: 'readonly', 'readwrite', 'no_broadcasting'
    -order: 'C', 'F', 'A', 'K'
'''

a_array = np.arange(0,60,5)
a_array = np.reshape(a_array,[3,4])
'''
    [[ 0  5 10 15]
     [20 25 30 35]
     [40 45 50 55]]
'''

for num in np.nditer(a_array):
    print(num, end = ' ')

print('\n')
## 0 5 10 15 20 25 30 35 40 45 50 55

for num in np.nditer(a_array, order = 'C'):
    print(num, end = ' ')

print('\n')
## 0 5 10 15 20 25 30 35 40 45 50 55

for num in np.nditer(a_array, order = 'F'):
    print(num, end = ' ')

print('\n')
## 0 20 40 5 25 45 10 30 50 15 35 55

#array.T => transpose
for num in np.nditer(a_array.T, order = 'C'):
    print(num, end = ' ')

print('\n')
## 0 20 40 5 25 45 10 30 50 15 35 55

for num in np.nditer(a_array, op_flags = ['readwrite']):
    num[...] = num * 2

print(a_array)
'''
    [[  0  10  20  30]
     [ 40  50  60  70]
     [ 80  90 100 110]]
'''

#broadcasting
a_array = np.arange(0,60,5)
a_array = np.reshape(a_array,[3,4])
'''
    [[ 0  5 10 15]
     [20 25 30 35]
     [40 45 50 55]]
'''

b_array = np.array([100,200,300,400])

for num1, num2 in np.nditer([a_array,b_array]):
    print("{0}: {1}".format(num1,num2), end = ' ')
## 0: 100 5: 200 10: 300 15: 400 20: 100 25: 200 30: 300 35: 400 40: 100 45: 200 50: 300 55: 400
