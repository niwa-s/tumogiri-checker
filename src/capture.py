import cv2
import pyautogui
import numpy as np
from constants import game_area
from constants import coordinate_of_opposite_player as toimen

def extract_toimen_hand(img):
    left = toimen["left"] - game_area["left"]
    top = toimen["top"] - game_area["top"]
    toimen_img = img[top:top+toimen['height'], left:left+toimen['width']]
    return toimen_img

def capture_game_screnn():
    img = pyautogui.screenshot(region=(game_area["left"], game_area["top"], game_area["right"], game_area["bottom"]))
    return img

def capture_toimen_hand():
    img = pyautogui.screenshot(region=(toimen["left"], toimen["top"], toimen["width"], toimen["height"]))
    return img

def capture_game_screnn_and_save(filename):
    position = pyautogui.position()
    print(position)
    img = pyautogui.screenshot(filename, region=(game_area["left"],game_area["top"],game_area["right"],game_area["bottom"]))
    return img
