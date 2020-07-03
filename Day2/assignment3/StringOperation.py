'''String Operation class for count digits,lowercase letters
and uppercase letters.'''
#Inbuilt library for Regular Expression
import re

class StringOperation:
    
    def doOperationWithRegEx(self,command,word):
        #operation for reverse string
        if command == 1:
            reverse  = ""
            word = word[0]
            for i in range(len(word)-1,-1,-1):
                reverse = reverse + word[i]
            print(reverse)
        #operation for count digits,lowercase and uppercase letters
        else:
            #regular expression for Digits
            digitReg = re.compile('\d')
            #regular expression for Lowercase letters
            lowerReg = re.compile('[a-z]')
            #regular expression for Uppercase letters
            upperReg = re.compile('[A-Z]')
            digitCount = 0
            lowerCount = 0
            upperCount = 0
            for  str in word:
                #count digits
                digitCount = digitCount + len(digitReg.findall(str))
                #count lowercase letters
                lowerCount = lowerCount + len(lowerReg.findall(str))
                #count uppercase letters
                upperCount = upperCount + len(upperReg.findall(str))
            print(f"Total Digit count is {digitCount}")
            print(f"Total Lowercase count is {lowerCount}")
            print(f"Total Uppercase count is {upperCount}")