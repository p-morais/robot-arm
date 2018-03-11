from time import sleep
import serial

ser = serial.Serial('/dev/tty.usbserial-A4VBILTY', 9600) # Establish the connection on a specific port
counter = 32 
i = 1

while True:
    counter += i
    ser.write((str(counter)).encode('ascii')) # Convert the decimal number to ASCII then send it to the Arduino
    print(ser.readline().decode('ascii'),end="") # Read the newest output from the Arduino
    
    sleep(.01) # Delay for one tenth of a second
    if counter == 127 or counter == 0:
        i = -i