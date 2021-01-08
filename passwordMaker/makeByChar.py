import random
from colorama import Fore as c
from colorama import init
# c.RED + " [" + c.WHITE + "" + c.RED + "] "
def ByChar():
    init()
    charecter = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', ':', '\'', '\"', '|', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '<', '.', '>', '/', '?', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '~', '`']
    numberOfPassword = 11

    with open("password.txt", 'w') as FILE:
            for i in range(numberOfPassword):
                numberOfCharecter = random.randint(1, 52)
                PASSWORD = FILE.write(charecter[numberOfCharecter])

    with open("password.txt", 'r') as FILE:
        PASSWORD = FILE.read()
        print(c.CYAN + " " + PASSWORD)
