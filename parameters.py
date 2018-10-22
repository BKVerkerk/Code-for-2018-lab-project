import numpy as np
import scipy.constants as sp

frequency = 436e6
c0 = sp.c
wavelength = c0/frequency
RCS = 10e-4
P_r = 2e-19
# P_r = 9.4e16
P_t = 1e6
T_range = 500e3
loss = 1.071519305
# gain = 15848

gain = (np.power(T_range,4)*np.power(4*np.pi,2)*P_r*loss)/(P_t*RCS*np.power(wavelength,2))
print(10*np.log(np.sqrt(gain)))

# P_r = (P_t*np.power(gain, 2)*np.power(wavelength, 2)*RCS)/(np.power(4*np.pi, 3)*np.power(T_range, 4))
# print(P_r)