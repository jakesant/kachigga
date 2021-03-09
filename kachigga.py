#!/usr/bin/env python

import os
import random
from pyfiglet import figlet_format
from cmd import Cmd
from termcolor import colored
import colorama
import getpass
import scrabble
from datetime import datetime
from convert_file import con_file

class Prompt(Cmd):
    def do_aw(self, input):
        print("Hello there,", getpass.getuser()) #Prints current user's name
    
    def do_cd(self, input):
        os.chdir(input)

    def do_dir(self, input):
        print(os.listdir())
    def do_ls(self, input):
        print(os.listdir())

    def do_exit(self, input):
        print("Goodbye")
        return True

    def do_cwd(self, input):
        print("CWD: ", os.getcwd())

    def do_echo(self, input):
        if(input is None):
            print("\n")
        else:
            print(input)
        
    def do_hex(self, input):
        if(hex(int(input)) is not None):
            print(input, " in hex is ", hex(int(input)))
        else:
            print("Cannot calculate hex for ", input)

    def do_bin(self, input):
        if(bin(int(input)) is not None):
                print(input, "in binary is ", bin(int(input)))
        else:
            print("Cannot convert ", input, " to binary")

    def do_oct(self, input):
        if(oct(int(input)) is not None):
            print(input, "in octal is ", oct(int(input)))
        else:
            print("Cannot calculate octal value for ", input)

    def do_nicetext(self, input):
        args = input.split(" ")
        if(args[1] == '--colour'):
            print(colored(figlet_format(args[0]), color=args[2]))
        else:
            print(colored(figlet_format(input)))

    def do_scrabble(self, input):
        scrabble.calculate_points(input)
    
    def do_d6(self, input):
        roll = random.randint(1, 6)
        print("You rolled a ", roll)

    def do_d12(self, input):
        roll = random.randint(1, 12)
        print("You rolled a ", roll)

    def do_d20(self, input):
        roll = random.randint(1, 20)
        print("You rolled a ", roll)

    def do_time(self, input):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

    def do_date(self, input):
        now = datetime.now()
        current_date = now.strftime("%d-%m-%Y")
        print("Current Date =", current_date)

    def do_ping(self, input):
        os.system('ping -n 4 {}'.format(input))

    def do_taboo(self, input):
        input = input.upper()
        input = input.replace("S","Z")
        input = input.replace("B","13")
        input = input.replace("I","1")
        print(input)

    def do_convert(self, input):
        con_file(input, output_path = os.getcwd())

    def default(self, input):
        print("Unknown command")

def load():
    text1 = colored(figlet_format("Welcome"), color="blue")
    text2 = colored(figlet_format("To"), color="green")
    text3 = colored(figlet_format("Kachigga"), color="yellow")
    print(text1)
    print(text2)
    print(text3)

if __name__ == '__main__':
    colorama.init()
    load()
    prompt = Prompt()
    prompt.prompt = 'kachIgga>> '
    prompt.cmdloop("Starting prompt...")

#print("~~~Enter a command~~~")
#usr_input = input()
#acceptInput(usr_input)

