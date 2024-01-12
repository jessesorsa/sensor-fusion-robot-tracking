Sensor fusion course project
Tracking a mobile robot

Calibration:
In acceleration_calibration, gyroscope_calibration, IMU is calibrated and the biases are calculated to accurately track the
position of the robot. In speed folder, the speed of the robot is calculated when 30% PWM is applied (constant speed).

Tracking:
In imu_tracking
The used dynamic model for the mobile robot is: reduced quasi-constant turn model. It requires the gyroscope and speed values
as inputs. The model is discretised, and the position values calculated, using Euler approximation.
