import cv2
import numpy as np
from constants import game_area
from constants import coordinate_of_opposite_player as toimen
from capture import capture_game_screnn, capture_toimen_hand
from capture import extract_toimen_hand
import time
import pyautogui
import datetime

def main():
    for _ in range(50):
        position = pyautogui.position()
        print(position)
        img = capture_toimen_hand()
        #img = capture_game_screnn()
        img = np.array(img)
        #img = extract_toimen_hand(img)
        filename = 'images/sc' + str(int(time.time() * 10000)) + '.png'
        #print(filename)
        cv2.imwrite(filename, img)


if __name__ == '__main__':
    main()
    