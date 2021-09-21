import cv2
from utils import time_execution
from facial_detection import FacialDetector


class HaarDetector(FacialDetector):
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    @time_execution
    def __call__(self, im, detect_eyes=True, **kwargs):
        if len(im.shape) > 2:
            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(im, **kwargs)
        if detect_eyes:
            eyes = self.eye_cascade.detectMultiScale(im, **kwargs)

            return faces, eyes
        return faces