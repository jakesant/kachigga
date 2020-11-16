#!/usr/bin/env python

import os
from pyfiglet import figlet_format
from cmd import Cmd
from termcolor import colored
import colorama
import getpass

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
        return True

    def do_cwd(self, input):
        print("CWD: ", os.getcwd())

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

