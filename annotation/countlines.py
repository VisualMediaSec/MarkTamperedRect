import os
import numpy as np
from sys import argv

inputFilePath = ""

if __name__ == '__main__':
    if (len(argv)<2):
        print "usage: python countlines.py inputFilePath\n"
        exit()
    
    inputFilePath = argv[1]
    markedlst = []
    predictlst = []

    pathDir =  os.listdir(inputFilePath)
    for allDir in pathDir:        
        if "_marked.txt" in allDir:
            f1 = open(inputFilePath + allDir, 'r')
            lst1 = f1.readlines()
            #print lst
            markedlst += lst1[3:]
            f1.close()
        elif  "_predicted.txt" in allDir:
            f2 = open(inputFilePath + allDir, 'r')
            lst2 = f2.readlines()
            #print lst
            predictlst += lst2[3:]
            f2.close()

    print len(markedlst)
    print len(predictlst)

    cnt2 = 0
    for i in markedlst:
        item = i.strip('\n').strip('\r').split(', ')
        cnt2 += (len(item)-2)

    cnt1 = 0
    for i in predictlst:
        item = i.strip('\n').strip('\r').split(', ')
        cnt1 += (len(item)-2)

    print "bounding box total", cnt1/4
    print "bounding box marked", cnt2/4


