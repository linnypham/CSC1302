import numpy as np

arr = np.zeros((4,5),int)

arr = np.insert(arr,1,7,0)

arr = np.insert(arr,1,5,1)

arr = np.delete(arr,0,0)

arr = np.delete(arr,0,1)

arr = np.sort(arr,0)

arr= np.ravel(arr,order='c')
print(arr)