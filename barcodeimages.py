from pyzbar import pyzbar
import cv2

def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)

    barcodefound = 0  # keeps track of whether barcode has been found

    for obj in decoded_objects:
        barcodefound = 1
        # draw the barcode
        print("detected barcode:", obj)
        image = draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()

    # sends error message if barcode not found
    if(barcodefound == 0):
        print("Barcode not found.")
        print()

    return image

def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    return image

if __name__ == "__main__":
    from glob import glob

    barcodes = glob("barcode*.jpg")
    print("barcodes:", barcodes)
    print()
    imgval=0
    for barcode_file in barcodes:
        # load the image to opencv
        img = cv2.imread(barcode_file)
        # decode detected barcodes & get the image
        # that is drawn
        img = decode(img)
        if not cv2.imwrite("barcodeoutput"".bmp",frame):
            raise Exception("Could not write image")
        # show the image
        #cv2.imshow("img", img)
        