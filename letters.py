import os 
import cv2
import time
import numpy as np
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-n","--name", type=str,help="The name that is greeted")
args = parser.parse_args()
_name=(args.name.upper() if args.name != None else input("Enter a Name \n").upper())
def announce(name,char=("1","0")): #
    def make_img():
        y, x = [int(a) for a in os.popen('stty size', 'r').read().split()]
        size=cv2.getTextSize(text=name, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=2)[0]
        img = np.zeros((y,size[0],1), np.uint8)
        cv2.putText(img=img,text=name, org=(0,y),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(2), thickness=2, lineType=cv2.LINE_AA)
        frame=cv2.threshold(img, 1, 1, cv2.THRESH_BINARY)[1] #gets the binary image 
        if char==("1","0"):
            frame=["".join([str(i) for i in frame[a]]) for a in range(len(frame))]
        else:
            frame=["".join(list(map(lambda x: char[0] if x==1 else char[1],i))) for i in frame]
        return x,y,len(frame[0]),frame
    x,y,siz,frame=make_img()
    c=0
    while True:
        cy, cx = [int(a) for a in os.popen('stty size', 'r').read().split()]
        # Check current console size so that it can be compared to the one used to build image
        if c==siz+x:
            c=0
        if cx!=x:
            #redefine x boundary if it has changed
            y, x = [int(a) for a in os.popen('stty size', 'r').read().split()]
        if cy!=y:
            #redefine x and y boundary if it has changed + redraw image to fit new y boundary
            x,y,siz,frame=make_img()
        #Clear Console for next frame
        os.system('clear')
        #Print each line in each frame 
        print(*[i.rjust(cx+siz,char[1])[c:c+cx].ljust(cx,char[1]) for i in frame],sep="\n")
        
        c+=1
        time.sleep(.01) 
        #(i[:(c+cx)%cx]if (c+cx)>siz else "")
announce(_name)