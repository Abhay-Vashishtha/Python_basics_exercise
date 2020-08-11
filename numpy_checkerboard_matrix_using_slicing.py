"""Take a value 'n' from user and create a checker board n*n matrix with 0 and 1
      
   n=2  [1 0]
        [0 1]
   
   n=3  [1 0 1]
        [0 1 0]
        [1 0 1]
        
   n=4  [1 0 1 0]
        [0 1 0 1]
        [1 0 1 0]
        [0 1 0 1]"""

import numpy as np
print('Enter the size of matrix : ',end='')
n=int(input())
arr=np.zeros((n,n),dtype='int')
arr[::2,::2]=1
arr[1::2,1::2]=1
print(arr)
