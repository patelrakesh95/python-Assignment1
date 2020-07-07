#String Manipulation caller class
import sys
from StringOperation import StringOperation

class StringManipulation:
    def main(self,args):
        if len(args) > 0 :
            obj2 = StringOperation()
            obj2.doOperation(args)
        else:
            print("Please enter command line arguments.")

if __name__=='__main__':
    obj = StringManipulation()
    obj.main(sys.argv[1:])
