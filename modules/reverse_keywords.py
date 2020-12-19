import re
import os
import os.path
import configparser
import codecs
import platform
import subprocess

if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()
print("You selected reverse keywords")
config = configparser.ConfigParser()
config.read_file(codecs.open('configs/config.ini', "r", encoding="ISO-8859-1"))
outputfile = config["ReverseKeywords"]["output"]
inputfile = input("The keyword file that you would like to reverse: ")
try:
    os.remove(outputfile)
except OSError:
    pass
if os.stat(inputfile).st_size < 1:
    print("input file is empty.")
else:
    with open(outputfile, "w+", encoding="ISO-8859-1") as output:
        with open(inputfile, 'r', encoding="ISO-8859-1") as inputf:
            for line in inputf:
                line = line.rstrip("\n")
                keywordm = re.match(r"(.*) (.*)", line)
                try:
                    output.write(keywordm.group(2) + " " + keywordm.group(1) + "\n")
                except:
                    output.write(line + "\n")
	
    print("Done reversing!")

input("Press enter to continue...")
if platform.system() == "Linux":
    p = subprocess.call(["python3", "start.py"])
if platform.system() == "Windows":
    p = subprocess.call(["python", "start.py"])