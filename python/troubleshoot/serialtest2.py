import serial 
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

serial.write(b'Hello World\n')
ser.close()