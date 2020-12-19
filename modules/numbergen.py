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
print("You selected generate numbers.")
config = configparser.ConfigParser()
config.read_file(codecs.open('configs/config.ini', "r", encoding="ISO-8859-1"))
outputfile = config["numbergen"]["output"]
try:
    os.remove(outputfile)
except OSError:
    pass
startnum=input("Please set the start number:")
endnum=input("Please set the end number:")
output = open(outputfile ,"w+")
count = int(startnum)
while count <= int(endnum):
	output.write(str(count) + "\n")
	count += 1

print("Number generating done!")
output.close()

input("Press enter to continue...")
if platform.system() == "Linux":
    p = subprocess.call(["python3", "start.py"])
if platform.system() == "Windows":
    p = subprocess.call(["python", "start.py"])