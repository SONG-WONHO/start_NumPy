#load numpy as np
import numpy as np

'''
np.asarray(object, dtype = None, order = None)
np.frombuffer(buffer, dtype = float, count = -1, offset = 0)
np.fromiter(iterable, dtype, count = -1)
'''

#list, tuple => ndarray
a_list = [c for c in range(5)]
print(type(a_list)) ##<class 'list'>
a_tuple = (0,1,2,3,4)
print(type(a_tuple)) ##<class 'tuple'>
a_array = np.asarray(a_list)
print(type(a_array)) ##<class 'numpy.ndarray'>
a_array = np.asarray(a_tuple)
print(type(a_array)) ##<class 'numpy.ndarray'>

#butter => ndarray
#Not used often
string = b'hello, numpy!'
a_array = np.frombuffer(string, dtype = 'S1')
print(a_array)
##[b'h' b'e' b'l' b'l' b'o' b',' b' ' b'n' b'u' b'm' b'p' b'y' b'!']

#iterator => ndarray
#Not used often
a_range = range(5)
it = iter(a_range)
a_array = np.fromiter(it, dtype = np.float32)
print(a_array)
##[ 0.  1.  2.  3.  4.]
