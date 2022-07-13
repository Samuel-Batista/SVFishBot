from window_capture import WindowCapture
import cv2 as cv
import pyautogui
from time import sleep

cap = WindowCapture("Stardew Valley")

game_resolution = (1280, 721)

def trow():
    print('starting lauching...')
    x, y = cap.get_screen_position(((game_resolution[0]//2)-300, game_resolution[1]//2))
    pyautogui.mouseDown(x, y)

    while True:
        game_screenshoot = cap.get_screenshot()
        y_max = (game_resolution[0] // 2) - 420
        y_min = (game_resolution[1] // 2) - 160
        x_max = (game_resolution[0] // 2) + 98
        x_min = (game_resolution[1] // 2) + 220
        
        trow_bar = game_screenshoot[y_min:y_max, x_min:x_max]
        trow_bar_height, trow_bar_widht, _ = trow_bar.shape 
        
        spot_y_max = (trow_bar_height // 2)
        spot_y_min = (trow_bar_height // 2) - 1
        spot_x_max = (trow_bar_widht) - 9
        spot_x_min = (trow_bar_widht) - 10

        trow_spot = trow_bar[spot_y_min:spot_y_max, spot_x_min:spot_x_max]
        r, g, b = trow_spot[0][0]
        if g >= 244:
            cv.destroyWindow('trowBar')
            break
        # trow_bar = cv.rectangle(trow_bar, (spot_x_min, spot_y_min), (spot_x_max, spot_y_max), (0, 255, 0), 1)
        cv.imshow("trowBar", trow_bar)
        cv.waitKey(1)

    print('launched')
    pyautogui.mouseUp(x, y)


def wait_for_fish():
    print("waiting")
    while True:
        game_screenshoot = cap.get_screenshot()
        y_max = (game_resolution[1] // 2) - 90
        y_min = (game_resolution[1] // 2) - 160
        x_max = (game_resolution[0] // 2) + 20
        x_min = (game_resolution[0] // 2) - 5

        found_alert = game_screenshoot[y_min:y_max, x_min:x_max]
        found_spot_height, found_spot_widht, _ = found_alert.shape
        spot_y_max = (found_spot_height // 2)
        spot_y_min = (found_spot_height // 2) - 1
        spot_x_max = (found_spot_widht // 2)
        spot_x_min = (found_spot_widht // 2) - 1

        found_spot = found_alert[spot_y_min:spot_y_max, spot_x_min:spot_x_max]
        r, g, b = found_spot[0][0]

        if r < 20 and g > 200 and b > 200:
            print('found')
            cv.destroyWindow('found_spot')
            break

        cv.imshow('found_spot', found_alert)
        cv.waitKey(1)

    x, y = cap.get_screen_position(((game_resolution[0]//2), game_resolution[1]//2))
    pyautogui.mouseDown(x, y)
    sleep(0.3)
    pyautogui.mouseUp(x, y)

def check_fish():
    pass


trow()
wait_for_fish()