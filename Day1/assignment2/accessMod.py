'''
Access Modifiers
Created on 24-Mar-2018

@author: p142325
'''

'''
Python has no access modifiers.
declare members and method with underscore notation before starting of name.
It will considered as non public members or methods.
refer below example
'''
age = 29; #number public member
_height = 5.13 # floating protected member
gender='M' #character public member
isMarried = False #boolean public member
__name = "Rakesh Patel" # String private member

def printProperties():
    print("Display members value from accessMod module")
    print("Name : ",__name)
    print("Gender : ",gender)
    print("Age : ",age)
    print("Height : ",_height)
    print("Married : ",isMarried)
    