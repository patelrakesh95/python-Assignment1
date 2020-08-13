#Display user's name, OS name and user directory of OS
import os

class SystemProperties:
    #Print user's name
    def whoami(self):
        os.system("whoami")
    #Print OS name
    def uname(self):
        os.system("uname")
    #Print user directory of Linux
    def udir(self):
        os.system("echo $HOME")