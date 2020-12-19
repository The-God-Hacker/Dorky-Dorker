import os
import os.path
import configparser
import codecs
import random
import platform
import subprocess

if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()

print("You selected randomize")
config = configparser.ConfigParser()
config.read_file(codecs.open('configs/config.ini', "r", encoding="ISO-8859-1"))
inputfile = input("Please type the file you would like to randomize: ")
outputfile = config["random"]["output"]

if not os.path.isfile(inputfile):
    print("Input file not found")
else:
    f = open(inputfile)
    if os.stat(inputfile).st_size < 1:
        print("input file is empty.")
    else:
        with open(inputfile,'rb') as source:
            max_line_len = max(len(line) for line in source)
        with open(inputfile,'rb') as source, open("temp.txt",'wb') as dest:
            for count,line in enumerate(source):
                dest.write(line + b"*"*(max_line_len-len(line)))
        indexes = list(range(count+1))
        random.shuffle(indexes)
        with open(outputfile, "w+") as output:
            with open("temp.txt",'rb') as source:
                for idx in indexes:
                    source.seek(idx * max_line_len)
                    random_line = source.read(max_line_len).decode("ISO-8859-1").split("\n")[0]
                    random_line = random_line.strip()
                    output.write(random_line + "\n")

        os.remove("temp.txt")
        print("Randomizing done!")
        
input("Press enter to continue...")
if platform.system() == "Linux":
    p = subprocess.call(["python3", "start.py"])
if platform.system() == "Windows":
    p = subprocess.call(["python", "start.py"])