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
config = configparser.ConfigParser()
config.read_file(codecs.open('configs/config.ini', "r", encoding="ISO-8859-1"))
print("You selected antipublic")

keyworddb = config["antipublic"]["keyworddb"]
pageparameterdb = config["antipublic"]["pageparameterdb"]

if not os.path.isfile(keyworddb):
    file = open(keyworddb, 'w+')
    file.close()
if not os.path.isfile(pageparameterdb):
    file = open(pageparameterdb, 'w+')
    file.close()

keywordfile = input("Keyword file that you would like to check: ")
parameterfile = input("Parameter file that you would like to check: ")

with open ("private_keywords.txt", "w+") as outputkw:
	with open(keywordfile, "r") as keywordf:
		with open(keyworddb, "r+") as keyworddatabase:
			for keyword in keywordf:
				keyword = keyword.strip("\n")
				true = 0
				for kwdb in keyworddatabase:
					kwdb = kwdb.strip("\n")
					if kwdb == keyword:
						true += 1
						print(true)
						break
				if true == 0:
					keyworddatabase.write(keyword + "\n")
					outputkw.write(keyword + "\n")

with open ("private_pageparameters.txt", "w+") as outputpp:
	with open(parameterfile, "r") as parameterf:
		with open(pageparameterdb, "r+") as pageparameterdatabase:
			for pageparameter in parameterf:
				pageparameter = pageparameter.strip("\n")
				true = 0
				for ppdb in pageparameterdatabase:
					ppdb = ppdb.strip("\n")
					if ppdb == pageparameter:
						true += 1
						print(true)
						break
				if true == 0:
					pageparameterdatabase.write(pageparameter + "\n")
					outputpp.write(pageparameter + "\n")

input("Press enter to continue...")
if platform.system() == "Linux":
    p = subprocess.call(["python3", "start.py"])
if platform.system() == "Windows":
    p = subprocess.call(["python", "start.py"])