#load numpy as np
import numpy as np

'''
np.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
'''

a_array = np.array([1,2,3])
print(a_array)
## [1 2 3]

a_array = np.array([1,2,3], dtype= np.float)
print(a_array)
## [1. 2. 3.]

a_array = np.array([[1,2,3],[4,5,6]], dtype= np.float)
print(a_array)
##[[ 1.  2.  3.] [ 4.  5.  6.]]

a_array = np.array([1,2,3], dtype= np.float, ndmin= 2)
print(a_array)
##[[ 1.  2.  3.]]

'''
1 dimension
[1,2,3] => shape:(3)

2 dimension
[[1,2,3],[4,5,6]] => shape:(2,3)

3 dimension
[[[1,2,3],[4,5,6]],[[11,12,13],[14,15,16]]] => shape:(2,2,3)

4 dimension
[[[[1,2],[3,4]],[[11,12],[13,14]]],[[[5,6],[7,8]],[[15,16],[17,18]]]] => shape:(2,2,2,2)
'''
