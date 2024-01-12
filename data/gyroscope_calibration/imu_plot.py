import os
import matplotlib.pyplot as plt
import csv


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the CSV file
csv_file_path = os.path.join(script_dir, 'imu_reading_task1.csv')

t = []
x = []
y = []
z = []

# get gyroscope calibration data from .csv file. The robot is stationary
with open('/Users/jessesorsa/Koulu/Sensor_fusion/project-code/data/gyroscope_calibration/imu_reading_task1.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        t.append(float(row[0]))
        x.append(float(row[6]))
        y.append(float(row[7]))
        z.append(float(row[8]))


# adjusting the time so that the it starts at 0
adjusted_t = []
i = 0
while (i < len(t)):
    adjusted_t.append(t[i]-t[0])
    i += 1

# plotting the data
plt.plot(adjusted_t, x, color='r', label="x")
plt.plot(adjusted_t, y, color='b', label="x")
plt.plot(adjusted_t, z, color='g', label="x")
plt.ylabel('Degrees')
plt.xlabel('Time (s)')
plt.title('Gyroscope data')
plt.show()

# bias calculation (skipping the first part with spikes)
x_adjusted = x[321:]
y_adjusted = y[321:]
z_adjusted = z[321:]
average_x = sum(x_adjusted)/len(x_adjusted)
average_y = sum(y_adjusted)/len(y_adjusted)
average_z = sum(z_adjusted)/len(z_adjusted)

# variance calculation
res_x = sum((i - average_x) ** 2 for i in x_adjusted) / len(x_adjusted)
res_y = sum((i - average_y) ** 2 for i in y_adjusted) / len(y_adjusted)
res_z = sum((i - average_z) ** 2 for i in z_adjusted) / len(z_adjusted)

# printing bias and variance
print(average_x, res_x)
print(average_y, res_y)
print(average_z, res_z)
