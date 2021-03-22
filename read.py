import serial
import re
import msvcrt
from datetime import datetime

ser = serial.Serial('COM5', 115200, timeout=1, parity=serial.PARITY_NONE, rtscts=0, stopbits=1, xonxoff=0)
print(ser.name)         # check which port was really used
test = ser.readline()
j=0
Vref = 3.3
Vlsb = float(Vref/pow(2,23))
scaleFacotr = 32768

fileName = "Stat1.csv"

print("Press s to start logging session")
print("Press e to exit the logging session")

input1 = 'N'
while (input1 != "b's'"):
     if msvcrt.kbhit():
        input1 = str(msvcrt.getch())

fId = open(fileName,"a")
today = datetime.today()
t=datetime.now().strftime('%M.%f')
dt_string = today.strftime("DATE,%d/%m/%Y,TIME,%H:%M:%S\n")
fId.write(dt_string)
string = "Index, Gyro_x [dps], Gyro_y [dps], Gyro_z [dps], Accel_x [g], Accel_y [g], Accel_z [g], Pressure [kg],,Time[s]\n"
fId.write(string)
time = 1
while(input1 != "b'e'"):
    if msvcrt.kbhit():
        input1 = str(msvcrt.getch())
    test = str(ser.readline())
    splitText = test.split(",")
    concatString = str(time)
    for i in range(len(splitText)):
        onlyInt = re.sub("[^0-9-]", "", splitText[i])
        if (i < 3):
            onlyInt = str(int(onlyInt)* 0.070)
        elif (i >= 3 and i < 6):
            onlyInt = str(int(onlyInt) * 0.00048828125)
        elif (i>=6 and i<=7):
            onlyInt = str((float((int(onlyInt)))*Vlsb/32768)*(5/0.00375))
        else:
            #t1 = datetime.today().strftime('%S.%f')
            #onlyInt = str(float(t1)-float(t))
            today1=datetime.today()
            dif=today1-today
            onlyInt=str(dif.total_seconds())
        concatString = concatString + ',' + onlyInt
    concatString = concatString + '\n'
    print(concatString)
    fId.write(concatString)
    time = time + 1

fId.close()  
ser.close()             # close port
