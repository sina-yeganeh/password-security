from colorama import Fore as c
from colorama import init
from os import system

init()
# c.RED + "[" + c.WHITE + "~" + c.RED + "]"
# c.RED + "[" + c.WHITE + "~" + c.RED + "]" + c.YELLOW + " " + c.WHITE + "  "

def getPassword():
	global PASSWORD
	global VALUE

	PASSWORD = input (" Plese enter your PASSWORD $ ")
	VALUE = input (" Plese enter the VALUE $ ")
	with open("password.txt", 'r') as FILE:
		theFirst = FILE.readline()

	with open("password.txt", 'a') as FILE:
		if theFirst == "":
			FILE.writelines(PASSWORD + " => " + VALUE)
		else:
			FILE.writelines("\n" + PASSWORD + " => " + VALUE)

def showPassword():
	orange = '\033[33m'
	try:

		with open("password.txt", 'r') as FILE:
			while True:
				PASSWORD = FILE.readline()
				if PASSWORD == "":
					print (" End of password . . .")
					break
				else:
					print (c.CYAN + " " + PASSWORD)

	except Exception as ERROR:
		pass
