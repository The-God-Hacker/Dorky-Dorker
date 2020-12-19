import re
import os
import os.path
import configparser
import codecs
import platform
import requests, json
import subprocess

if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()

print("You selected keyword suggestion scraper")

config = configparser.ConfigParser()
config.read_file(codecs.open('configs/config.ini', "r", encoding="ISO-8859-1"))
inputfile = input("Select the input keyword list: ")
outputfile = config["keyword-scraper"]["output"]
depth = config["keyword-scraper"]["depth"]
empty = re.compile("Input file for")
try:
    os.remove(outputfile)
except OSError:
    pass

if not os.path.isfile(inputfile):
    with open(inputfile, 'w+') as file:
        file.write("Input file for keyword suggestion scraper")
        print("input file is empty.")
else:
    f = open(inputfile)
    if empty.match(f.read()):
            print("input file is empty.")
    elif os.stat(inputfile).st_size < 1:
        print("input file is empty.")
    else:
        print("Scraping started!")
        keywordlist = []
        with open(inputfile, 'r', encoding="ISO-8859-1") as inputf:
            for line in inputf:
                count = 1
                while count <= int(depth):
                    if count == 1:
                        line = line.strip("\n")
                        URL="http://suggestqueries.google.com/complete/search?client=firefox&q=" + line
                        headers = {'User-agent':'Mozilla/5.0'}
                        response = requests.get(URL, headers=headers)
                        result = json.loads(response.content.decode('utf-8'))
                        with open(outputfile, 'a+') as file:
                            for num3 in range(len(result[1])):
                                if not result[1][num3] in keywordlist:
                                    try:
                                        file.write(result[1][num3] + '\n')
                                        print(result[1][num3])
                                        keywordlist.append(result[1][num3])
                                    except Exception as e:
                                        continue
                    else:
                        oldrs = result
                        for num1 in range(len(oldrs[1])):
                            URL="http://suggestqueries.google.com/complete/search?client=firefox&q=" + oldrs[1][num1]
                            headers = {'User-agent':'Mozilla/5.0'}
                            response = requests.get(URL, headers=headers)
                            result = json.loads(response.content.decode('utf-8'))
                            with open(outputfile, 'a+') as file:
                                for num2 in range(len(result[1])):
                                    if not result[1][num2] in keywordlist:
                                        try:
                                            file.write(result[1][num2] + '\n')
                                            print(result[1][num2])
                                            keywordlist.append(result[1][num2])
                                        except Exception as e:
                                            continue
                    count += 1

                count = 1
                while count <= int(depth):
                    if count == 1:
                        line = line.strip("\n")
                        URL="https://api.bing.com/osjson.aspx?query=" + line
                        headers = {'User-agent':'Mozilla/5.0'}
                        response = requests.get(URL, headers=headers)
                        result = json.loads(response.content.decode('utf-8'))
                        with open(outputfile, 'a+') as file:
                            for num3 in range(len(result[1])):
                                if not result[1][num3] in keywordlist:
                                    try:
                                        file.write(result[1][num3] + '\n')
                                        print(result[1][num3])
                                        keywordlist.append(result[1][num3])
                                    except:
                                        continue
                    else:
                        oldrs = result
                        for num1 in range(len(oldrs[1])):
                            URL="https://api.bing.com/osjson.aspx?query=" + oldrs[1][num1]
                            headers = {'User-agent':'Mozilla/5.0'}
                            response = requests.get(URL, headers=headers)
                            result = json.loads(response.content.decode('utf-8'))
                            with open(outputfile, 'a+') as file:
                                for num2 in range(len(result[1])):
                                    if not result[1][num2] in keywordlist:
                                        try:
                                            file.write(result[1][num2] + '\n')
                                            print(result[1][num2])
                                            keywordlist.append(result[1][num2])
                                        except:
                                            continue
                    count += 1
        print("Done scraping!")

input("Press enter to continue...")
if platform.system() == "Linux":
    p = subprocess.call(["python3", "start.py"])
if platform.system() == "Windows":
    p = subprocess.call(["python", "start.py"])