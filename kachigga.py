import os

def greet():
    os.system("Hello there, $USER")

def acceptInput(input):
    if(input == "Hello"):
        greet()
    if(input == "Kachigga"):
        print("Kachigga!")

print("~~~Enter a command~~~")
usr_input = input()
acceptInput(usr_input)

