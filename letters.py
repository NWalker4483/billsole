import os 
import cv2
import time
import numpy as np
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-n","--name", type=str,help="The name that is greeted")
args = parser.parse_args()
name=(args.name if args.name != None else input("Enter a Name \n"))
def make_img():
    y, x = [int(a) for a in os.popen('stty size', 'r').read().split()]
    size=cv2.getTextSize(name, cv2.FONT_HERSHEY_SIMPLEX, 1, thickness=2)[0]
    img = np.zeros((y,size[0],1), np.uint8)
    cv2.putText(img,name,(0,int(y-2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (2), 2, cv2.LINE_AA)
    frame=cv2.threshold(img, 1, 1, cv2.THRESH_BINARY)[1]
    frame=["".join([str(i) for i in frame[a]]) for a in range(len(frame))]
    return x,y,len(frame[0]),frame
x,y,siz,frame=make_img()
c=0
while True:
    if c==siz:
        c=0
    cy, cx = [int(a) for a in os.popen('stty size', 'r').read().split()]
    if cx!=x or cy!=y:
        x,y,siz,frame=make_img()
    # if cx!=x or cy!=y:
    #    break
    
    os.system('clear')
    #sys.stdout.flush()
    print(*[i[c:c+cx-1].rjust(cx-x,"0").ljust(x,"0") for i in frame],sep="\n")
    c+=1
    time.sleep(.01) 
    #(i[:(c+cx)%cx]if (c+cx)>siz else "")