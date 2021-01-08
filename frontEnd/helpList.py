from colorama import Fore as c
from colorama import init

init()

# c.RED + " [" + c.WHITE + "" + c.RED + "] "

def Root():
    print(c.RED + " [" + c.WHITE + "1" + c.RED + "] " + c.LIGHTGREEN_EX + "Password Maker")
    print(c.RED + " [" + c.WHITE + "2" + c.RED + "] " + c.LIGHTGREEN_EX + "My Password")
    print(c.RED + " [" + c.WHITE + "3" + c.RED + "] " + c.LIGHTGREEN_EX + "How to use")
    print(c.RED + " [" + c.WHITE + "4" + c.RED + "] " + c.LIGHTGREEN_EX + "About")
    print(c.RED + " [" + c.WHITE + "5" + c.RED + "] " + c.RED + "Exit" + c.WHITE)

def passwordMaker():
    print(c.RED + " [" + c.WHITE + "1" + c.RED + "] " + c.LIGHTGREEN_EX + "By Charecter")
    print(c.RED + " [" + c.WHITE + "2" + c.RED + "] " + c.LIGHTGREEN_EX + "By Information")

def myPassword():
    print(c.RED + " [" + c.WHITE + "1" + c.RED + "] " + c.LIGHTGREEN_EX + "Saved Password")
    print(c.RED + " [" + c.WHITE + "2" + c.RED + "] " + c.LIGHTGREEN_EX + "Save New Password")

def howToUse():
    print(c.CYAN + """
 Jast G0 To This Link: github\SinaYeganeh0-0\PasswordSecurity
 And Read \'README.md\' | Good luck : )""")

def developer():
    print(c.CYAN + """
 developer : SinaYeganeh0-0
 Made In   : IRAN
 Powerd By : SinaYeganeh0-0
 Thank From: My Brother :)""")
