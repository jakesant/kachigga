import os
from pyfiglet import figlet_format
from termcolor import colored

def greet():
    os.system("Hello there, $USER")

def acceptInput(input):
    if(input == "Hello"):
        greet()
    if(input == "Kachigga"):
        print("Kachigga!")


def main():
    text1 = colored(figlet_format("1"), color="blue")
    text2 = colored(figlet_format("2"), color="green")
    text3 = colored(figlet_format("3"), color="yellow")
    print(text1)
    print(text2)
    print(text3)

main()
#print("~~~Enter a command~~~")
#usr_input = input()
#acceptInput(usr_input)

