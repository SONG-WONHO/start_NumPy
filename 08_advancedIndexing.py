#load numpy as np
import numpy as np

#슬라이싱 범위를 입력할 수 도 있지만, 구체적인 인덱스 값을 입력할 수도 있다.
a_array = np.arange(24)
a_array = np.reshape(a_array,[4,6])
'''
    [[ 0  1  2  3  4  5]
     [ 6  7  8  9 10 11]
     [12 13 14 15 16 17]
     [18 19 20 21 22 23]]
'''

#row: 0  col: 0
print(a_array[[0],[0]])
'''
    [0]
'''

#rows: 0,1  col: 0
#broadcasting
print(a_array[[0,1],[0]])
'''
    [0 6]
'''

#rows: 0,3  col: 0
#boradcasting
print(a_array[[0,3],[0]])
'''
    [ 0 18]
'''

#rows: 0,1  cols: 0,1,2,3
#print(a_array[[0,1],[0,1,2,3]]) it will get an error because of broadcasting
#hence
print(a_array[[[0,0,0,0],[1,1,1,1]],[[0,1,2,3],[0,1,2,3]]])
'''
    [[0 1 2 3]
     [6 7 8 9]]
'''

#슬라이싱 범위에 조건문이 올 수도 있다.
a_array = np.arange(24)
a_array = np.reshape(a_array,[4,6])
'''
    [[ 0  1  2  3  4  5]
     [ 6  7  8  9 10 11]
     [12 13 14 15 16 17]
     [18 19 20 21 22 23]]
'''

print(a_array[a_array >= 12])
'''
    [12 13 14 15 16 17 18 19 20 21 22 23]
'''

a_array = np.array([1,2,3,4+3j,5+6j,np.nan,6,7,np.nan])
'''
    [1, 2, 3, (4+3j), (5+6j), nan, 6, 7, nan]
'''

print(a_array[np.iscomplex(a_array)])
'''
    [ 4.+3.j  5.+6.j]
'''

#~ means not
print(a_array[~np.isnan(a_array)])
'''
    [ 1.+0.j  2.+0.j  3.+0.j  4.+3.j  5.+6.j  6.+0.j  7.+0.j]
'''
