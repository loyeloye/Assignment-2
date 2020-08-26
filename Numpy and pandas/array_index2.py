import numpy as np
ray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(ray)

#print (ray[2][2])

#slices of 2d ARRAY

slice1 = ray[0:2,0:3]
#print(slice1)

ray[:2,1:] = 30
# print
#using loops to index(ray)
ray_len = ray.shape[0]
for i in range (ray_len):
    ray[i] = i;
print(ray)

#more ways for accessing rows
#print (ray [[0,1]])