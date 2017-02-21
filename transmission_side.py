import serial
import struct
import binascii
from time import sleep
port = "COM4"
ser = serial.Serial(port, 9600)
while True:
    data = raw_input('Enter the data...')
    final = ('s'+data)
    #final = (without_end+'e')
    #print final
    out = bin(int(binascii.hexlify(final),16))
    orig=out[2:]
    #print orig
    d = ('0'+orig)
    #print d
    size = len(d)
    for i in range (0,size,1):
        send = ser.write (d[i])
        ser.read()
        #print d[i]
    ser.write('e')
    ser.read()
