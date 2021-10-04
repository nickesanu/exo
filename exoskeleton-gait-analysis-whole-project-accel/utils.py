from imports import *

gyro_x = []
gyro_y = []
gyro_z = []
accel_x = []
accel_y = []
accel_z = []
time = []
# in 'for' use some sort of map function
with open('test1.csv', 'r') as stat_csv:
    plots = csv.reader(stat_csv, delimiter=';')
    for column in plots:
        time.append(column[9])
        gyro_x.append(column[1])
        gyro_y.append(column[2])
        gyro_z.append(column[3])
        accel_x.append(column[4])
        accel_y.append(column[5])
        accel_z.append(column[6])


time = list(map(lambda x: float(x), time[2:]))
gyro_x = list(map(lambda x: float(x) * math.pi / 180, gyro_x[2:]))
gyro_y = list(map(lambda x: float(x) * math.pi / 180, gyro_y[2:]))
gyro_z = list(map(lambda x: float(x) * math.pi / 180, gyro_z[2:]))
accel_x = list(map(lambda x: float(x), accel_x[2:]))
accel_y = list(map(lambda x: float(x), accel_y[2:]))
accel_z = list(map(lambda x: float(x), accel_z[2:]))

# multiple line plots
f, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(time, accel_x, marker='', markerfacecolor='blue', color='skyblue',
         linewidth=1, label="accel_x")
ax1.plot(time, accel_y, marker='', color='olive', linewidth=1, label="accel_y")
ax1.plot(time, accel_z, marker='', color='red', linewidth=1, linestyle='dashed', label="accel_z")

ax1.legend()

ax1.set_xlabel("time [s]")
ax1.set_ylabel("Acceleration [g]")

ax2.plot(time, gyro_x, marker='', markerfacecolor='blue', color='skyblue',
         linewidth=1, label="gyro_x")
ax2.plot(time, gyro_y, marker='', color='olive', linewidth=1, label="gyro_y")
ax2.plot(time, gyro_z, marker='', color='red', linewidth=1, linestyle='dashed', label="gyro_z")

ax2.set_xlabel("time [s]")
ax2.set_ylabel("Gyro [rps]")

# show legend
ax2.legend()

# show graph
plt.show()
