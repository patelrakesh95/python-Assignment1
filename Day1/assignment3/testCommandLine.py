'''
Take Username and Password from Command Line Argument

Created on 01-Apr-2018

@author: p142325
'''
from sys import argv
from assignment3.usernamePassword import validate

def main():
    if len(argv) < 3:
        print("Please enter Username and Password")
    else:
        isValid = validate(argv[1],argv[2])
        if  isValid == True:
            print("Welcome "  ,argv[1])
        else:
            print("Invalid Username or Password")
            
main()