## This script extracts time descriptors from the input signal.
## extract_features(x) -> x is a numpy array of shape (3,N), where N is the number of samples
## and 3 represents the axes: x, y, z. For each axis 7 features are extracted
## The functions returns a numpy array of shape (21, )

import numpy as np
from scipy.stats import skew

def standard_deviation(x):
    return np.std(x, axis=0)

def root_mean_squared(x):
    return np.sqrt(np.mean(np.square(x)))

def skewness(x):
    return skew(x)

def waveform_length(x):
    return np.sum(np.abs(np.diff(x)))

def mean_absolute_value(x):
    return np.mean(np.abs(x))
def zero_crossing_rate(x):
    arr = np.nonzero(np.diff(x > 0))[0]
    return len(arr)

def slope_sign_changes(x):
    idx1 = np.diff(x)
    arr = np.nonzero(np.diff(idx1 > 0))[0]
    return len(arr)

def extract_features(x):
    arr = np.zeros((3, 7))
    for index in range(3):
        arr[index][0] = standard_deviation(x[index])
        arr[index][1] = root_mean_squared(x[index])
        arr[index][2] = skewness(x[index])
        arr[index][3] = zero_crossing_rate(x[index])
        arr[index][4] = waveform_length(x[index])
        arr[index][5] = mean_absolute_value(x[index])
        arr[index][6] = slope_sign_changes(x[index])
    arr1 = arr.flatten()
    return arr1
