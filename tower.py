#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


data = np.loadtxt("droptower_vdata.txt", unpack = True)
time = data[0]
velocity = data[1]
position = integrate.cumtrapz(velocity, initial = 0) + 30
acceleration = np.diff(velocity)
acc_times = np.arange(0.5, 10.5, 1)

#Position is Blue
plt.plot(time,position)

#Velocity is Green
plt.plot(time,velocity)

#Acceleration is red
plt.plot(acc_times,acceleration)





plt.show()



