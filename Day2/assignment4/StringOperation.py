#Count the lowercase, uppercase and digits in argument string
class StringOperation:
    def doOperation(self,args):
        lowerCnt = 0
        upperCnt = 0
        digitCnt = 0
        for arg in args:
            for i in range(0,len(arg)):
                #get the ascii value of each charactor and check
                ascii = ord(arg[i])
                #check for number letters
                if ascii >= 48 and ascii <=57:
                    digitCnt = digitCnt + 1
                #check for uppercase letters
                elif ascii >= 65 and ascii <= 90:
                    upperCnt = upperCnt + 1
                #check for lowercase letters
                elif ascii>=97 and ascii <=122:
                    lowerCnt = lowerCnt + 1
        print(f"Digit Count : {digitCnt}")
        print(f"Lower Count : {lowerCnt}")
        print(f"Upper Count : {upperCnt}")
