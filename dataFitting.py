import numpy as np 
import matplotlib.pyplot as plt

inputArray = np.array([0.3595, 0.2528, 0.2958, 0.3072, 0.3827, 0.5186, 0.5869, 0.6160, 0.7092, 0.7786, 0.8304, 0.8904, 0.9424, 0.9575,1.0000, 0.9988, 0.9969, 1.0000, 0.9757, 0.9049, 0.8868, 0.8317, 0.7572, 0.7039, 0.6628, 0.5290, 0.4582, 0.4497,0.3931, 0.2831, 0.1987, 0.3559])


x = np.arange(0, 32, 1)
coefficients1 = np.polyfit(x, inputArray, 5)
coefficients2 = np.polyfit(x, inputArray, 6)
coefficients3 = np.polyfit(x, inputArray, 7)


y = np.arange(0, 32, 32/50)
array1 = np.polyval(coefficients1, y)
array2 = np.polyval(coefficients2, y)
array3 = np.polyval(coefficients3, y)


print(array3)
# print(array3[49])
# print(inputArray[31])

# plt.figure()
# plt.plot(inputArray)
# plt.figure()
# plt.plot(array3)    
# plt.plot(inputArray)
# plt.show()