#GAME: https://fishington.io/
#Inspiration: https://www.youtube.com/watch?v=X2bRXcCvmKY
from bot import Commands

import threading
from time import sleep

fisher = Commands(8, 10)

def loop():
    run = True

    fisher.move(True)
    fisher.move(False)

    while run:
        img = fisher.screen_shot()
        run = fisher.show_img(img)


#threading.Thread(target=loop).start

sleep(2)
loop()

""" while True:
    print("running")
    sleep(.5) """