import cv2
import io
from pyzbar.pyzbar import decode

def webcamSingle():
  #filename="64barcode.txt"
  #with open(filename,"rb") as fid:
  #  data = fid.read()
  #b64_bytes = base64.b64encode(data)
  #b64_string = b64_bytes.decode()
  #image=imread(io.BytesIO(base64.b64decode(b64_string)))
  #image = v2.cvtColor(image,cv2.COLOR_RGB2BGR)

  vc = cv2.VideoCapture(0)

  if vc.isOpened():
    rval, frame = vc.read()
  else:
    rval = False
  cv2.imwrite("outputimage.bmp",frame)
  vc.release()

  image = cv2.imread("outputimage.bmp",cv2.IMREAD_ANYCOLOR)

  detectedBarcodes = decode(image)

  for barcode in detectedBarcodes:
    (x,y,w,h)=barcode.rect
    cv2.rectangle(image, (x,y),(x+w,y+h),(255,0,0),5)
    print(barcode.data)
    print(barcode.type)
  if not cv2.imwrite("barcodeoutput.bmp",image):
    raise Exception("Could not write image")




