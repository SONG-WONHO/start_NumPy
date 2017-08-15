#load numpy as np
import numpy as np

#Trigonometric Functions

#np.sin()
#np.cos()
#np.tan()
a_array = np.array([0, 30, 45, 60, 90])
print(np.sin(a_array*np.pi/180)) ## [ 0.          0.5         0.70710678  0.8660254   1.        ]
print(np.cos(a_array*np.pi/180)) ## [  1.00000000e+00   8.66025404e-01   7.07106781e-01   5.00000000e-01   6.12323400e-17]
print(np.tan(a_array*np.pi/180)) ## [  0.00000000e+00   5.77350269e-01   1.00000000e+00   1.73205081e+00   1.63312394e+16]

#np.around()
#np.floor()
#np.ceil()
a_array = np.array([1.0, 5.55, 123, 0.567, 25.532])
print(np.around(a_array)) ## [   1.    6.  123.    1.   26.]
print(np.around(a_array, 1)) ## [   1.     5.6  123.     0.6   25.5]
print(np.around(a_array, -1)) ## [   0.   10.  120.    0.   30.]
print(np.around(a_array, -2)) ## [   0.    0.  100.    0.    0.]

print(np.floor(a_array)) ## [   1.    5.  123.    0.   25.]
print(np.ceil(a_array)) ## [   1.    6.  123.    1.   26.]
