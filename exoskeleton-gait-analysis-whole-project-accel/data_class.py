import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

# get the root folder
file_name = r"D:\py_p2\date"
min1 = 40000
num_ex = len(os.listdir(file_name))

# iterate through the csv files
for f in os.listdir(file_name):
    data = pd.read_csv(file_name + "\\" + f)  # read the csv file
    length = len(data[' Accel_x [g]'])
    if length < min1:
        min1 = length  # get the minimum number of samples

print(min1)
con = np.zeros((1, 5))  # data from the csv files
label = np.zeros((num_ex, 1))  # label of each csv file
contor = 0
num_id = np.zeros((num_ex, 1))  # id for each csv file
for f in os.listdir(file_name):
    label[contor][0] = int(f[0])
    num_id[contor][0] = int(f[2:5])
    contor += 1
    data = pd.read_csv(file_name + "\\" + f)
    accel_x = np.array(data[' Accel_x [g]'])
    accel_y = np.array(data[' Accel_y [g]'])
    accel_z = np.array(data[' Accel_z [g]'])
    # timp = np.array(data[' Time[s]'])
    # a2 = accel_z
    # t2 = timp
    length = len(accel_x)
    dif = (length - min1) / 2  # the number of extra rows of each csv file compared to the previously obtained minimum
    # dif is divided by 2 so the extra rows are removed both from the start and the end of the array
    if dif != 0:
        if int(dif) != dif:  # odd number of extra rows
            dif = int(dif)
            accel_x = accel_x[dif + 1:length - dif]  # actual removal of those rows
            accel_y = accel_y[dif + 1:length - dif]
            accel_z = accel_z[dif + 1:length - dif]
            # timp = timp[dif + 1:length - dif]
        else:  # even number of extra rows
            dif = int(dif)
            accel_x = accel_x[dif:length - dif]
            accel_y = accel_y[dif:length - dif]
            accel_z = accel_z[dif:length - dif]
            # timp = timp[dif:length - dif]
    accel_x = accel_x[:27975]  # 25 * 1119 / another removal for further ease in reshaping
    accel_y = accel_y[:27975]
    accel_z = accel_z[:27975]
    sample = np.concatenate((accel_x, accel_y, accel_z))  # concatenate the 3 axis
    if not np.any(con):
        con = sample
    else:
        con = np.vstack((con, sample))  # add the sample data in an array
print(con.shape)

np.save("numpy_data", con)  # save the data in .npy format
np.save("label", label)  
np.save("id_subiecti", num_id)
print(label.shape)
print(num_id.shape)
print(num_id)
# print(timp[-1]-timp[0])
# print(num_id, num_id.shape)
# plt.style.use('fivethirtyeight')
# f, (ax1, ax2) = plt.subplots(2, 1)
# ax1.plot(timp,accel_z)
# ax2.plot(t2,a2)
# plt.show()
