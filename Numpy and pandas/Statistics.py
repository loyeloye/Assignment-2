import numpy as np
import matplotlib.pyplot as plt
axes_values = np.arange(-10,100,10)

dx, dy = np.meshgrid(axes_values,axes_values)

print(dx)
print("dy")
print(dy)

print("function")
function = 2*dx+3*dy
function2 = np.cos(dx) + np.cos(dy)
print(function2)

plt.imshow(function2)
plt.title("function cos plot")
plt.colorbar()
plt.savefig("myfig2.png")

08033234721