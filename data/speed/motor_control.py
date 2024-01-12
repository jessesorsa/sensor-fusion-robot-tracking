import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import csv


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the CSV file
csv_file_path = os.path.join(script_dir, 'robot_speed_task4.csv')

distance = []  # in cm
time = []  # in s

# get time and distance data
with open('/Users/jessesorsa/Koulu/Sensor_fusion/project-code/data/speed/robot_speed_task4.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        distance.append(float(row[0])/100)
        time.append(float(row[1]))


# adjust the data so that it increases with each step
t_adjusted = []
i = 0
print(time)
while i < len(time):
    t_adjusted.append(sum(time[:i])+time[i])
    i += 1

# plot data
plt.plot(t_adjusted, distance, color='r', label="x")
plt.ylabel('Dist (m)')
plt.xlabel('Time (s)')
plt.title('Motor control')
plt.show()

# using a linear regression model to calculate the speed
model = LinearRegression()
t_np = np.array(t_adjusted)
# Reshape to NumPy array
t_reshaped = t_np.reshape(-1, 1)

# Fitting the model
model.fit(t_reshaped, distance)
# Getting the speed (gradient)
gradient = model.coef_[0]

print(gradient)
