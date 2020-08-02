"""
Basic numpy functions.
"""
import numpy as np
import math
print('***I was created for some often used numpy functions purpose to understand Mr.Jha*** ')
a = [0, .5, .2]
print('This list is used for the following numpy functions', a)
print('Inverse of cos values are ', np.arccos(a))
print('Inverse of sin values are ', np.arcsin(a))
print('Inverse of tan values are ', np.arctan(a))
print('The degrees value are ', np.degrees(a))
print('The values of tan are', np.tan(a))
print('The hyperbolic values of tanh are', np.tanh(a))
print('The conversion of degree to radian are', np.deg2rad(a))
print('Inverse value of sinh are ', np.arcsinh(a))
print('Inverse value of tanh are ', np.arctanh(a))
b = [10, 5, 3]
c = [2, 6, 4]
print('The hypotenuse is ', np.hypot(b, c))
print('Math function', math.pi)
d = [90, 45, 30, 60]
print('Degree to radian value', np.deg2rad(d))
print('Radian to degree value are', np.rad2deg(a))
print('Radians value', np.radians(d))
e = [0.1, 2.2, 3.2, 5.6]
print('Input array for ceil', e)
print('Output array for ceil', np.ceil(e))
print('Same array output for floor', np.floor(e))
print('Same array output for fix', np.fix(e))
print('Same array output for rint', np.rint(e))


