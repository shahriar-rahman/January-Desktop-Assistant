from pynput.keyboard import Key, Controller
import webbrowser;
from time import *;
import time;
import os;
from playsound import playsound;
keyboard = Controller();
from pynput.mouse import Button, Controller
mouse = Controller();
#import keyboard
from tkinter import *;
# Read pointer position
#print('The current pointer position is {0}'.format(mouse.position))

# Set pointer position
#mouse.position = (416, 1058) #CLOSING POSITION
#keyboard.press(Key.caps_lock);
#keyboard.release(Key.caps_lock);
#mouse.press(Button.left)
#mouse.release(Button.left)
#outlook (1727, 100)
#print('Now we have moved it to {0}'.format(mouse.position))

# Move pointer relative to current position
#mouse.move(5, -5)

# Press and release
#mouse.press(Button.left)
#mouse.release(Button.left)

# Double click; this is different from pressing and releasing

# Scroll two steps down
#mouse.scroll(0, 2)
import psutil;
import subprocess;
# gives a single float value
print("Helllo");
# gives an object with many fields
print(psutil.virtual_memory())
# you can convert that object to a dictionary
dict(psutil.virtual_memory()._asdict())
import sys
SpokenWords="Need a reminder in 22 hours in 5 minutes";
print(str(time.strftime("%H:%M:%S")));

from tkinter import *




#os.system("TASKKILL /f /im Activation.pyw")
#TASKKILL /F /IM "program_name.exe"

