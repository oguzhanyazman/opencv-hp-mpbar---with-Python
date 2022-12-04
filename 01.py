import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from PIL import Image
import cv2
import numpy as np
import time
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('Knight Evolution')


while(True):


    screenshot = wincap.get_screenshot()
    hpbar = screenshot[30: 50, 15: 220]
    mpbar = screenshot[50: 70, 15: 220]

    cv.imshow('hpbar', hpbar)
    cv.imshow('mpbar', mpbar)
    



    #print('FPS {}'.format(1 / (time() - loop_time)))
    #loop_time = time()


    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
