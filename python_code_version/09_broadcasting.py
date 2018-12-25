#load numpy as np
import numpy as np

a_array = np.array([[0,0,0],[10,10,10],[20,20,20],[30,30,30]], dtype = np.float32)
'''
    [[  0.   0.   0.]
     [ 10.  10.  10.]
     [ 20.  20.  20.]
     [ 30.  30.  30.]]
'''

#broadcasting horizontally and vertically
b_array = np.array([1])
'''
    [1]
'''

print(a_array + b_array)
'''
    [[  1.   1.   1.]
     [ 11.  11.  11.]
     [ 21.  21.  21.]
     [ 31.  31.  31.]]
'''

#broadcasting vertically
b_array = np.array([1,2,3], dtype = np.float32)
'''
    [ 1.  2.  3.]
'''

print(a_array + b_array)
'''
    [[  1.   2.   3.]
     [ 11.  12.  13.]
     [ 21.  22.  23.]
     [ 31.  32.  33.]]
'''

#boradcasting horizontally
b_array = np.array([[1],[2],[3],[4]], dtype = np.float32)
'''
    [[ 1.]
     [ 2.]
     [ 3.]
     [ 4.]]
'''

print(a_array + b_array)
'''
    [[  1.   1.   1.]
     [ 12.  12.  12.]
     [ 23.  23.  23.]
     [ 34.  34.  34.]]
'''
