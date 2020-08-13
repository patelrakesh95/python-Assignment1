#System Properties in Python
import sys
from SystemProperties import SystemProperties

class ShowSystemProperties:
    def main(self,cmd):
        obj2 = SystemProperties()
        if cmd == "whoami":
            obj2.whoami()
        elif cmd == "uname":
            obj2.uname()
        elif cmd == "udir":
            obj2.udir()
        elif cmd == "all":
            obj2.whoami()
            obj2.uname()
            obj2.udir()
        else:
            print("Invalid Command")

if __name__ == "__main__":
    obj1 = ShowSystemProperties()
    if len(sys.argv) < 2:
        print("Insufficient Arguments")
    else:
        obj1.main(sys.argv[1])