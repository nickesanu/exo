#### This script is used for real-time prediction and it's running on the Raspberry Pi 4
#### Everytime the buffer is full, it computes the time descriptors and then they are fed at the input of the neural network
#### The network makes a prediction, the class is then printed

import serial
import re
import numpy as np
import tflite_runtime.interpreter as tflite
from extragere_features import extract_features
from sklearn.preprocessing import StandardScaler

# Init of serial communication
ser = serial.Serial("/dev/ttyAMA0", 115200, timeout=1, parity=serial.PARITY_NONE, rtscts=0, stopbits=1, xonxoff=0)

# Init of buffer as a list, that later should be converted to np.array
buffer = np.zeros((3,1200))

# Loading data set so we can compute locally the mean and stdev
train_data = np.load("train_data_dif.npy")
val_data = np.load("val_data_dif.npy")
test_data = np.load("test_data_dif.npy")

# Computing the mean and stdev of the dataset
all_data = np.concatenate((train_data, val_data, test_data), axis=0)
scaler1 = StandardScaler()
scaler1.fit(all_data)

while True:
	# Reading 1200 samples from UART
	for sample_no in range(1200):
		test = str(ser.readline())
		splitText = test.split(",")
		for i in range(len(splitText)):
			onlyInt = re.sub("[^0-9-]", "", splitText[i])
			if i >=3 and i < 6:
				onlyInt = int(onlyInt)*0.00048828125/2
				buffer[i-3][sample_no] = onlyInt


	# Exctracting features out of the 3 second window, reshaping it and normalizing it to the above mentioned mean and stdev
	in_data = extract_features(buffer)
	in_data = np.expand_dims(in_data,axis=0)
	in_data = scaler1.transform(in_data)
	in_data = np.array(in_data, dtype=np.float32)

	# loading the TFLite model and allocate tensors
	interpreter = tflite.Interpreter(model_path="model.tflite")
	interpreter.allocate_tensors()

	# Get input and output tensors
	input_details = interpreter.get_input_details()
	output_details = interpreter.get_output_details()

	interpreter.set_tensor(input_details[0]['index'], in_data)

	interpreter.invoke()

	output_data = interpreter.get_tensor(output_details[0]['index'])
	### Printing the predicted movement type
	print(np.argmax(output_data))
