# Pico

Simple two-way serial communication between a Raspberry Pi Pico and any Pi or PC without additional hardware:

Raspbery Pi Pico code demonstrating USB serial communication. It's nothing fancy.
One files goes on the Pico (as main.py or run it from Thonny),
The other file -you guessed it- is ran on the host.

I'm using a Pimorini Pi Display in this demo, but the code can be used for anything really.

For more information see the comments in the Python and MicroPython file. I'm not much of a programmer, the code could be cleaned up and is hacked together from other example code like the button.py script Pimorini provides for the Pico Display.

If you are on Windows, be sure to check the serial port on line 12 in the host file as in the code it's dev/ttyACM0 for a Linux machine.

Note: If you run the Pico code from Thonny, it wil complain it loses communication with the board after running the host script, but that doesn't stop anything from functioning. If anything the host code runs better after Thonny loses the connection. But putting the Pico code on the Pico as main.py would look more professional I guess. All in all this is really just a crude introduction to serial communication between board and host.
