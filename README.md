# Lockscreen-Trap

Bait the snoopers.

Small python3 script that snaps a webcam photo and locks the computer when a keyboard/mouse press is detected.
A countermeasure solution to those that are eager to pull a prank on an unlocked machine.

OS: Linux   Tested: Arch Linux (testing appreciated but should work)

Dependencies:
python3   (Most distros usually have it)  
pynput    (pip3 install pynput)           
bash      (Most distros should have it)   
mplayer   (For taking screenshots)        

Optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         For debugging purposes. (default: False)
  -l, --no-lock         Disables locking (default: False)
  -n, --no-video        Disables image capturing (default: False)
  -p PATH, --path PATH  File path to captured images (default: ./)
  -t ARM_TIME, --arm-time ARM_TIME
                        Seconds before activating (default: 3)
  -c COMMAND [COMMAND ...], --command COMMAND [COMMAND ...]
                        Executes custom command at the end (default: None)

Examples:
Arm after 10 seconds and save the image to users Desktop
  python3 Lock_Trap.py -t 10 -p /home/user/Desktop

Arm immideately and do not lock, saves the directory it is run in by default
  python3 Lock_Trap.py -t 0 -l
  
Skip capturing the frame but start playing noise
