import cv2
from cuepy import CorsairSDK
import os

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

username = os.getlogin()
path_to_sdk_dll = "C:\\Users\\%s\\Google Drive\\nerd stuff\\keyboard\\CUESDK_2.18.127\\CUESDK\\redist\\i386\\CUESDK_2013.dll" % username
sdk = CorsairSDK(path_to_sdk_dll) # eg. "C:\\cuesdk\\CUESDK.x64_2013.dll"
device = sdk.device(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
    
keyboard_map = [[154,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,72,97],
                [1,2,3,4,5,6,7,8,9,10,11,12,73,74,75,76,0,0,0,0,0],
                [13,14,15,16,17,18,19,20,21,22,23,24,85,87,77,78,79,103,104,105,106],
                [25,26,27,28,29,30,31,32,33,34,35,36,80,81,88,89,90,109,110,111,107],
                [37,38,39,40,41,42,43,44,45,46,47,48,82,83,0,0,0,113,114,115,0],
                [49,50,51,52,53,54,55,56,57,58,59,60,0,91,0,93,0,116,117,118,108],
                [61,62,63,0,64,0,65,0,66,67,68,147,70,92,94,95,96,119,0,120,0]]

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    for x in range(0,20):
        for y in range(0,6):
            tempx=(30*x)
            tempy=(80*y)
            #print(tempx,tempy)
            key = keyboard_map[y][x]
            color = frame[tempy][tempx]
            #print(color) bgr rgb
            tempcolor = [color[2],color[1],color[0]]
            device.set_led(key,tempcolor)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    if key == 32:
        sat = vc.get(12)
        print(sat)
        vc.set(12,sat-10)
        sat = vc.get(12)
        print(sat)
cv2.destroyWindow("preview")