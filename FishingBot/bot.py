import sys
import time
from cv2 import cv2
import numpy as np
import mss
from PIL import Image
import pyautogui

#from pynput.keyboard import Key, Controller
#from pynput.mouse import Button, Controller as MController
import os
from win32api import GetSystemMetrics

class Commands():
    def __init__(self, capacity: int, catch_interval: int) -> None:
        self.capacity = capacity
        self.catch_interval = catch_interval

        self.x = GetSystemMetrics(0)
        self.y = GetSystemMetrics(1)
        self.capture = {"origin": [int((self.y * 0.725)), int((self.x * 0.34))], "size": []}
        
        #print("top:", self.capture["origin"][0],"left:" , self.capture["origin"][1], "width", self.capture["origin"][1] + 620, "height", self.capture["origin"][0] + 85)
        #recorded = from(650, 777), to(1266, 868) | settings = top: 783 left: 652 width 1272 height 868
        
        self.meter = {"top": self.capture["origin"][0], "left": self.capture["origin"][1] ,"width": 620, "height": 85}
        self.scr = mss.mss()

        #self.keyboard = Controller()
        #self.mouse = MController()

    def screen_shot(self):
        #print("Taking a screen shot")

        scr_img = self.scr.grab(self.meter)
        img = np.array(scr_img)
        img = cv2.cvtColor(img, cv2.IMREAD_COLOR)

        return img
    
    def show_img(self, img) -> None:
        cv2.imshow("capture", np.array(img))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            return False
        return True
    
    def sell_fish(self):
        pass

    def move(self, shop: bool) -> None: # move to shop if the shop var is True
        key = "W" if shop else "S"

        pyautogui.keyDown(key)
        time.sleep(1)
        pyautogui.keyUp(key)
    
    def sell(self):
        self.move(True)
        self.sell_fish()
        self.move(False)