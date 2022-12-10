from pyzbar.pyzbar import decode
import serial, json

from .FridgeCam import FridgeCam
from .SupabaseDB import SupabaseDB

class SmartFridge:
    
    def __init__(self):
        self._cam = FridgeCam()
        self._db = SupabaseDB()
        self._serial = serial.Serial('/dev/serial0',115200,timeout=1)

        frame = self._cam.takePicture()

    def __del__(self):
        self._serial.close()

    def _extractBarcodesInFrame(self, frame) -> list:
        barcodes = []
        detectedBarcodes = decode(frame)
        for barcodeObj in detectedBarcodes:
            barcode=barcodeObj.data
            barcodes.append(barcode)
        return barcodes
    
    def _extractBarcodes(self, frames) -> list:
        barcodes = []
        for frame in frames
            newBarcodes = self._extractBarcodesInFrame(frame)
            barcodes += newBarcodes
        return barcodes

    def _readSerial(self):
        data = self._serial.readline()
        data_json=json.loads(data)

        return data_json

    def run(self):
        json = self._readSerial()

        if (json["switch"]=="True"):
            frames = self._cam.takePictureBurst(5)
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




    