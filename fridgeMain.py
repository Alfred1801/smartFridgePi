import serial, cv2 , base64, io, time , json, datetime
from pyzbar.pyzbar import decode
from webcamSimple import barcodeDetect
from webcamTest import webcamSingle
from serialCom import serialCom
from barcodeConcate import dataConcate
from CNN_recognition import test_single_image
from CNN_recognition import CNN_init
from takePictures import takePictures
active=1
piWeight=0
barcodeInt=0
charString=""
model=CNN_init()
#dbInit
while active == 1:
    userInp=input("S for single image, B for burst, C for serial, M for mainloop, N for Neural Network, X to exit\n")
    if(userInp=='S'):
        webcamSingle()
    elif(userInp=='B'):
        data=barcodeDetect()
        print(data)
        #sendData(dataF)
    elif(userInp=='C'):
        serialCom()
    elif(userInp=='X'):
        active=0
    elif(userInp=='N'):
        test_single_image("banana.bmp",model)
    elif(userInp=='M'):
        while(1):
            jsonMsg=serialCom()
            if str(jsonMsg["switch"]) == "True":
                takePictures()
                barcodeInt=barcodeDetect()
                #charList=ocr_digits()
                #barcodeList=webcamBurst()
                #charList=ocr_digits()
                #productGuess=test_single_image()
                if int(jsonMsg["direction"]) == 1: 
                    print(str(barcodeInt) +"Removed")
                    #sbDB itemString=getItem(int(barcodeInt))
                    #sbDB removeItem(itemString) 
                elif int(jsonMsg["direction"]) == 2:
                    print(str(barcodeInt) + "Added")
                    #sbDB itemString=getItem(int(barcodeInt))
                    #sbDB addItem(itemString)
                else: 
                    print("No item entered")
            elif str(jsonMsg["alarm"]) == "True":
                print("Alarm is sounding")
            else:
                print("Waiting for door to open")
            temp=0
    else:
        print("Input not understood, try again")