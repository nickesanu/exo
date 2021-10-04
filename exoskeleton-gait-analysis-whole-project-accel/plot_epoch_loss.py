#### This script plots the epoch loss and accuracy for the training and validation set

import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator
import seaborn

path_train = 'logs\log20210513-131602 dif_user\\train\events.out.tfevents.1620900962.DESKTOP-UGRFP2C.22348.235.v2'
path_val = 'logs\log20210513-131602 dif_user\\validation\events.out.tfevents.1620900964.DESKTOP-UGRFP2C.22348.1441.v2'


event_train = EventAccumulator(path_train)
event_train.Reload()

event_val = EventAccumulator(path_val)
event_val.Reload()


acc_train = []
for scalar in event_train.Scalars('epoch_accuracy'):
    acc_train.append(scalar.value)
acc_train = np.asanyarray(acc_train)


acc_val = []
for scalar in event_val.Scalars('epoch_accuracy'):
    acc_val.append(scalar.value)
acc_val = np.asanyarray(acc_val)


loss_train = []
for scalar in event_train.Scalars('epoch_loss'):
    loss_train.append(scalar.value)
loss_train = np.asanyarray(loss_train)


loss_val = []
for scalar in event_val.Scalars('epoch_loss'):
    loss_val.append(scalar.value)
loss_val = np.asanyarray(loss_val)



x_axis = np.linspace(0, len(acc_train), num=len(acc_train))

my_signals = [{'name': '', 'x': x_axis,
    'y': acc_train, 'color':'r', 'linewidth':2},
    
    {'name': '', 'x': x_axis,
    'y': acc_val, 'color':'b', 'linewidth':2}]

my_signals1 = [{'name': '', 'x': x_axis,
               'y': loss_train, 'color': 'r', 'linewidth': 2},

              {'name': '', 'x': x_axis,
               'y': loss_val, 'color': 'b', 'linewidth': 2}]


fig, ax = plt.subplots()


for signal in my_signals:
    ax.plot(signal['x'], signal['y'],
            color=signal['color'],
            linewidth=signal['linewidth'],
            label=signal['name'])

    ax.legend()
    ax.set_title('Train evolution')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Accuracy')
    ax.grid(True, which='both')
    ax.set_xlim(0)
    ax.set_ylim(0)
    seaborn.despine(ax=ax, offset=0)

fig1, ax1 = plt.subplots()

for signal in my_signals1:
    ax1.plot(signal['x'], signal['y'],
            color=signal['color'],
            linewidth=signal['linewidth'],
            label=signal['name'])

    ax1.legend()
    ax1.set_title('Train evolution')
    ax1.set_xlabel('Iteration')
    ax1.set_ylabel('Loss')
    ax1.grid(True, which='both')
    ax1.set_xlim(0)
    ax1.set_ylim(0)
    seaborn.despine(ax=ax1, offset=0)
plt.show()

