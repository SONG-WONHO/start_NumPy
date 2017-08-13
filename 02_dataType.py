#load numpy as np
import numpy as np

'''
np.dtype(object, align, copy)

    'b' - boolean
    'i' - integer
    'u' - unsigned integer
    'f' - float
    'c' - complex
    'o' - objects
    'S' - string
    'U' - unicode
'''

dt = np.dtype(np.int32)
print(dt) ## int32

#int8, int16, int32, int64 = 'i1', 'i2', 'i4', 'i8'
dt = np.dtype('i1')
print(dt) ## int8

#float16, float32, float64 = 'f2'. 'f4', 'f8'
dt = np.dtype('f2')
print(dt) ## float16

#string = 'S'
dt = np.dtype('S10')
print(dt) ## S10

#>, < = big endian, little endian
dt = np.dtype('>i8')
print(dt)## big endian int64

#structured data type
#[(field name, data type)]
dt = np.dtype([('age', np.int8)])
print(dt) ## [('age', 'i1')]

dt = np.dtype([('name', 'S20'), ('age', 'i1'), ('student_num', 'i2')])
print(dt) ## [('name', 'S20'), ('age', 'i1'), ('student_num', '<i2')]

#now apply it to ndarray object
a_array = np.array([('max', 20, 1000),('tim',21,1001),('herry',20,1002)], dtype = dt)
print(a_array['name']) ## [b'max' b'tim' b'herry']
print(a_array['age']) ## [20 21 20]
print(a_array['student_num']) ## [1000 1001 1002]
