
import serial
import asyncio
from serial.serialutil import SerialException
from time import sleep
from datetime import datetime

# modified from https://blog.rareschool.com/2021/01/controlling-raspberry-pi-pico-using.html
class SerialSender:
    TERMINATOR = '\n'.encode('UTF8')

    def __init__(self, device='/dev/ttyACM0', baud=115200, timeout=1):
        self.serial = serial.Serial(device, baud, timeout=timeout)

# The magic happens in this part. Basically we find out which button was pressed
# on the Pimorini Pico Display by receiving and evaluating the serial input.
# The commented out print statements can be use for more verbose output
# some repeating code here, what can I say, I'm lazy and not a good programmer.
    def receive(self) -> str:
        cc=str(self.serial.readline())
        ll = len(cc)
        if ll > 3: # this could probably be zero instead of three
          #print(cc[2:][:-5])
          #print(cc)
          if cc.find("A") != -1:
            print("Button A pressed")
            burp = "Button A pressed"
            serial_sender = SerialSender()
            serial_sender.send(burp)
            serial_sender.close
          elif cc.find("B") != -1:
            print("Button B pressed")
            burp = "Button B pressed"
            serial_sender = SerialSender()
            serial_sender.send(burp)
            serial_sender.close
          elif cc.find("X") != -1:
            print("Button X pressed")
            burp = "Button X pressed"
            serial_sender = SerialSender()
            serial_sender.send(burp)
            serial_sender.close
          elif cc.find("Y") != -1:
            print("Button Y pressed")
            burp = "Button Y pressed"
            serial_sender = SerialSender()
            serial_sender.send(burp)
            serial_sender.close
	
    def send(self, text: str):
        line = '%s\n' % text
        self.serial.write(line.encode('UTF8'))

    def close(self):
        self.serial.close()

x = 1

#show a ready message on the Pico Display. It's this easy to send any message to it.
burp = "Host ready"
serial_sender = SerialSender()
serial_sender.send(burp)
serial_sender.close
sleep(2) # isn't actually needed, but shows the 'Host Ready' message for a bit, also if the clock demo below is active

while x < 2:
	#You can uncomment the three lines below to see a clock demonstration.
	#now = datetime.now() # current date and time
	#burp = now.strftime("%H:%M")
	serial_sender = SerialSender()
	#serial_sender.send(burp)
	serial_sender.receive()
	serial_sender.close()
	sleep(1) # give the pico some room to breathe, or it will suffocate itself



