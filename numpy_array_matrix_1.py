#Program to take a number n as input and create a N*N matrix with 0's in centre and 1's on borders

import numpy as np
print('Enter the size of matrix : ',end='')
n=int(input())
if n==0:
    print('Enter valid choice')
else:
    arr1=np.empty(shape=(n,n),dtype='int')
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                arr1[i,j]=1
            else:
                arr1[i,j]=0
                
print('The output matrix is \n',arr1)
