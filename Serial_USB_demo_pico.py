# A simple script demonstrating serial communication over USB
# This example uses a Pimorini Pico Display, but will work with anything of course

# Imports, obviously you won't need the first one if you don't use a pico display
import picodisplay as display  
import utime
import uselect
from sys import stdin, exit

# how serial lines are ended
TERMINATOR = "\n"

# Initialise display with a bytearray display buffer
buf = bytearray(display.get_width() * display.get_height() * 2)
display.init(buf)
display.set_backlight(0.5)

# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(0, 0, 0)
    display.clear()
    display.update()
    
def read_serial_input():
        """
        Buffers serial input.
        Writes it to input_line_this_tick when we have a full line.
        Clears input_line_this_tick otherwise.
        """
        buffered_input = ""
        global input_line_this_tick
        input_line_this_tick =""
        # stdin.read() is blocking which means we hang here if we use it. Instead use select to tell us if there's anything available
        # note: select() is deprecated. Replace with Poll() to follow best practises
        select_result = uselect.select([stdin], [], [], 0)
        while select_result[0]:
            # there's no easy micropython way to get all the bytes.
            # instead get the minimum there could be and keep checking with select and a while loop
            input_character = stdin.read(1)
            # add to the buffer
            buffered_input = buffered_input + input_character
            # check if there's any input remaining to buffer
            select_result = uselect.select([stdin], [], [], 0)
        # if a full line has been submitted
        if TERMINATOR in buffered_input:
            line_ending_index = buffered_input.index(TERMINATOR)
            # make it available
            input_line_this_tick = "".join(buffered_input[:line_ending_index])
            # remove it from the buffer.
            # If there's remaining data, leave that part. This removes the earliest line so should allow multiple lines buffered in a tick to work.
            # however if there are multiple lines each tick, the buffer will continue to grow.
            if line_ending_index < len(buffered_input):
                buffered_input = buffered_input[line_ending_index + 1 :]
            else:
                buffered_input = []
        # otherwise clear the last full line so subsequent ticks can infer the same input is new input (not cached)
        else:
            input_line_this_tick = ""


#signal to the user the pico is ready for action
clear()                                           # clear to black
display.set_pen(255, 255, 255)                    # change the pen colour
display.text("Pico ready", 10, 10, 240, 4)  # display some text on the screen
display.update()

#check for possible button presses and for possible serial input.
#Of course we could directly update the display from here, but where's the fun in that?
#See also the clock demo in the host script.
#But the point of this demo is showing the host computer can do the messaging. That's what the 'else' part does.
while True:
    if display.is_pressed(display.BUTTON_A):  # if a button press is detected then...
        print("A")
    elif display.is_pressed(display.BUTTON_B):
        print("B")
    elif display.is_pressed(display.BUTTON_X):
        print("X")
    elif display.is_pressed(display.BUTTON_Y):
        print("Y")
    else:
        #clear the display
        display.set_pen(255, 0, 0)
        display.text("", 10, 10, 240, 4)
        display.update()
        #wait a bit
        utime.sleep(0.1)  # this number is how frequently the Pico checks for button presses (and for serial input)
        read_serial_input()
        #and... check for serial input, if there is any, show it on the display
        if input_line_this_tick:
                clear()
                display.set_pen(255, 255, 0)
                latest_input_line = input_line_this_tick
                display.text(latest_input_line, 10, 10, 240, 4)
