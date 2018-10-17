import sys, subprocess
from threading import Thread
import pynput.mouse as ms
import pynput.keyboard as kb
from time import gmtime, strftime, sleep
import argparse

def parseArgs():
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options]', 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter, 
        description="Locks the system and captures a webcam photo as soon as user input is detected.",
        epilog="Example: %(prog)s -t 3 -p /home/user/Desktop")
    parser.add_argument('-v', '--verbose', action='store_const',
                        const=True, default=False, help='For debugging purposes.')
    parser.add_argument('-l', '--no-lock', action='store_const',
                        const=True, default=False, help='Disables locking')
    parser.add_argument('-n','--no-video', action='store_const',
                        const=True, default=False, help='Disables image capturing')
    parser.add_argument('-p', '--path', default='./', help='File path to captured images')
    parser.add_argument('-t', '--arm-time', type=int, default=3, help='Seconds before activating')
    parser.add_argument('-c', '--command', nargs=argparse.REMAINDER, help='Executes custom command at the end')
    args = vars(parser.parse_args())
    return args['verbose'], args['no_lock'], args['no_video'], args['path'], args['arm_time'], args['command']


args=parseArgs()
print(args)

# Takes all arguments for -c command and concatinate them into a single string
customCommand = ''
if args[5]:
    for i in args[5]:
        customCommand += str(i) + ' '

sleep(args[4])       # Seconds of waiting before starting/arming the script

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


captureCommand = "mplayer -vo jpeg:outdir={}/{} -frames 1 tv://".format(args[3], strftime("%Y-%m-%d_%H-%M-%S", gmtime()))
print(captureCommand)
bash_command(captureCommand) if not args[2] else False          # Captures image
bash_command("loginctl lock-session") if not args[1] else False # Locks session
bash_command(customCommand) if customCommand else False         # Executes custom command
sys.exit()                                  # Closes main process and its daemons too.
