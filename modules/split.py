import os
import os.path
import configparser
import codecs
import platform
import shutil
import subprocess

if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()
if os.path.exists("split"):
    shutil.rmtree("split")
if not os.path.exists("split"):
    os.makedirs("split")
print("You selected split")
config = configparser.ConfigParser()
config.read_file(codecs.open('configs/config.ini', "r", encoding="ISO-8859-1"))
inputfile = input("File that you would like to split: ")
splitLen = int(input("How many lines each split: "))
if not os.path.isfile(inputfile):
    print("Input file not found")
else:
    f = open(inputfile)
    if os.stat(inputfile).st_size < 1:
        print("input file is empty.")
    else:
        count = 0
        at = 0
        for line in f:
            if count % splitLen == 0:
                dest = open("split/split_" + str(at) + '.txt', 'w+')
                at += 1
            dest.write(line)
            count += 1
        print("Splitting done!")
            
input("Press enter to continue...")
if platform.system() == "Linux":
    p = subprocess.call(["python3", "start.py"])
if platform.system() == "Windows":
    p = subprocess.call(["python", "start.py"])