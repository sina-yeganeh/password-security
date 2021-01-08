from frontEnd.banner import SLANTbanner
from frontEnd.helpList import *
from myPassword.passwordSaver import getPassword, showPassword
from passwordMaker.makeByChar import ByChar
from passwordMaker.makeByinfo import ByInfo
from sys import exit
from colorama import Fore as c
from colorama import init

def terminal():
    init()
    global number
    try:
        number = input("\n Chose The Number $ ")
    except KeyboardInterrupt:
        print("")

def main():
    while True:
        SLANTbanner()
        Root()
        terminal()

        if number == "1":
            passwordMaker()
            terminal()
            if number == "1":
                ByChar()
            elif number == "2":
                ByInfo()

        elif number == "2":
            myPassword()
            terminal()
            if number == "1":
                showPassword()
            elif number == "2":
                getPassword()

        elif number == "3":
            howToUse()

        elif numebr == "4":
            developer()

        elif number == "5":
            exit()

if __name__ == '__main__':
    main()
