import serial, cv2 , base64, io, time , json
from pyzbar.pyzbar import decode
from webcamSimple import webcamBurst
from webcamTest import webcamSingle
from serialCom import serialCom
from barcodeConcate import dataConcate
from CNN_recognition import test_single_image
active=1
piWeight=0
barcodeList=[]
while active == 1:
    userInp=input("S for single image, B for burst, C for serial, M for mainloop, N for Neural Network, X to exit\n")
    if(userInp=='S'):
        webcamSingle()
    elif(userInp=='B'):
        data=webcamBurst()
        print(data)
        dataF=formatData(data)
        #sendData(dataF)
    elif(userInp=='C'):
        serialCom()
    elif(userInp=='X'):
        active=0
    elif(userInp=='N'):
        test_single_image("banana.bmp")
    elif(userInp=='M'):
        while(1):
            jsonMsg=serialCom()
            if str(jsonMsg["switch"]) == "true":
                barcodeList=webcamBurst()
                if int(jsonMsg["direction"]) == 1: #continue making main loop
                    print(dataConcate(barcodeList,"","Added"))
                elif int(jsonMsg["direction"]) == 2:
                    print(dataConcate(barcodeList,"","Removed"))
                else: 
                    print("No item entered")
            elif str(jsonMsg["alarm"]) == "true":
                print("Alarm is sounding")
            else:
                print("Waiting for door to open")
    else:
        print("Input not understood, try again")