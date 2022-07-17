from window_capture import WindowCapture
import cv2 as cv
import pyautogui
from time import sleep

cap = WindowCapture("Stardew Valley")
game_height, game_width, _ = cap.get_screenshot().shape
game_resolution = (game_width, game_height)

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



def cath_fish():
    x, y = cap.get_screen_position(((game_resolution[0]//2), game_resolution[1]//2))
    pyautogui.mouseDown(x, y)
    sleep(0.3)
    pyautogui.mouseUp(x, y)

    game_screenshot = cap.get_screenshot()
    screen_height, screen_width, _ = game_screenshot.shape
    screen_center_x, screen_center_y = screen_width // 2, screen_height // 2

    top_pos = 0
    botton_pos = 0
    center_bar_pos = 0
    fish_pos = 0

    while True:
        game_screenshot = cap.get_screenshot()
        cath_bar = game_screenshot[20:screen_height-130, screen_center_x+140:screen_center_x+215]
        cath_bar_height, cath_bar_widht, _ = cath_bar.shape
        bar_center_x, bar_center_y = cath_bar_widht // 2, cath_bar_height // 2

        # cv.rectangle(cath_bar, (bar_center_x - 30, bar_center_y - 5), (bar_center_x - 25, bar_center_y - 2), (0, 0, 255), 1)
        bar_spot = cath_bar[bar_center_y-5:bar_center_y-4, bar_center_x-30:bar_center_x - 29]
        # print(bar_spot)
        # [ 67 142 203] bar
        # [ 78 134 146] none
        b_bs, g_bs, r_bs = bar_spot[0][0]
        if r_bs >= 200:
            # peixe e um sequencia de verdes e azuis
            # barra de pesca e uma sequencia igual de tons de verde
            # fundo sequencia variada de tons de azuis

            
            # encontrar a parte de cima da barra de pesca
            for h in range(cath_bar_height):
                b_p, g_p, r_p  = cath_bar[h:h+1, bar_center_x-15:bar_center_x-14][0][0]

                if b_p < 200:
                    count = 0

                    # verify similary sequence of pixel
                    if h < cath_bar_height - 10:
                        for plus in range(3):
                            b_pp, g_pp, r_pp  = cath_bar[h+plus:(h+1)+plus, bar_center_x-15:bar_center_x-14][0][0]
                            if b_pp == b_p and g_pp == g_p and r_pp == r_p:
                                count += 1
                    
                    if count >= 3:
                        cv.line(cath_bar, (bar_center_x - 50, h-2), (bar_center_x + 50, h-2), (255, 0, 0), 3)
                        top_pos = h
                        break


            # encontrar a parte de baixo da barra de pesca
            for h2 in range(cath_bar_height-20, 1, -1):
                b_p, g_p, r_p  = cath_bar[h2-1:h2, bar_center_x-15:bar_center_x-14][0][0]

                if b_p < 200:
                    count = 0

                    # verify similary sequence of pixel
                    if h2 > 10:
                        for plus in range(1, 4):
                            b_pp, g_pp, r_pp  = cath_bar[h2-plus:(h2-plus)+1, bar_center_x-15:bar_center_x-14][0][0]
                            if b_pp == b_p and g_pp == g_p and r_pp == r_p:
                                count += 1
                    
                    if count >= 3:
                        botton_pos = h2
                        break

            # econtrar peixe
            for hp in range(cath_bar_height):
                b_p, g_p, r_p  = cath_bar[hp:hp+1, bar_center_x-15:bar_center_x-14][0][0]


                if b_p < 70 and g_p < 70 and r_p < 70:
                    fish_pos = hp + 15
                    break

            # encontrar centro da barra verde
            midle_gap = int((botton_pos - top_pos) / 2)
            center_bar_pos = top_pos + midle_gap
            
            # controll green bar
            

            # draw lines for debug
            # top green bar
            cv.line(cath_bar, (bar_center_x - 50, top_pos), (bar_center_x + 50, top_pos), (255, 0, 0), 3)

            # botton green bar
            cv.line(cath_bar, (bar_center_x - 50, botton_pos), (bar_center_x + 50, botton_pos), (255, 0, 0), 3)

            # center green bar
            cv.line(cath_bar, (bar_center_x - 50, center_bar_pos-4), (bar_center_x + 50, center_bar_pos-4), (255, 0, 255), 3)
            cv.line(cath_bar, (bar_center_x - 50, center_bar_pos+4), (bar_center_x + 50, center_bar_pos+4), (255, 0, 255), 3)

            # fish
            cv.line(cath_bar, (bar_center_x - 50, fish_pos), (bar_center_x + 50, fish_pos), (0, 0, 255), 3)


            cv.imshow('cathBar', cath_bar)
            cv.waitKey(1)
        
        else:
            print('fishing done')
            cv.destroyAllWindows()
            break
       


trow()
wait_for_fish()
sleep(1)
cath_fish()