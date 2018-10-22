import numpy as np 
import scipy.constants as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

theta = np.radians(90)
phi = np.radians(80)
wavelength = sp.c/436000000

d_x = 5.968620625e-01
beta = 2*np.pi/wavelength

array_size = 50
x_phase = np.degrees(beta*d_x*(np.sin(theta)*np.cos(phi)))
y_phase = np.degrees(beta*d_x*(np.sin(theta)*np.sin(phi)))

x_rows = np.tile([x_phase*x for x in range(0,array_size)], (array_size, 1))


y_rows = np.array([y_phase*y for y in range(0,array_size)])
y_rows2 = y_rows.transpose()

y_rows2.shape = (array_size, 1)
y_rows3 = np.tile(y_rows, (array_size, 1))
y_rows4 = y_rows3.transpose()


output = np.add(x_rows,y_rows4)

np.savetxt("outputphasing.csv",output.ravel(), fmt = '%.1f', delimiter=",")
# print(output)
# print(np.tile(y_rows2, (array_size, 1)))

# output1 = np.reshape(np.outer(x_rows,y_rows).ravel(), (array_size, array_size))
# output2 = output1.ravel()

# np.savetxt("phasing.txt",output2, fmt = '%.1f', delimiter=",")

# nx, ny = 5, 5
# x = range(nx)
# y = range(ny)

# hf1 = plt.figure()
# ha = hf1.add_subplot(111, projection='3d')

# X, Y = np.meshgrid(x, y)  # `plot_surface` expects `x` and `y` data to be 2D
# ha.plot_surface(X, Y, output1, cmap='jet')

# plt.show()