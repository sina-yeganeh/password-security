def checkInstall():
	print("Checking to install Library . . .")
	try:
		from os import system
		import sys, colorama, random
	except Exception as ERROR:
		print ("Error: You not install \"random\", \"sys\" and \"colorama\" sys library")


	print("No problem:	\n you can run \"RunMe.py\"")

checkInstall()
