#114 171
import time

from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *

class DinoBot:
    def __init__(self, replaybtn, dino):
        self.replaybtn = replaybtn
        self.dino = dino
        self.counter = 0

    def restartgame(self):
        pyautogui.click(self.replaybtn)

    def jump(self):
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyUp('space')

    def grabImage(self):
        box = (self.dino[0] + 35, self.dino[1], self.dino[0] + 75, self.dino[1] + 30)
        image = ImageGrab.grab(box)
        grayImage = ImageOps.grayscale(image)
        a = array(grayImage.getcolors())
        return a.sum()

    def start(self):
        self.restartgame()
        while True:
            self.counter += 1
            print(self.counter)
            print(f"coord = {self.grabImage()}")
            if self.grabImage() != 1530 and self.counter > 213:
                self.jump()
                time.sleep(0.3)
                pyautogui.keyDown("down")
                time.sleep(0.1)
                pyautogui.keyUp("down")
            elif self.grabImage() != 1530:
                self.jump()

def main():
    bot = DinoBot((416 , 561), (170, 572 ))
    bot.start()

if __name__ == "__main__":
    main()