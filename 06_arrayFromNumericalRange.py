#load numpy as np
import numpy as np

'''
np.arange(start = 0, stop, step = 1, dtype)
np.linspace(start = 0, stop, num = 50, endpoint = True, retstep = False, dtype)
np.logspace(start = 0, stop, num = 50, endpoint = True, base = 10, dtype)
'''

#evenly spaced values
a_array = np.arange(5)
print(a_array) ##[0 1 2 3 4]
a_array = np.arange(5,10)
print(a_array) ##[5 6 7 8 9]
a_array = np.arange(10,20,2,np.float32)
print(a_array) ##[ 10.  12.  14.  16.  18.]

#evenly spaced values between the interval is specified
a_array = np.linspace(10,20, 5, dtype = np.float32)
print(a_array) ##[ 10.   12.5  15.   17.5  20. ]
a_array = np.linspace(10,20, 5, endpoint = False, dtype = np.float32)
print(a_array) ##[ 10.  12.  14.  16.  18.]
a_array = np.linspace(10,20, 5, endpoint = False, retstep = True, dtype = np.float32)
print(a_array) ##(array([ 10.,  12.,  14.,  16.,  18.], dtype=float32), 2.0)

#evenly spaced values on log scale
a_array = np.logspace(1, 2, 5, dtype = np.float32)
print(a_array) ##[ 10. 17.78279495 31.62277603 56.23413086 100.]
a_array = np.logspace(1, 2, 5, endpoint = False, dtype = np.float32)
print(a_array) ##[ 10. 15.84893227 25.11886406 39.81071854 63.09573364]
a_array = np.logspace(1,10, 10, base = 2, dtype = np.float32)
print(a_array) ##[ 2. 4. 8. 16. 32. 64. 128. 256. 512. 1024.]
