from window_capture import WindowCapture
import numpy as np
import cv2 as cv
import pyautogui
from time import sleep


from PIL import Image
cap = WindowCapture("Stardew Valley")


game_resolution = (1280, 721)

def trow():
    x, y = cap.get_screen_position(((game_resolution[0]//2)-300, game_resolution[1]//2))
    # pyautogui.mouseDown(x, y)

    while True:
        game_screenshoot = cap.get_screenshot()
        y_max = (game_resolution[0] // 2) - 420
        y_min = (game_resolution[1] // 2) - 160
        x_max = (game_resolution[0] // 2) + 98
        x_min = (game_resolution[1] // 2) + 220
        
        trow_bar = game_screenshoot[y_min:y_max, x_min:x_max]
        cv.imshow("game", trow_bar)
        cv.waitKey(1)


    
    pyautogui.mouseUp()
    # sleep(3)


trow()