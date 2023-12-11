###########################trial creation################

import cv2
import pickle
import os
import face_recognition

#importing the students images
folderPath = "images"
pathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    imgList.append(os.path.splitext(path)[0])
    # print(path)
    # print(os.path.splitext(path)[0])

print(studentIds)

def findEncodings(imagesList):
    encodeList = []

    for image in imagesList:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(image)[0]
        encodeList.append(encode)

    return encodeList
print("Encoding Started.........")
encodeListKnown = findEncodings(imgList)
print(encodeListKnown)
print("Encoding Complete")
