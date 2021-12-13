import os
import sys
from time import sleep as WAIT
from send2trash import send2trash as DISCARD
import subprocess
import shutil
import tempfile
import keyboard

def LOG(msg):
    print(msg)
    sys.stdout.flush()

def MKDIR(path):
    if not os.path.exists(path):
        os.makedirs(path)

def MKDIR_F(path):
    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=True)
    os.makedirs(path)

def DELETE(path):
    if not os.path.exists(path):
        raise Exception("File or folder does not exist: " + path)
    if os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.isfile(path):
        os.remove(path)

def EXIT():
    sys.exit(0)

def COPY(src, dst):
    with open(src, 'rb') as f:
        with open(dst, 'wb') as g:
            g.write(f.read())

def MOVE(src, dst):
    shutil.move(src, dst)

def GETPTH(path):
    return os.path.expandvars(path)

def GETCWD():
    return os.getcwd()

def RUNCMD(cmd):
    subprocess.Popen(cmd, shell=True)

def RUNCMD_w(cmd):
    subprocess.run(cmd, shell=True, timeout=60)

def CD(path):
    os.chdir(path)

def PWD():
    return os.getcwd()

def CD_UP():
    os.chdir("..")

def CD_HOME():
    os.chdir(os.path.expanduser("~"))

def CD_TEMP():
    os.chdir(tempfile.gettempdir())

def KP(keys):
    keyboard.write(keys)

def OPEN(path):
    os.startfile(path)
