import random
from colorama import Fore as c
from colorama import init

def ByInfo():
    init()
    PASSWORD = []
    info = []
    theAppendChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '^', '&', '*']

    name = input(' name : ')
    family = input(' family : ')
    age = str(input(' age : '))

    info = [name, age, family]

    for i in range(3):
        PASSWORD.append(info[i])

    with open("password.txt", 'w') as FILE:
        for i in range(4):
            numberOfIndex = random.randint(1, 17)
            appendChar = FILE.write(theAppendChar[numberOfIndex])

    with open("password.txt", 'r') as FILE:
        appendChar = FILE.read()

    PASSWORD.append(str(appendChar))

    finalyPassword = PASSWORD[0] + PASSWORD[1] + PASSWORD[2] + PASSWORD[3] # I can't use "sum" function ...
    print(c.CYAN + " " + finalyPassword)
