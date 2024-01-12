import os
import matplotlib.pyplot as plt
import csv


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the CSV file
csv_file_path = os.path.join(script_dir, 'imu_calibration_task2.csv')

t = []
x = []
y = []
z = []

# get acceleration calibration data (robot is turned around)
with open('/Users/jessesorsa/Koulu/Sensor_fusion/project-code/data/acceleration_calibration/imu_calibration_task2.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        t.append(float(row[0]))
        x.append(float(row[1]))
        y.append(float(row[2]))
        z.append(float(row[3]))

# time is adjusted so it starts at 0, and x,y direction is corrected
adjusted_t = []
adjusted_x = []
adjusted_y = []
i = 0
while (i < len(t)):
    adjusted_t.append((t[i]-t[0]))
    i += 1
i = 0
while (i < len(x)):
    adjusted_x.append(-1*(x[i]))
    i += 1
i = 0
while (i < len(y)):
    adjusted_y.append(-1*(y[i]))
    i += 1

# data is plotted
plt.plot(adjusted_t, adjusted_x, color='r', label="x")
plt.plot(adjusted_t, adjusted_y, color='b', label="x")
plt.plot(adjusted_t, z, color='g', label="x")
plt.ylabel('Gravity unit')
plt.xlabel('Time (s)')
plt.title('Acceleration data')
plt.show()

# calculating biases for x,y,z directions

# robot on its side, x positive
ax_u = sum(adjusted_x[813:1056])/243
# robot on its other side, x negative
ax_d = sum(adjusted_x[1291:1594])/303
# gain kx
kx = ((ax_u)-(ax_d))/(2*9.81)
# bias bi
bx = ((ax_u)+(ax_d))/2
print(kx, bx)

# robot on its side, y positive
ay_u = sum(adjusted_y[1834:1994])/160
# robot on its other side, y negative
ay_d = sum(adjusted_y[2393:2647])/254
# gain ky
ky = ((ay_u)-(ay_d))/(2*9.81)
# bias by
by = ((ay_u)+(ay_d))/2
print(ky, by)

# robot upside down, z positive
az_u = sum(z[0:160])/161
# robot right side up, z negative
az_d = sum(z[400:608])/208
# gain kz
kz = ((az_u)-(az_d))/(2*9.81)
# bias bz
bz = ((az_u)+(az_d))/2
print(kz, bz)
