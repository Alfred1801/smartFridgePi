# import the necessary packages
import pytesseract
#import argparse
import cv2
#import base64


# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="path to input image to be OCR'd")
#ap.add_argument("-d", "--digits", type=int, default=1,
#	help="whether or not *digits only* OCR will be performed")
#args = vars(ap.parse_args())
#def ocr_digits:
# Detecting and OCR'ing Digits with Tesseract and Python : 
# load the input image, convert it from BGR to RGB channel ordering, and initialize our Tesseract OCR options as an empty string
charList[]
for imgval in range(5) :
    image = cv2.imread("outputimage"+str(imgval)+".bmp",cv2.IMREAD_ANYCOLOR)
    #rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    edge = cv2.Canny(image,100,200)
    # check to see if *digit only* OCR should be performed, and if so,
    # update our Tesseract OCR options
    options = "outputbase digits"
    #options = ""
    # OCR the input image using Tesseract
    text = pytesseract.image_to_string(edge, config=options)
    #text = pytesseract.image_to_string(rgb, config=options)
    #text = pytesseract.image_to_boxes(rgb, config=options)
    print(text)

