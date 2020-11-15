import os
import pyfiglet

def greet():
    os.system("Hello there, $USER")

def acceptInput(input):
    if(input == "Hello"):
        greet()
    if(input == "Kachigga"):
        print("Kachigga!")


def main():
    fig = Figlet(font='slant')
    introtext = fig.renderText("Hello there user!")
    print(introtext)

print("~~~Enter a command~~~")
usr_input = input()
acceptInput(usr_input)

