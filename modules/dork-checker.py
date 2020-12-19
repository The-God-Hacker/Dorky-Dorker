import os
import configparser
import codecs
import os.path
import platform
import subprocess
import time
import _thread
def dork_check(dork, threadcounter):
	global threadcount
	global banned
	dork = dork.strip("\n")
	try:
		if not banned == 1:
			search_results = google.search(dork, num_page)
			try:
				if int(search_results[0].number_of_results) >= int(good_dork_result_amount):
					with open (output, "a", encoding="ISO-8859-1") as outputf:
						outputf.write(dork + "\n")
					print(dork + " --> " + str(search_results[0].number_of_results) + " results.")
			except:
				print(dork + " --> error / 0 results.")
	except:
		if banned < 1:
			banned = 1
	threadcount -= 1
try:
	from google import google
except:
	print("It looks like you didn't install the module, try to run \"pip install git+https://github.com/abenassi/Google-Search-API\"")
	input("Press Enter to continue...")
	exit(1)
if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()
print("You selected dork checker")
num_page = 1
config = configparser.ConfigParser()
config.read_file(codecs.open('configs/config.ini', "r", encoding="ISO-8859-1"))
good_dork_result_amount = config["dork-checker"]["min-results"]
output = config["dork-checker"]["output"]
try:
    os.remove(output)
except OSError:
    pass
count = 0
file = input("Please give the dork file you would like to test: ")
with open(file, 'r', encoding="ISO-8859-1") as inputf:
	threadcount = 0
	banned = 0
	for dork in inputf:
		if not banned == 1:
			if threadcount < 100:
				threadcount += 1
				_thread.start_new_thread(dork_check, (dork, threadcount))
			else:
				threadcount += 1
				_thread.start_new_thread(dork_check, (dork, threadcount))
				while threadcount > 100:
					time.sleep(1)
		else:
			while not threadcount == 1:
				pass
			input("Google banned, change your ip and press enter to continue.")
			banned = 0
input("Press enter to continue...")
if platform.system() == "Linux":
    p = subprocess.call(["python3", "start.py"])
if platform.system() == "Windows":
    p = subprocess.call(["python", "start.py"])