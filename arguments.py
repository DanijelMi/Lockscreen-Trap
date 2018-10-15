import argparse
parser = argparse.ArgumentParser(
    usage='%(prog)s [options]', 
    formatter_class=argparse.ArgumentDefaultsHelpFormatter, 
    description="Locks the system and captures a webcam photo as soon as user input is detected.",
    epilog="Example: %(prog)s PARAMS_LEL")
parser.add_argument('-p', '--path', default='./', help='File path to captured images')
parser.add_argument('-t', '--arm-time', type=int, default=5, help='Seconds before activating')
parser.add_argument('-n','--no-video', dest='accumulate', action='store_const',
                    const=sum, default=max, help='Disables the image capturing')
args = parser.parse_args()
