import numpy as np
from extragere_features import extract_features

data = np.load("numpy_data.npy", allow_pickle=True)  # load the data we prev obtained
print(data.shape)
label = np.load("label.npy")
print(label.shape)
num_id = np.load("id_subiecti.npy")
print(num_id.shape)

num_ex = data.shape[0]  # get the number of csv files, first dimension
num_sam = int(data.shape[1]/3)  # get the number of samples

data = data.reshape((num_ex, 3, num_sam))
# reshape the array: number of files * number of axis (x, y, z) * number of samples
data = np.transpose(data, (0, 2, 1))
# 104 * 27975 * 3
data = data.reshape((num_ex, int(num_sam/1119), 1119, 3))
# number of files * number of 3 sec windows * number of samples per 3 sec window * number of axis
# 104 * 25 * 1119 * 3
data2 = np.zeros((num_ex, 25, 21))
label2 = np.zeros((num_ex, 25))

for i in range(num_ex):
    label2[i] = label[i]


for i in range(num_ex):
    for j in range(25):
        data2[i][j] = extract_features(np.transpose(data[i][j]))

print(data2.shape)

train_data = np.zeros((num_ex - 8, 20, 21))
# the data is split like this: 80% of every csv file is used for training and 20% is used for validation
train_label = np.zeros((num_ex - 8, 20))
val_data = np.zeros((num_ex - 8, 5, 21))
val_label = np.zeros((num_ex - 8, 5))
# one csv file is kept for test
test_data = np.zeros((8, 25, 21))
test_label = np.zeros((8, 25))

test_id = int(input("introduceti id-ul subiectului pentru test: "))
contor_tr = 0
contor_test = 0
for i in range(num_ex):
    if num_id[i][0] != test_id:
        for j in range(20):  # 20 out of 25 3 sec windows for train
            train_data[contor_tr][j] = data2[i][j]
            train_label[contor_tr][j] = label2[i][j]
        for j in range(5):  # remaining 5 for val
            val_data[contor_tr][j] = data2[i][j + 20]
            val_label[contor_tr][j] = label2[i][j + 20]
        contor_tr += 1
    else:
        test_data[contor_test] = data2[i]
        test_label[contor_test] = label2[i]
        contor_test += 1

train_data = train_data.reshape(((num_ex-8)*20, 21))
train_label = train_label.reshape(((num_ex-8)*20, 1))
val_data = val_data.reshape(((num_ex-8)*5, 21))
val_label = val_label.reshape(((num_ex-8)*5, 1))
test_data = test_data.reshape((8*25, 21))
test_label = test_label.reshape((8*25, 1))

# save the obtained data in .npy format
np.save("test_data", test_data)
np.save("test_label", test_label)
np.save("train_data", train_data)
np.save("val_data", val_data)
np.save("train_label", train_label)
np.save("val_label", val_label)
