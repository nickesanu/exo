import tensorflow as tf
import numpy as np
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

dif_user = False

if dif_user:

    path = 'data_val_diff_user/'
    train_data = np.load(path + "train_data_dif.npy")
    train_label = np.load(path + "train_label_dif.npy")
    train_label = to_categorical(train_label, 4)
    val_label = np.load(path + "val_label_dif.npy")
    val_label = to_categorical(val_label, 4)
    val_data = np.load(path + "val_data_dif.npy")
    test_data = np.load(path + "test_data_dif.npy")
    test_label1 = np.load(path + "test_label_dif.npy")
    test_label = to_categorical(test_label1, 4)
else:
    path = 'data_val_same_user/'
    train_data = np.load(path + "train_data.npy")
    train_label = np.load(path + "train_label.npy")
    train_label = to_categorical(train_label, 4)
    val_label = np.load(path + "val_label.npy")
    val_label = to_categorical(val_label, 4)
    val_data = np.load(path + "val_data.npy")
    test_data = np.load(path + "test_data.npy")
    test_label1 = np.load(path + "test_label.npy")
    test_label = to_categorical(test_label1, 4)


all_data = np.concatenate((train_data, val_data, test_data), axis=0)
print(all_data.shape)
scaler1 = StandardScaler()
all_data = scaler1.fit_transform(all_data)

train_data = all_data[:train_data.shape[0]]
val_data = all_data[train_data.shape[0]:train_data.shape[0] + val_data.shape[0]]
test_data = all_data[train_data.shape[0] + val_data.shape[0]:]

if __name__ == '__main__':

    ###PCA Visualization of features
    pca = PCA(n_components=2)
    decomposed_data = pca.fit_transform(train_data)
    print(decomposed_data.shape)
    print(train_data.shape)

    colors = ['purple', 'red', 'black', 'green']
    genres_label = ['Standing', 'Walking', 'Running', 'Stairs']
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = [], [], []
    for i in range(4):
        x = decomposed_data[int(decomposed_data.shape[0]/4) * i:int(decomposed_data.shape[0]/4) * (i + 1), 0]
        y = decomposed_data[int(decomposed_data.shape[0]/4) * i:int(decomposed_data.shape[0]/4) * (i + 1), 1]
        z = i * np.ones(int(decomposed_data.shape[0]/4))
        ax.scatter(x, y, z, c=colors[i], label=genres_label[i])
    ax.set_xlabel("1st principal component")
    ax.set_ylabel("2nd principal component")
    ax.set_zlabel("Types of movement")
    ax.set_zticklabels([])
    # plt.legend(bbox_to_anchor=(1, 0.5),loc="center right")
    plt.legend()
    plt.show()