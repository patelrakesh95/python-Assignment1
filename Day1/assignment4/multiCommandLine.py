'''
Created on 08-Apr-2018

@author: p142325
'''

def doOperation(args):
    if len(args) >2:
        if args[1] == "1":
            result = 0
            for num in args[2:]:
                try:
                    result = result + int(num)
                except:
                    try:
                        result = result + float(num)
                    except:
                        print()
            return result
        elif args[1] == "2":
            result = ""
            for strs in args[2:]:
                result = result +" " + strs.lower();
            return result
        else:
            return "Invalid argument"
    else:
        return "Please Arguments"
        