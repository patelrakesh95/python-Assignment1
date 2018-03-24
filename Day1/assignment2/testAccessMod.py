'''
Created on 24-Mar-2018

@author: p142325
'''
from assignment2 import accessMod

def main():
    accessMod.printProperties()
    print("Display members value from testAccessMod module")
    print("Name : ",accessMod.__name) #invalid way to access private members
    print("Gender : ",accessMod.gender) #OK
    print("Age : ",accessMod.age) #OK
    print("Height : ",accessMod._height) #OK
    print("Married : ",accessMod.isMarried) #OK

if __name__ == '__main__':
    main()