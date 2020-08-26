import numpy as np
List1= [1,2,3,4,5,6]
List2= [7,8,9,10,11,12]
#to turn this to a numpy array you do this
Array1= np.array([List1,List2])
print(Array1)
#f = [a*b for a,b in zip(a,b)] #works even though the list is not the same length, it multiplies the list# # #print(f)

 #works when the list is the same size np.multiply(a,b)
print(Array1.shape)