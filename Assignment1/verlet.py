import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x0 = 0
v0 = 1

# simulation time, timestep and time
t_max = 100
dt = 0.1
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []


x_list.append(x0)
v_list.append(v0)

x = x0 + v0*dt


for i in range(1,len(t_array)):

    x_list.append(x)

    a = -k * x_list[i] / m
    x = 2*x_list[i] - x_list[i-1] + dt**2*a  
    v = (x_list[i] - x_list[i-1])/dt

    v_list.append(v)
    

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.legend()
plt.show()
