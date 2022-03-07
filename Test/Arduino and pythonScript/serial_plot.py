import serial as ser
import matplotlib.pyplot as myplot
import numpy as np

port = '/dev/ttyACM0'
baud = 9600

s = ser.Serial(port,baud)
s.close()
s.open()
myplot.close('all')
myplot.figure()
myplot.ion()
myplot.show()

dataset = np.array([])

while True:

    datainbinary = s.readline().decode()
    data = float(datainbinary[:-2])

    dataset = np.append(dataset , data)
    myplot.cla()
    myplot.plot(dataset)
    myplot.pause(0.0001)

   