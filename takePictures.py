import cv2
import io
import time
from pyzbar.pyzbar import decode

def takePictures():
    imgval=0
    dataList=[4]
    direction=0
    for imgval in range(5) :
        vc = cv2.VideoCapture(0)
        time.sleep(1)
        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False
        cv2.imwrite("outputimage"+str(imgval)+".bmp",frame)
        vc.release()