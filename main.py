#the mhindi
import os

import cv2

cap = cv2.VideoCapture(0)
#the width below
cap.set(3,640)
#the height
cap.set(4, 480)

imgBack = cv2.imread("Resources/backg.png")
#the path of the modes
folderModePath = 'Resources/Modes'
#if you print this, it brings out the list of images in this path
modePath = os.listdir(folderModePath)
imgModeList = []
for path in modePath:
    imgModeList.append(cv2.imread(os.path.join(folderModePath)))



while True:
    success, img = cap.read()

    imgBack[162:162+480,55:55+640] = img
    # imgBack[44:44+633, 808:808 + 414] = int(imgModeList[1] or 0)

    #we are now bringing in the modes

    #displays the webcam
    # cv2.imshow("Webcam", img)
    #displays the graphics
    cv2.imshow("Face Attendance", imgBack)
    cv2.waitKey(1)