from cuepy import CorsairSDK
import time
import os

def wheel(pos):
    pos = pos % 1280
    """Generate rainbow colors across 0-255 positions."""
    if pos <= 255:
        r = 255-pos
        g = 0
        b = 255
    else:
        pos = pos-256
        if pos <= 255:
            r = 0
            g = pos
            b = 255
        else:
            pos = pos-256
            if pos <= 255:
                r = 0
                g = 255
                b = 255-pos
            else:
                pos = pos-256
                if pos <= 255:
                    r = pos
                    g = 255
                    b = 0
                else:
                    pos = pos-256
                    if pos <= 255:
                        r = 255
                        g = 255-pos
                        b = 0
            
    return [r,g,b]


username = os.getlogin()
path_to_sdk_dll = "C:\\Users\\%s\\Google Drive\\nerd stuff\\keyboard\\CUESDK_2.18.127\\CUESDK\\redist\\i386\\CUESDK_2013.dll" % username
Corsair = CUESDK(path_to_sdk_dll)

print(sdk.device_count())


print(sdk.device_info(0))

device = sdk.device(0)
print(device)


for x in range(1,154):
    print(x)
    for y in range(1,154):
        
        if x == y:
            device.set_led(y, [255,255,255])
        else:
            device.set_led(y, [0,0,0])
        
    input()
    