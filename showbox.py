import cv2
import copy
import numpy as np
from sys import argv

r = 2
seqBox = {}
boxList = []

if __name__ == '__main__':        
    if (len(argv)<1):
        print "usage: python showbox.py txtFileName\n"
        exit()
    txtFileName = argv[1]
    f = open(txtFileName, 'r')
    if not f:
    	exit()
    oFileName = f.readline()
    tFileName = f.readline()
    oFileName = oFileName.strip('\n').strip('\r')
    tFileName = tFileName.strip('\n').strip('\r')
    origin = cv2.VideoCapture(oFileName)
    tamper = cv2.VideoCapture(tFileName)
    f.readline() #skip title

    fps = origin.get(cv2.CAP_PROP_FPS)
    size = (int(origin.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(origin.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print "fps %.2f, width %d, height %d" % (fps, size[0], size[1])
    print "\npress ESC for quit\n"
    print oFileName
    print tFileName

    w, h = size[0], size[1]
    cv2.namedWindow('origin', cv2.WINDOW_NORMAL)
    cv2.namedWindow('tamper', cv2.WINDOW_NORMAL)
    cv2.moveWindow('tamper', w/r+40, 40)

    if (not origin.isOpened()) or (not tamper.isOpened()):
        exit()

    #read box to seq
    linestr = f.readline().strip('\n').strip('\r')
    while (linestr):
        d = linestr.split(', ')
        frameID = int(d[0])
        seqBox[frameID] = []
        for i in range(1, len(d)-1, 4):
            #print d[i], i
            x1, y1 = d[i], d[i+1]
            x2, y2 = d[i+2], d[i+3]
            boxDict = dict(x1=int(x1)/r, y1=int(y1)/r, x2=int(x2)/r, y2=int(y2)/r)
            seqBox[frameID].append(boxDict)
            
        linestr = f.readline().strip('\n').strip('\r')
    f.close()

    #display frame by frame
    cnt = 0
    ret1, frame = origin.read()
    ret2, framet = tamper.read()
    while (ret1 and ret2):        
        if cnt in seqBox:
            boxList = copy.deepcopy(seqBox.get(cnt))
        else:
            boxList = []

        if (ret1 and ret2):
            res=cv2.resize(frame, (w/r,h/r), interpolation=cv2.INTER_CUBIC)
            rest=cv2.resize(framet, (w/r,h/r), interpolation=cv2.INTER_CUBIC)

            for cbox in boxList:
                cv2.rectangle(res, (cbox["x1"], cbox["y1"]), (cbox["x2"], cbox["y2"]), (0,255,0),2,0) 

            cv2.imshow('origin', res)
            cv2.imshow('tamper', rest)

        cnt += 1
        if cv2.waitKey(0) & 0xFF == 27:
            break

        ret1, frame = origin.read()
        ret2, framet = tamper.read()

    origin.release()
    tamper.release()
    cv2.destroyAllWindows()
