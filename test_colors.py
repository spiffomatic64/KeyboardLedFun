import os
from cuepy import CorsairSDK

username = os.getlogin()
path_to_sdk_dll = "C:\\Users\\%s\\Google Drive\\nerd stuff\\keyboard\\CUESDK_2.18.127\\CUESDK\\redist\\i386\\CUESDK_2013.dll" % username
sdk = CorsairSDK(path_to_sdk_dll)

sdk.device_count()

sdk.device_info(0)

device = sdk.device(0)


for key in range(1,200):
    print(key)
    for keys in range(1,200):
        if keys == key:
            device.set_led(keys, [255,0,0])
        else:
            device.set_led(keys, [0,0,0])
        
    input()