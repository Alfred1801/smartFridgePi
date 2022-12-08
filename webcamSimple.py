import cv2
import io
import time
from barcodeConcate import dataConcate
from pyzbar.pyzbar import decode

#filename="64barcode.txt"
#with open(filename,"rb") as fid:
#  data = fid.read()
#b64_bytes = base64.b64encode(data)
#b64_string = b64_bytes.decode()
#image=imread(io.BytesIO(base64.b64decode(b64_string)))
#image = v2.cvtColor(image,cv2.COLOR_RGB2BGR)
def barcodeDetect():
  imgval=0
  dataList=0
  a=0
  for imgval in range(5) :
    image = cv2.imread("outputimage"+str(imgval)+".bmp",cv2.IMREAD_ANYCOLOR)
    detectedBarcodes = decode(image)
    for barcode in detectedBarcodes:
      (x,y,w,h)=barcode.rect
      cv2.rectangle(image, (x,y),(x+w,y+h),(255,0,0),5)
      #print(barcode.data)
      #print(barcode.type)
      #print("barcode found in image: ", str(imgval+1))
      dataList=barcode.data
      a=a+1
  print(dataList)
  return dataList
#image = cv2.imread("outputimage.bmp"+y+".bmp",cv2.IMREAD_ANYCOLOR)
#detectedBarcodes = decode(image)