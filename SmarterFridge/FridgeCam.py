import cv2
from time import sleep

class FridgeCam:
    def __init__(self):
        self._vc = cv2.VideoCapture(0)
    
    def takePicture(self):
        if self._vc.isOpened():
            rval, frame = self._vc.read()
        return frame

    def takePictureBurst(self, amount : int):
        frames = []
        sleep(1)
        for _ in range(amount):
            frames.append(self.take_picture())

        return frames

