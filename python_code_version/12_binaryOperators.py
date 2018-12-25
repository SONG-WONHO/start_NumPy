#load numpy as np
import numpy as np

#bitwise_and => and operation
a, b = 16, 17
print(bin(a), bin(b)) ## 0b10000 0b10001
print(np.bitwise_and(a,b)) ##16

#bitwise_or => or operation
print(np.bitwise_or(a,b)) ## 17

#invert => not operation
a = 13
b = np.invert(np.array([a], dtype = np.uint8))

print(np.binary_repr(a, width = 8)) ## 00001101
print(np.binary_repr(b[0], width = 8)) ## 11110010

#left shift
a = 10
b = np.left_shift(a,2)

print(np.binary_repr(a, width = 8)) ## 00001010
print(np.binary_repr(b, width = 8)) ## 00101000

#right shift
a = 40
b = np.right_shift(a,2)

print(np.binary_repr(a, width = 8)) ## 00101000
print(np.binary_repr(b, width = 8)) ## 00001010
