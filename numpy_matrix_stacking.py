"""
arr1=[7  13 14]     (3x3)
     [18 10 17]
     [11 12 19]
     
arr2=[16 6 1]       (1-D)

arr3=[[5 8 4 3]]    (1x4)


out_arr=[7  13 14 5]
        [18 10 17 8]
        [11 12 19 4]
        [16 6  1  3]
"""


import numpy as np

arr1=np.array([[7,13,14],
               [18,10,17],
               [11,12,19]])
arr2=np.array([16,6,1])
arr3=np.array([[5,8,4,3]])
out_arr=np.vstack((arr1,arr2))
out_arr=np.hstack((out_arr,np.transpose(arr3)))
print(out_arr)
