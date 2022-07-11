from anyio import current_time
from numpy import imag, true_divide
from window_capture import WindowCapture
import cv2 as cv

cap = WindowCapture("Stardew Valley")


while True:
    current_image = cap.get_screenshot()
    current_image.reshape(300, 300)
    cv.imshow('game', current_image)
    cv.waitKey(1)