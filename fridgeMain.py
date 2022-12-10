import serial, cv2 , base64, io, time , json, datetime
from pyzbar.pyzbar import decode
from barcodeDetect import barcodeDetect
from webcamSingle import webcamSingle
from serialCom import serialCom
from dataConcate import dataConcate
#from CNN_recognition import test_single_image
#from CNN_recognition import CNN_init
from takePictures import takePictures
active=1
foundFlag=False
piWeight=0
barcodeInt=[]
strList=[]
#model=CNN_init()
#dbInit
while active == 1:
    userInp=input("S for single image, B for burst, C for serial, M for mainloop, N for Neural Network, X to exit\n")
    if(userInp=='S'):
        webcamSingle()
    elif(userInp=='B'):
        takePictures()
        data=barcodeDetect()
        print(data)
        #sendData(dataF)
    elif(userInp=='C'):
        serialCom()
    elif(userInp=='X'):
        active=0
    elif(userInp=='N'):
        #print(str(test_single_image("apple.bmp",model)))
        print("CNN commented out")
    elif(userInp=='M'):
        while(1):
            jsonMsg=serialCom()
            if str(jsonMsg["switch"]) == "True":
                while (foundFlag==False):
                    takePictures()
                    barcodeInt=barcodeDetect()
                    #charList=ocr_digits()
                    if(barcodeInt!=0):
                        print("Barcode found")
                        foundFlag=True
                    else:
                        #productGuess=test_single_image()
                        #tell databse item found is productGuess
                        print("No barcode found")
                    if(ocr_digits()!=False):
                        print("Date found")
                    else:
                        #tell database no expiration date
                        print("No date found")
                if int(jsonMsg["direction"]) == 1: 
                    print(str(barcodeInt) +"Removed")
                    #sbDB itemString=getItem(int(barcodeInt))
                    #sbDB removeItem(itemString) 
                elif int(jsonMsg["direction"]) == 2:
                    print(str(barcodeInt) + "Added")
                    #sbDB itemString=getItem(int(barcodeInt))
                    #sbDB addItem(itemString)
                else: 
                    print("No item entered yet")
            if str(jsonMsg["alarm"]== "True"):
                print("Alarm is sounding")
            else:
                print("Waiting for door to open")
            temp=0
    elif(userInp=='A'):
        while(True):
            jsonMsg=serialCom()   
            if(jsonMsg["switch"]=="True"):
                takePictures()
                barcodeNum=barcodeDetect()
                if (barcodeNum not in barcodeInt) and (barcodeNum != 0):
                    barcodeInt.append(barcodeNum)
                #strList=ocr_digits()
                if int(jsonMsg["direction"]) == 1:
                    if not barcodeInt:
                        #productGuess=test_single_image("outputimage0.bmp",model)
                        print("cnn off")
                        #tell databse item found is productGuess 
                    print(str(barcodeInt) +"Removed")
                    #sbDB itemString=getItem(int(barcodeInt))
                    #sbDB removeItem(itemString) 
                elif int(jsonMsg["direction"]) == 2:
                    if not barcodeInt:
                        #productGuess=test_single_image("outputimage0.bmp",model)
                        print("cnn off")
                        #tell databse item found is productGuess
                    print(str(barcodeInt) + "Added")
                    #sbDB itemString=getItem(int(barcodeInt))
                    #sbDB addItem(itemString)
                else: 
                    print("No item entered yet")
            elif(jsonMsg["alarm"]=="True"):
                print("Hey database, alarm is goin")
    else:
        print("Input not understood, try again")