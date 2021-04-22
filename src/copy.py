#!/data/data/com.termux/files/usr/bin/python

import os, sys
import subprocess as sp

clipboard = "/data/data/com.termux/files/usr/bin/termux-clipboard-set"
api = "/data/data/com.termux.api"

red = "\033[31m"
green = "\033[32m"
off = "\033[0m"

def error(msg):
    print(red + 'Error: ' + off + msg)
    print(green + 'Usage: ' + off + 'copy <file>')
    sys.exit(1)

def success(msg):
    print(green + msg + off)
    sys.exit(0)

if len(sys.argv) == 1:
    error("No file specified!")
elif len(sys.argv) > 2:
    error("Too many arguments!")
else:
    file = sys.argv[1]
    if os.path.exists(api) and os.path.exists(clipboard):
        if os.path.isfile(file):
            cmd = sp.run(["cat",file], universal_newlines=True, capture_output=True)
            file_cont = cmd.stdout
            sp.run(["termux-clipboard-set",file_cont])
            success("Successfully copied file content to clipboard")
        elif os.path.isdir(file):
            error(green + file + off + " is a directory")
        else:
            error(red + file + off + " doesn\'t exist")
    elif not os.path.exists(api):
        error("Termux:Api app is not installed. Install it first")
    elif not os.path.exists(clipboard):
        print(red + "Error: " + off + "termux-api package is not installed")
        print(green + "Installing termux-api..." + off)
        sp.call(["pkg","update"])
        sp.call(["pkg","upgrade"])
        sp.call(["pkg","install","termux-api"])
        if os.path.exists(clipboard):
            success("Successfully installed termux-api. Make sure that Termux:Api is installed and try again.")
        else:
            print(red + "Failed to install termux-api" + off)
