from pyzbar.pyzbar import decode
import serial, json, pytesseract

from .FridgeCam import FridgeCam
from .SupabaseDB import SupabaseDB
from .ProductDetector import ProductDetector

class SmartFridge:
    
    def __init__(self):
        self._cam = FridgeCam()
        self._db = SupabaseDB()
        self._serial = serial.Serial('/dev/serial0',115200,timeout=1)
        self._pd = ProductDetector()
        frame = self._cam.takePicture()
        self.OCRoptions = "outputbase digits"

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
        for frame in frames:
            newBarcodes = self._extractBarcodesInFrame(frame)
            if newBarcodes not in barcodes:
                barcodes += newBarcodes
        return barcodes

    def _readSerial(self):
        data = self._serial.readline()
        data_json=json.loads(data)
        return data_json

    def _readDateInFrame(self,frame) -> list:
        date=''
        text = pytesseract.image_to_string(frame, config=self.options)
        return date

    def _readDatesInFrames(self,frames) -> list:
        dates = []
        for frame in frames:
            newDate = self._readDateInFrame(frame)
            dates += newDate
        return dates
    
    def _collectData(self,barcode,date,guess,direction) -> list:
        data=[]
        data.append(self._db.getUserID(int(barcode)))
        data.append(data)
        data.append(guess)
        return data

    def run(self):
        json = self._readSerial()
        if (json["switch"]=="True"):
            frames = self._cam.takePictureBurst(5)
            barcodeList = self._extractBarcodes(self,frames)
            dateList = self._readDatesInFrames(self,frames) #Dates not currently being read in. 
            guessList = []
            if int(json["direction"])!= 0:
                if not barcodeList:
                    guessList = self._pd.productGuesses(frames)
                collectedData=self._collectData(int(barcodeList[len(barcodeList)-1]),dateList[len(dateList)-1],guessList[len(guessList)-1])
                if int(json["direction"]) == 1:
                    print("hello")
                    self._db.removeItem(collectedData[0],collectedData[1],collectedData[2])
                elif int (json["direction"]) == 2:
                    print("hello")
                    self._db.sendItem(collectedData[0],collectedData[1],collectedData[2])
            else: 
                print("No item entered yet")
        else:
            self.collectedItems.clear()
        if(json["alarm"]=="True"):
            print("Hey database, alarm is goin")




    