import os
import numpy as np
from sys import argv

inputFilePath = ""

if __name__ == '__main__':
    if (len(argv)<2):
        print "usage: python countframes.py inputFilePath\n"
        exit()
    
    inputFilePath = argv[1]
    lst = []

    pathDir =  os.listdir(inputFilePath)
    for allDir in pathDir:        
        if ".txt" in allDir:
            f1 = open(inputFilePath + allDir, 'r')
            lst1 = f1.readlines()
            #print lst
            lst += lst1
            f1.close()

    cnt1 = len(lst)-400

    cnt2 = 0
    for i in lst:
        item = i.strip('\n').strip('\r').split(', ')
        #print item[1],item[2],item[3],item[4]
        if (len(item)==5 and item[1]=='0' and item[2]=='0' and item[3] =='0' and item[4] =='0'):
            cnt2 += 1
            #print item
    
    print cnt1+cnt2
    print cnt1-cnt2



