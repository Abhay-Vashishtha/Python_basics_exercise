"""Given 'm' and 'n', swap the mth and nth columns of the provided 2-D matrix

arr = [[4 3 1]
       [5 7 0]
       [9 9 3]
       [8 2 4]] """

import numpy as np
arr=np.array([[4,3,1],
              [5,7,0],
              [9,9,3],
              [8,2,4]])
print('Original array : \n',arr)
print('Enter the value of m and n (0-3):')
print('m = ',end='')
m=int(input())
print('n = ',end='')
n=int(input())
arr[:,[m,n]]=arr[:,[n,m]]
print('Swapped array  ;\n',arr)
