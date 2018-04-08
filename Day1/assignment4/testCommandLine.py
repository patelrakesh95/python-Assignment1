'''
Created on 08-Apr-2018

@author: p142325
'''
from assignment4 import multiCommandLine
import sys

def main(args):
    print(multiCommandLine.doOperation(args));

if __name__ == '__main__':
    main(sys.argv)