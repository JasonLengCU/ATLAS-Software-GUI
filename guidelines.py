import numpy as np
import cv2

cv2.namedWindow("preview",0)
cv2.startWindowThread()
#vc stands for video capture
vc = cv2.VideoCapture(0)


from kivy.logger import Logger
import logging
Logger.setLevel(logging.TRACE)


if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
while rval:
    # Set properties. Each returns === True on success (i.e. correct resolution)
    vc.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
    vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    else:
        cv2.circle(img=frame, center=(300,300), radius=100, color=(0,255,0), thickness =10)
        cv2.rectangle(img=frame, pt1 = (150, 150) , pt2 = (350, 350) , color=(0,255,0), thickness =10)
vc.release()
#close window by pressing esc (may have to press twice);
#was not closing correctly on my mac;
#this may just be needed for macs idk
cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)
