import serial
from time import sleep
import binascii

port = "COM5"
ser = serial.Serial(port, 9600, timeout=0)
data1='0'
while True:
        data = ser.read()
        if data=='e':
            break
        elif len(data) > 0:
            #print 'data received =',data
            data1 = (data1+data)
            next_bit = ser.write('1')
        
        else:   
                sleep(0.01)
                print 'no data'

#print 'The data is',data1
ser.write('1')
c='%08X' % int(data1, 2)
z=binascii.unhexlify(c)
#print z
p=len(z)
x=z[1:p]
print 'Complete data====>  ',x
