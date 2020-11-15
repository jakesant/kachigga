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
    fig = pyfiglet.Figlet(font='slant')
    introtext = fig.renderText("1!")
    othertext = fig.renderText("2!")
    text3 = fig.renderText("3")
    print(introtext)
    print("\n\n")
    print(othertext)
    print("\n\n")
    print(text3)

main()
#print("~~~Enter a command~~~")
#usr_input = input()
#acceptInput(usr_input)

