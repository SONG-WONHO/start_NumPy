#load numpy as np
import numpy as np

#type => numpy.ndarray

#np.char.add()
print(np.char.add('hi, ','numpy!')) ## hi, numpy!
print(np.char.add(['hi, '],['numpy!'])) ## ['hi, numpy!']
print(np.char.add(['hi, ','hello, '],['python!','numpy!'])) ## ['hi, python!' 'hello, numpy!']

#in python
print('hi, '+'numpy!') ##hi, numpy!

#np.char.multiply()
print(np.char.multiply('numpy! ',3)) ## numpy! numpy! numpy!
print(np.char.multiply(['numpy! '],3)) ## ['numpy! numpy! numpy! ']

#in python
print('numpy! '*3) ## numpy! numpy! numpy!

#np.char.center()
#np.char.rjust()
#np.char.ljust()
print(np.char.center('hello',20,'*')) ## *******hello********
print(np.char.center(['hello'],20,'*')) ## ['*******hello********']

print(np.char.rjust('hello',20,'*')) ## ***************hello
print(np.char.rjust(['hello'],20,'*')) ## ['***************hello']

print(np.char.ljust('hello',20,'*')) ## hello***************
print(np.char.ljust(['hello'],20,'*')) ##['hello***************']

#in python
print('hello'.center(20,'*')) ## *******hello********
print('hello'.rjust(20,'*')) ## ***************hello
print('hello'.ljust(20,'*')) ## hello***************

#np.char.capitalize()
print(np.char.capitalize('hello, numpy!')) ## Hello, numpy!
print(np.char.capitalize(['hello, numpy!', 'hi, python!'])) ## ['Hello, numpy!' 'Hi, python!']

#in python
print('hello, numpy!'.capitalize()) ## Hello, numpy!

#np.char.title()
print(np.char.title('hello, numpy!, hi, python!')) ## Hello, Numpy!, Hi, Pyhon!

#in python
print('hello, numpy!, hi, python!'.title()) ## Hello, Numpy!, Hi, Python!

#np.char.lower()
#np.char.upper()
print(np.char.lower('HELLO, NUMPY!')) ## hello, numpy!
print(np.char.upper('hello, numpy!')) ## HELLO, NUMPY!

#in python
print('HELLO, NUMPY!'.lower()) ## hello, numpy!
print('hello, numpy!'.upper()) ## HELLO, NUMPY!

#np.char.split()
print(np.char.split('numpy scipy matplotlib tensorflow')) ## ['numpy', 'scipy', 'matplotlib', 'tensorflow']
print(np.char.split('numpy,scipy,matplotlib,tensorflow', sep = ',')) ## ['numpy', 'scipy', 'matplotlib', 'tensorflow']

#in python
print('numpy scipy matplotlib tensorflow'.split()) ## ['numpy', 'scipy', 'matplotlib', 'tensorflow']
print('numpy,scipy,matplotlib,tensorflow'.split(',')) ## ['numpy', 'scipy', 'matplotlib', 'tensorflow']

#np.char.splitlines()
print(np.char.splitlines('numpy!\nhello, python!\nhi, library!')) ## ['numpy!', 'hello, python!', 'hi, library!']

#in python
print('numpy!\nhello, python!\nhi, library!'.splitlines()) ## ['numpy!', 'hello, python!', 'hi, library!']

#np.char.join()
print(np.char.join(':','ymd')) ## y:m:d
print(np.char.join([':','-'],['ymd','ymd'])) ## ['y:m:d' 'y-m-d']

#np.char.replace()
print(np.char.replace('hello, numpy!','hello','hi')) ## hi, numpy!

#in python
print('hello, numpy!'.replace('hello','hi')) ## hi, numpy!

#np.char.encode()
#np.char.decode()

a_str = 'numpy!'
a_str = np.char.encode(a_str,'cp500')
b_str = np.char.decode(a_str,'cp500')
print(a_str,b_str) ## b'\x95\xa4\x94\x97\xa8O' numpy!
