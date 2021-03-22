import matplotlib.pyplot as plt
import pandas as pd
from math import pi


data = pd.read_csv('Stat1.csv', header=1)
gyro_x = data[' Gyro_x [dps]']
gyro_y = data[' Gyro_y [dps]']
gyro_z = data[' Gyro_z [dps]']
accel_x = data[' Accel_x [g]']
accel_y = data[' Accel_y [g]']
accel_z = data[' Accel_z [g]']
time = data['Time[s]']


# multiple line plots
plt.style.use('fivethirtyeight')
f, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(time, accel_x, marker='', markerfacecolor='blue', color='skyblue',
         linewidth=1, label="accel_x")
ax1.plot(time, accel_y, marker='', color='olive', linewidth=1, label="accel_y")
ax1.plot(time, accel_z, marker='', color='red', linewidth=1, linestyle='dashed', label="accel_z")

ax1.legend()

ax1.set_xlabel("time [s]")
ax1.set_ylabel("Acceleration [g]")

ax2.plot(time, gyro_x * pi / 180, marker='', markerfacecolor='blue', color='skyblue',
         linewidth=1, label="gyro_x")
ax2.plot(time, gyro_y * pi / 180, marker='', color='olive', linewidth=1, label="gyro_y")
ax2.plot(time, gyro_z * pi / 180, marker='', color='red', linewidth=1, linestyle='dashed', label="gyro_z")

ax2.set_xlabel("time [s]")
ax2.set_ylabel("Gyro [rps]")

# show legend
ax2.legend()

# show graph
plt.tight_layout()
plt.show()
