import serial, cv2 , base64, io, time , json
from pyzbar.pyzbar import decode
from webcamSimple import webcamBurst
from webcamTest import webcamSingle
from serialCom import serialCom
from barcodeConcate import dataConcate
active=1
piWeight=0
barcodeList=[]
while active == 1:
    userInp=input("S for single image, B for burst, C for serial, M for mainloop, X to exit\n")
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
    elif(userInp=='M'):
        while(1):
            jsonMsg=serialCom()
            if str(jsonMsg["switch"]) == "true":
                barcodeList=webcamSimple()
                if int(jsonMsg["weight"])<piWeight-(piWeight*0.1): #continue making main loop
                    
                elif int(jsonMsg["weight"])>piWeight+(piWeight*0.1):

    else:
        print("Input not understood, try again")