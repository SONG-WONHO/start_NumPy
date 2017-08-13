#load numpy as np
import numpy as np

'''
np.empty(shape, dtype, order)
np.zeros(shape, dtype, order)
np.ones(shape,dtype,order)
'''

#create uninitialized array
a_array = np.empty([2,2], np.float32)
print(a_array.shape, a_array)
##(2, 2) [[  2.29812948e-43   0.00000000e+00] [  0.00000000e+00   0.00000000e+00]]

#create array initialized by zeros
a_array = np.zeros([2,2], np.float32)
print(a_array.shape, a_array)
##(2, 2) [[ 0.  0.] [ 0.  0.]]

#create array initialized by ones
a_array = np.ones([2,2], np.float32)
print(a_array.shape, a_array)
##(2, 2) [[ 1.  1.] [ 1.  1.]]
