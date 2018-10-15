import sys, subprocess
from threading import Thread    #
import pynput.mouse as ms       #
import pynput.keyboard as kb    #
from time import gmtime, strftime, sleep

SCREENSHOT_DIR = "/home/danijel/desktop"

sleep(1)     # Seconds of waiting before starting the script

def bash_command(cmd):                              # 
    subprocess.Popen(['/bin/bash', '-c', cmd])      #

def on_action(*args):                               # Gets called when a keyboard
   sys.exit()                                       # or mouse press happens

def keyboard_listen():                      # Defines a listener for keyboard
    with kb.Listener(                       # presses
            on_press=on_action) as listener:
        listener.join()

def mouse_listen():                         # Defines a listener for mouse
    with ms.Listener(                       # presses
            on_click=on_action) as listener:
        listener.join()

t_kb=Thread(target=keyboard_listen, args=())# Sets the listener on a new thread.
t_kb.setDaemon(True)                        # Daemons get killed if the caller (main) process
t_kb.start()                                # gets killed.

t_ms=Thread(target=mouse_listen, args=())   # Sets the listener on a new thread.
t_ms.setDaemon(True)                        # Daemons get killed if the caller (main) process
t_ms.start()                                # gets killed.

while(t_kb.isAlive() and t_ms.isAlive()):   # If either thread died, then a mouse/keyboard event
    sleep(1)                           # triggered. Therefore stop checking and exit loop


#captureCommand = "mplayer -vo jpeg:outdir=/var/www/html -frames 1 tv://"
captureCommand = "mplayer -vo jpeg:outdir={}/{} -frames 1 tv://"
captureCommand = captureCommand.format(SCREENSHOT_DIR, strftime("%Y-%m-%d_%H-%M-%S", gmtime()))
print(captureCommand)
#bash_command(captureCommand)
#bash_command("mplayer -vo png -frames 1 tv://")
#bash_command("loginctl lock-session")

sys.exit()                                  # Closes main process and its daemons too.
