#String Manipulation & Regular Expression in Python
#Inbuilt library for command line arguments
import sys
from StringOperation import StringOperation

class StringManipulation():

    def main(self,args):
        #check number of parameters
        if len(args) < 2:
            print("Please enter atleast 2 arguments.")
        else:
            try:
                command = int(args[0])
                if command <1 or command >2:
                    print("Please enter valid command.")
                    print("1 for Reverse String.")
                    print("2 for count lowercase,uppercase and digits.")
                else:
                    #check arguments length for reverse operation
                    if command==1 and len(args[1:])>1:
                        print("Invalid string for reverse operation.")
                        print("Please enter single word input.")
                    else:
                        #call string oprtation function
                        obj2 = StringOperation()
                        obj2.doOperationWithRegEx(command,args[1:])

            except expression as identifier:
                print("Please enter valid command(1 or 2).")
                print("1 for Reverse String.")
                print("2 for count lowercase,uppercase and digits.")


if __name__ == "__main__":
    obj1 = StringManipulation()
    obj1.main(sys.argv[1:])