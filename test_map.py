import os
from cuepy import CorsairSDK

username = os.getlogin()
path_to_sdk_dll = "C:\\Users\\%s\\Google Drive\\nerd stuff\\keyboard\\CUESDK_2.18.127\\CUESDK\\redist\\i386\\CUESDK_2013.dll" % username
sdk = CorsairSDK(path_to_sdk_dll)

sdk.device_count()

sdk.device_info(0)

device = sdk.device(0)

keyboard_map = [[154,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,72,97],
                [1,2,3,4,5,6,7,8,9,10,11,12,73,74,75,76,0,0,0,0,0],
                [13,14,15,16,17,18,19,20,21,22,23,24,85,87,77,78,79,103,104,105,106],
                [25,26,27,28,29,30,31,32,33,34,35,36,80,81,88,89,90,109,110,111,107],
                [37,38,39,40,41,42,43,44,45,46,47,48,82,83,0,0,0,113,114,115,0],
                [49,50,51,52,53,54,55,56,57,58,59,60,0,91,0,93,0,116,117,118,108],
                [61,62,63,0,64,0,65,0,66,67,68,147,70,92,94,95,96,119,0,120,0]]
keyboard_map_list = []
for y in range(0,len(keyboard_map)):
    for x in range(0,len(keyboard_map[y])):
        keyboard_map_list.append(keyboard_map[y][x])
        
keyboard_map_list = sorted(keyboard_map_list)

for y in range(0,len(keyboard_map)):
    for x in range(0,len(keyboard_map[y])):
        key = keyboard_map[y][x]
        for k in keyboard_map_list:
            if k == key:
                device.set_led(k, [255,0,0])
            else:
                device.set_led(k, [0,0,0])
                
        input()
        

