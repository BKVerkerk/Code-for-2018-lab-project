import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# inputArray = np.array([0.3595, 0.2528, 0.2958, 0.3072, 0.3827, 0.5186, 0.5869, 0.6160, 0.7092, 0.7786, 0.8304, 0.8904, 0.9424, 0.9575,1.0000, 0.9988, 0.9969, 1.0000, 0.9757, 0.9049, 0.8868, 0.8317, 0.7572, 0.7039, 0.6628, 0.5290, 0.4582, 0.4497,0.3931, 0.2831, 0.1987, 0.3559])
inputArray = np.array([0.34144803, 0.29685796, 0.27944466, 0.28360598, 0.30450921, 0.33801711,\
 0.38061815, 0.42936061, 0.48179076, 0.53589482, 0.59004476, 0.64294792,\
 0.69360022, 0.74124299, 0.78532345, 0.82545858, 0.86140241, 0.89301673,\
 0.92024502, 0.94308966, 0.96159222, 0.97581694, 0.98583713, 0.99172458,\
 0.99354188, 0.99133753, 0.98514383, 0.97497743, 0.96084255, 0.94273676,\
 0.92065923, 0.89462139, 0.86466004, 0.83085268, 0.79333507, 0.75232103,\
 0.70812425, 0.66118222, 0.61208203, 0.56158818, 0.51067215, 0.46054377,\
 0.41268429, 0.36888109, 0.33126397, 0.30234292, 0.28504735, 0.28276674,\
 0.29939248, 0.33936111])

output1 = np.reshape(np.outer(inputArray,inputArray).ravel(), (50, 50))

np.savetxt("outputReshaped.csv", output1, delimiter=",")

# nx, ny = 50, 50
# x = range(nx)
# y = range(ny)

# hf1 = plt.figure()
# ha = hf1.add_subplot(111, projection='3d')

# X, Y = np.meshgrid(x, y)  # `plot_surface` expects `x` and `y` data to be 2D
# ha.plot_surface(X, Y, output1, cmap='jet')

if output1.any()<=0.1:
    output1=0.1

output2 = np.around(output1, decimals=1)
np.savetxt("outputReshaped2.csv", output2, delimiter=",")
# print(output2)

np.set_printoptions(threshold=np.inf)
finalOutput = output2.ravel()
# print("{0:.1f}".format(finalOutput))
# np.trunc(finalOutput)
np.savetxt("outputReshaped3.csv", finalOutput, fmt = '%f')
# print(finalOutput)
np.savetxt("outputReshaped3.txt",finalOutput, fmt = '%.1f', delimiter=",")
# test = np.arange(0, 25, 1)
# np.savetxt("test.txt", test, fmt = '%f', delimiter='\t')
nx, ny = 50, 50
x = range(nx)
y = range(ny)

hf2 = plt.figure()
ha = hf2.add_subplot(111, projection='3d')

X, Y = np.meshgrid(x, y)  # `plot_surface` expects `x` and `y` data to be 2D
ha.plot_surface(X, Y, output2, cmap='inferno')

plt.show()