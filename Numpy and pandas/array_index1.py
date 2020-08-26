import numpy as np
array = np.arange(0,12,)
print (array)

#print(array [0:5]) #shows array of (0,1,2,3,4)
#print(array[2:6]) #shows array (2,3,4,5)

array [0:5] = 30 #numbers 0-4 get assigned the value of 30
print(array)

# intresting thing and important

array2= array [0:6]

array2[:] = 29 #all elements are modified
print(array2)

arraycopy = array.copy()
print(arraycopy)





