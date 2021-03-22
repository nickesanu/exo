import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
from math import pi

plt.style.use('fivethirtyeight')


def animate(i):
    data = pd.read_csv('Stat1.csv', header=1)
    gyro_x = data[' Gyro_x [dps]']
    time = data['Time[s]']
    plt.cla()
    plt.plot(time, gyro_x * pi / 180)
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)  # refresh rate of the plot/ still plots all the values

plt.tight_layout()
plt.show()
