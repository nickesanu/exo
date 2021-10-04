import numpy as np
from extragere_features import extract_features

data = np.load("numpy_data.npy", allow_pickle=True)
print(data.shape)
label = np.load("label.npy")
print(label.shape)
num_id = np.load("id_subiecti.npy")
print(num_id.shape)

num_ex = data.shape[0]
num_sam = int(data.shape[1]/3)


data = data.reshape((num_ex, 3, num_sam))
data = np.transpose(data, (0, 2, 1))
# 104 * 27975 * 3
data = data.reshape((num_ex, int(num_sam/1119), 1119, 3))
# 104 * 25 * 1119 * 3
data2 = np.zeros((num_ex, 25, 21))
label2 = np.zeros((num_ex, 25))


# for i in range(num_ex):
#     label2[i] = label[i]
#     num_id2 = num_id[i]

for i in range(num_ex):
    for j in range(25):
        data2[i][j] = extract_features(np.transpose(data[i][j]))

print(data2.shape)
# the data is split like this: 80% of the users are used for training and 20% are used for validation
id_train = list(map(int, input("introduceti id subiectilor pentru train(9): ").split()))
id_val = list(map(int, input("introduceti id subiectilor pentru val(3): ").split()))
# one csv file is kept for test
id_test = int(input("introduceti id subiectilor pentru test(1): "))

train_data = np.zeros((len(id_train) * 8, 25, 21))
train_label = np.zeros((len(id_train) * 8, 25))
val_data = np.zeros((len(id_val) * 8, 25, 21))
val_label = np.zeros((len(id_val) * 8, 25))
test_data = np.zeros((8, 25, 21))
test_label = np.zeros((8, 25))


contor_t = 0
contor_v = 0
contor_test = 0
for i in range(num_ex):
    if num_id[i] in id_train:
        train_data[contor_t] = data2[i]
        train_label[contor_t] = label[i]
        contor_t += 1
    elif num_id[i] in id_val:
        val_data[contor_v] = data2[i]
        val_label[contor_v] = label[i]
        contor_v += 1
    else:
        test_data[contor_test] = data2[i]
        test_label[contor_test] = label[i]
        contor_test += 1

train_data = train_data.reshape((len(id_train) * 8 * 25, 21))
train_label = train_label.reshape((len(id_train) * 8 * 25, 1))
val_data = val_data.reshape((len(id_val) * 8 * 25, 21))
val_label = val_label.reshape((len(id_val) * 8 * 25, 1))
test_data = test_data.reshape((8 * 25, 21))
test_label = test_label.reshape((8 * 25, 1))

# save the obtained data in .npy format
np.save("train_data_dif", train_data)
np.save("val_data_dif", val_data)
np.save("train_label_dif", train_label)
np.save("val_label_dif", val_label)
np.save("test_data_dif", test_data)
np.save("test_label_dif", test_label)
