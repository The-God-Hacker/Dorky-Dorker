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

print("You selected extractor")

config = configparser.ConfigParser()
config.read_file(codecs.open('configs/config.ini', "r", encoding="ISO-8859-1"))
inputfile = input("File you would like to extract from: ")
domainextentionsfile = config["extractor"]["domainextentions"]
pageparametersfile = config["extractor"]["pageparameters"]
keywordsfile = config["extractor"]["keywords"]
pagetypesfile = config["extractor"]["pagetypes"]
empty = re.compile("Input file for")
bad = re.compile("((?=.*?[@&(\/)',=?^$+\"]))")
max_domainextentions_len = int(config["extractor"]["max_domainextentions_len"])
max_pagetypes_len = int(config["extractor"]["max_pagetypes_len"])
max_pageparameters_len = int(config["extractor"]["max_pageparameters_len"])
max_keywords_len = int(config["extractor"]["max_keywords_len"])
try:
    os.remove(domainextentionsfile)
except OSError:
    pass

try:
    os.remove(pageparametersfile)
except OSError:
    pass

try:
    os.remove(keywordsfile)
except OSError:
    pass

try:
    os.remove(pagetypesfile)
except OSError:
    pass

if not os.path.isfile(inputfile):
    with open(inputfile, 'w+') as file:
        file.write("Input file for extractor")
        print("input file is empty.")
else:
    f = open(inputfile)
    if empty.match(f.read()):
            print("input file is empty.")
    elif os.stat(inputfile).st_size < 1:
        print("input file is empty.")
    else:
        print("Extracting started!")
        f = open(inputfile)
        domainextentions = open(domainextentionsfile, "w+")
        pageparameters = open(pageparametersfile, "w+")
        keywords = open(keywordsfile, "w+")
        pagetypes = open(pagetypesfile, "w+")
        keywordslist = []
        domainextentionslist = []
        pagetypeslist = []
        pageparameterslist = []
        with open(inputfile, 'r', encoding="ISO-8859-1") as inputf:
            for line in inputf:
                line = line.rstrip("\n")
                linem = re.search(r"([^\/\.]*)\.([^\/.]*|[^\/.]*\.|gov\.rw|com\.au|add\.YourOwnDommainExtentionsHereIfItHasMultipleDots|co\.za|ca\.us)\/[^\.]*[^\/]*\.([a-zA-Z1-9]*)\?([^=&]*)=", line)
                try:
                    if not len(linem.group(1)) > max_keywords_len:
                        if not bad.match(linem.group(1)):
                            if not linem.group(1) in keywordslist:
                                keywords.write(linem.group(1) + "\n")
                                keywordslist.append(linem.group(1))
                    if not len(linem.group(2)) > max_domainextentions_len:
                        if not bad.match(linem.group(2)):
                            if not linem.group(2) in domainextentionslist:
                                domainextentions.write(linem.group(2) + "\n")
                                domainextentionslist.append(linem.group(2))
                    if not len(linem.group(3)) > max_pagetypes_len:
                        if not bad.match(linem.group(3)):
                            if not linem.group(3) in pagetypeslist:
                                pagetypes.write(linem.group(3) + "\n")
                                pagetypeslist.append(linem.group(3))
                    if not len(linem.group(4)) > max_pageparameters_len:
                        if not bad.match(linem.group(4)):
                            if not linem.group(4) in pageparameterslist:
                                pageparameters.write(linem.group(4) + "\n")
                                pageparameterslist.append(linem.group(4))
                except AttributeError as e:
                    pass
                    

        print("Done extracting!")
        keywords.close()
        domainextentions.close()
        pagetypes.close()
        pageparameters.close()
input("Press enter to continue...")
if platform.system() == "Linux":
    p = subprocess.call(["python3", "start.py"])
if platform.system() == "Windows":
    p = subprocess.call(["python", "start.py"])