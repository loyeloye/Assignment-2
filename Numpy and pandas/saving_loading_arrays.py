import numpy as np

tey = np.arange(10)
print(tey)

np.save('saved_array',tey)
#new file has been created as - saved_array.npy

new_array =  np.load('saved_array.npy')
print(new_array)

#how to save multiple arrays
tey_1 = np.arange(10,25,)
tey_2 = np.arange(1,30,2)
np.savez('saved_archive.npz' , x = tey_1, y = tey_2)

tey_3 = np.load ('saved_archive.npz')
print('tey_3 [x] is')
print(tey_3 ['x'])

print('tey_3 [y] is')
print(tey_3['y'])

#saving to a .txt file
np.savetxt('notepadfile.txt', tey_1, delimiter=',')

#loading of .txt files
load_txt_file = np.loadtxt('notepadfile.txt', delimiter=',')
print('load_txt_file is')
print(load_txt_file)