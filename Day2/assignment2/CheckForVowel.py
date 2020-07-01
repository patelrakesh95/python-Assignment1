#Character Manipulation in Python
from VowelConsonant import VowelConsonant
import sys

class CheckForVowel:

    def main(self,args):
        #check the size of the arguments
        if len(args) > 1:
            print("Please enter only single commandline argument.")
        else:
            #check the length of first argument
            if len(args[0]) > 1:
                print("Please enter only single character argument.")
            else:
                '''convert inour character to capital so it will work for both.
                lower case and upper case.
                If we don't change then need to write seperate logic for both'''
                intChar = ord(args[0].upper())
                #check whether given character is alphabet or not
                if intChar>=65 and intChar<=90:
                    VowelConsonant.checkChar(intChar)
                else:
                    print("Please enter only alphabet character.")

if __name__ == "__main__":
    obj = CheckForVowel()
    #skip the first argument of the file name it self
    obj.main(sys.argv[1:])