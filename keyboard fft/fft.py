#!/usr/bin/env python

import sys
from recorder import *
import signal
import math
from cuepy import CorsairSDK
import os
import keyboard
import time

SPEED = 0.05

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
while 0 in keyboard_map_list:
    keyboard_map_list.remove(0)
LED_COUNT = len(keyboard_map_list)
print("LED_COUNT: %s" % LED_COUNT)

def setup_keyboard():
    username = os.getlogin()
    path_to_sdk_dll = "C:\\Users\\%s\\Google Drive\\nerd stuff\\keyboard\\CUESDK_2.18.127\\CUESDK\\redist\\i386\\CUESDK_2013.dll" % username
    sdk = CorsairSDK(path_to_sdk_dll)

    sdk.device_count()

    sdk.device_info(0)

    device = sdk.device(0)
    
    return device

def wheel(pos):
    """b->g->r color wheel from 0 to 1020, neopixels use grb format"""
    
    if pos < 255:
        return [pos , 0 , 255]
    elif pos < 510:
        pos -= 255
        return [255 , 0, 255 - pos ]
    elif pos < 765:
        pos -= 510
        return [255 , pos, 0]
    elif pos<=1020:
        pos -= 765
        return [255 - pos, 255, 0]
    else:
        return [0, 255, 0]

if __name__ == "__main__":
    
    SR=SwhRecorder()
    SR.setup(3,1)
    SR.continuousStart()
    
    leds = []
    for led in range(LED_COUNT):
        leds.append(0)
        
    device = setup_keyboard()
    max_led_num = 0
    
    while True:
        try:
            if keyboard.is_pressed('ctrl+shift+q'):
                break
            xs,ys = SR.fft(trimBy=False)
            #print("%d,%d" % (xs.size,ys.size))

            for led in range(LED_COUNT):
                led_num = int(led * (led/22.0))
                #print(led_num)
                if led_num > max_led_num:
                    max_led_num = led_num
                db = int(ys[led_num]/(10-(led/12))) * 3
                if db > leds[led]:
                    leds[led] = db
                else:
                    leds[led] = int((leds[led] * 4 + db) / 5 )
                #print(led, wheel(leds[led] ))
                device.set_led(keyboard_map_list[led], wheel(leds[led]))
            
            #print min(ys),max(ys)
            time.sleep(SPEED)
        except Exception as e:
            print("yay")
            print(e)
    print("done")
    print(max_led_num)
    SR.continuousEnd()