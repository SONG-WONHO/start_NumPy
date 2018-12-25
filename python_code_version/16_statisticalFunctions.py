#load numpy as np
import numpy as np

#np.amin(array, axis) ,최솟값
#np.amax(array, axis) ,최댓값
a_array = np.array([[3,7,5],[8,4,3],[2,4,9]])
'''
    [[3 7 5]
     [8 4 3]
     [2 4 9]]
 '''

print(np.amin(a_array)) ## 2
print(np.amin(a_array, axis = 0)) ## [2 4 3]
print(np.amin(a_array, axis = -1)) ## [3 3 2]

print(np.amax(a_array)) ## 9
print(np.amax(a_array, axis = 0)) ## [8 7 9]
print(np.amax(a_array, axis = -1)) ## [7 8 9]

#np.median(arraay, axis) ,중앙값
print(np.median(a_array)) ## 4.0
print(np.median(a_array, axis = 0)) ## [3. 4. 5.]
print(np.median(a_array, axis = -1)) ## [5. 4. 4.]

#np.mean(array, axis) ,평균
print(np.mean(a_array)) ## 5.0
print(np.mean(a_array, axis = 0)) ## [4.33 5.    5.67]
print(np.mean(a_array, axis = -1)) ## [5. 5. 5.]

#np.std() ,표준편차
print(np.std([1,2,3,4])) ## 1.118033

#np.var() ,분산
print(np.var([1,2,3,4])) ## 1.25
