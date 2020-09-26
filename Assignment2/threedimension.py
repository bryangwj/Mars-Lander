import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#initialize constants and starting values
G = 6.67408 * (10 ** (-11))
M = 6.42 * (10 ** 23)
position = np.array([20000000,0,0])
velocity = np.array([1000,1000,0])

#Time values
t_max = 200000
dt = 10



def euler(position = position, velocity = velocity):

    position_array = np.zeros((int(t_max/dt),3))
    velocity_array = np.zeros((int(t_max/dt),3))

    for i in range(int(t_max/dt)):

        position_array[i] = position
        velocity_array[i] = velocity

        a = -(G*M)/(np.linalg.norm(position)**3)*position
        position = position + dt * velocity
        velocity = velocity + dt * a

    position_x, position_y, position_z = zip(*position_array)
    

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(position_x, position_y,position_z)

    plt.show()

def verlet(position = position, velocity = velocity):

    position_array = np.zeros((int(t_max/dt),3))
    velocity_array = np.zeros((int(t_max/dt),3))

    position_array[0] = position
    velocity_array[0] = velocity

    position = position + velocity * dt

    for i in range(1,int(t_max/dt)):

        position_array[i] = position

        a = -(G*M)/(np.linalg.norm(position)**3)*position
        position = 2*position_array[i] - position_array[i-1] + (dt)**2*a
        velocity = (position_array[i] - position_array[i-1])/dt

        velocity_array[i] = velocity

    position_x, position_y, position_z = zip(*position_array)
    

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(position_x, position_y,position_z)

    plt.show()





if __name__ == '__main__':
    euler()
    verlet()
    


