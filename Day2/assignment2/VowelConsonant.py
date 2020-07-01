#Character Manipulation in Python

class VowelConsonant:
    def checkChar(ch):
        isVowel = False
        if ord('A') == ch:
            isVowel= True
        elif ord('E') == ch:
            isVowel= True
        elif ord('I') == ch:
            isVowel= True
        elif ord('O') == ch:
            isVowel= True
        elif ord('U') == ch:
            isVowel= True
        
        #check does inout character is vowel or constant
        if isVowel:
            print("Given chacter is vowel.")
        else:
            print("Given chacter is constant.")
