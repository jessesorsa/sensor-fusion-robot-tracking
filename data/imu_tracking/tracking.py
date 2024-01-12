import numpy as np
import csv
import matplotlib.pyplot as plt

# initial position and heading of the robot


def initial_conditions():
    px_0 = 0.627
    py_0 = 0.16
    phi_0 = 0

    return np.array([px_0, py_0, phi_0])


# reduced quasi-constant turn model used
def dynamic_model(xt, ut):
    return np.array([
        -ut[0] * np.cos(xt[2]),             # px*(t) = v(t) * cos(phi(t))
        ut[0] * np.sin(xt[2]),              # py*(t) = v(t) * sin(phi(t))
        ut[1]                               # phi*(t) = w_gyro(t)
    ])

# get inputs from recorded values in that are in the .csv files


def inputs_u():
    speed = []
    gyro_z = []

    # get speed values
    with open('/Users/jessesorsa/Koulu/Sensor_fusion/Project/Part_2/data/task6-task7/motor_control_tracking_task6.csv', 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in lines:
            a = ((float(row[1]) + float(row[2]))/2) * \
                0.189     # speed of the robot calculated
            if i == 0:
                speed = a
            else:
                speed = np.append(speed, a)
            i += 1

    # get gyroscope values
    with open('/Users/jessesorsa/Koulu/Sensor_fusion/Project/Part_2/data/task6-task7/imu_tracking_task6.csv', 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in lines:
            if i > 736:
                b = (np.deg2rad(float(row[8])) +
                     np.deg2rad(0.15235769230769233))   # bias of the gyroscope taken into account
                if i == 0:
                    gyro_z = b
                else:
                    gyro_z = np.append(
                        gyro_z, b)
            i += 1

    # getting both speed and gyroscope values to one array (different lenght of speed and gyro_z taken into account)
    a = 0
    inputs = []
    for i in range(len(gyro_z)):
        if ((i % 8 == 0) & (i != 0)):
            a += 1
        if (i == 0):
            inputs = np.append(speed[a], gyro_z[i])
        else:
            inputs = np.append(inputs, np.append(speed[a], gyro_z[i]))
    length = int(len(inputs)/2)
    inputs_adjusted = inputs.reshape(length, 2)
    print(length)

    return inputs_adjusted


# using Euler method for tracking
def Euler_solution(x0, t_0, t_end, inputs, func):
    u = inputs()
    N = 3560
    T = np.linspace(t_0, t_end, N)
    dt = 0.0645  # estimated from imu_tracking_task6 timestamps

    x_euler = np.zeros((T.shape[0], 3))
    x_euler[0, :] = x0

    for i in range(0, T.shape[0] - 1):
        x_euler[i+1, :] = x_euler[i, :] + func(x_euler[i, :], u[i, :])*dt
    return x_euler


# run the model with the following values
# get initial conditions
x0 = initial_conditions()

# start and end times
t_0 = 0
t_end = 180

# run the Euler method
# input: initial conditions, start and end times, input values from .csv files, the dynamic turn model
# output: array with route of the robot in x,y coordinates
xt = Euler_solution(x0, t_0, t_end, inputs_u, dynamic_model)

# plot the route of the robot
f, ax = plt.subplots(1, 1, figsize=(7, 7))
plt.scatter(xt[:, 0], xt[:, 1], marker='o', label='Robot-position', s=1)
ax.legend()
plt.show()
