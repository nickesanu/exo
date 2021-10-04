## This script is used for UART communication with an STM32 microcontroller, the data received is written into a CSV.
## The microcontroller receives accelerometer and gyroscope data, on all three axes, through SPI.
## Then the data is sent to the Raspberry Pi 4. Here the data is written into a CSV as follows:
## For each subject we conducted two sets of tests, each set containing four types of activity:
## standing still (0), walking (1), running (2) and climbing stairs(3).
## Each activity represents a class, written in the paranthesis.

import serial
import re
from datetime import datetime

timer = float(input("Seconds for data acquisition >>>"))

#Initializing UART
ser = serial.Serial('/dev/ttyAMA0',115200,timeout = 1, parity = serial.PARITY_NONE, rtscts = 0, stopbits=1, xonxoff = 0)
print(ser.name)
test = ser.readline()

#Name of csv: class_subjectID_i_noOfTrial
filename = "0_018_i_1.csv"
fId = open(filename, 'a')

tac = datetime.today()
tic = datetime.today()
dif = tic - tac
count1 = 1
string="Index, Gyro_x [dps], Gyro_y [dps], Gyro_z [dps], Accel_x [g], Accel_y [g], Accel_z [g], Time[s]\n"
fId.write(string)
while timer > dif.total_seconds():
	concatString = str(count1)
	test = str(ser.readline())
	splitText = test.split(",")
	for i in range(len(splitText)):
		onlyInt = re.sub("[^0-9-]", "", splitText[i])
		if i<3:
			onlyInt = str(int(onlyInt)*0.070)
		elif i >= 3 and  i<6:
			onlyInt = str(int(onlyInt) * 0.00048828125/2)
		concatString = concatString + ',' + onlyInt
	tic1 = datetime.today()
	dif1 = tic1 - tac
	onlyInt = str(dif1.total_seconds())
	concatString = concatString + ',' + onlyInt
	concatString = concatString + '\n'
	tic = datetime.today()
	dif = tic - tac
	if test == "b''":
		continue
	if test == '':
		continue
	count1 = count1 + 1
	fId.write(concatString)
	print(test)

fId.close()
ser.close()
