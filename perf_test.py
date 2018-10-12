import psutil
import time
import keyboard
import os
from cuepy import CorsairSDK

SPEED = 0.05

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
        return [0 , pos , 255]
    elif pos < 510:
        pos -= 255
        return [0 , 255, 255 - pos]
    elif pos < 765:
        pos -= 510
        return [ pos, 255, 0]
    elif pos<=1020:
        pos -= 765
        return [255, 255 - pos, 0]
    else:
        return [255, 0, 0]

keyboard_map = [[154,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,72,97],
                [1,2,3,4,5,6,7,8,9,10,11,12,73,74,75,76,0,0,0,0,0],
                [13,14,15,16,17,18,19,20,21,22,23,24,85,87,77,78,79,103,104,105,106],
                [25,26,27,28,29,30,31,32,33,34,35,36,80,81,88,89,90,109,110,111,107],
                [37,38,39,40,41,42,43,44,45,46,47,48,82,83,0,0,0,113,114,115,0],
                [49,50,51,52,53,54,55,56,57,58,59,60,0,91,0,93,0,116,117,118,108],
                [61,62,63,0,64,0,65,0,66,67,68,147,70,92,94,95,96,119,0,120,0]]

device = setup_keyboard()

for row in keyboard_map:
    for col in row:
         device.set_led(col, (0,0,0))
         
row = len(keyboard_map[1])
print(row)

disk = psutil.disk_io_counters(perdisk=False)
disk_read = disk.read_bytes
disk_write = disk.write_bytes
eth = psutil.net_io_counters(pernic=True)["Ethernet"]
eth_read = eth.bytes_recv
eth_write = eth.bytes_sent

while True:
        if keyboard.is_pressed('ctrl+shift+q'):
            break
        cpu = psutil.cpu_percent()
        print("Cpu: %s" % cpu)
        cpu_num = int(row * (cpu/100.0))
        
        vmem = psutil.virtual_memory().percent
        print("Virtual Memory: %s" % vmem)
        vmem_num = int(row * (vmem/100.0))
        
        smem = psutil.swap_memory().percent
        print("Swap Memory: %s" % smem)
        smem_num = int(row * (smem/100.0))
        
        disk = psutil.disk_io_counters(perdisk=False)
        print("Disk Read: %s Disk Write: %s" % (disk.read_bytes,disk.write_bytes))
        disk_diff = (disk.read_bytes - disk_read) + (disk.write_bytes - disk_write)
        disk_read = disk.read_bytes
        disk_write = disk.write_bytes
        disk_num = int(row * (disk_diff/1000000.0))
        
        eth = psutil.net_io_counters(pernic=True)["Ethernet"]
        print("Net Recv: %s Net Send: %s" % (eth.bytes_recv,eth.bytes_sent))
        eth_diff = (eth.bytes_recv - eth_read) + (eth.bytes_sent - eth_write)
        eth_read = eth.bytes_recv
        eth_write = eth.bytes_sent
        eth_num = int(row * (eth_diff/1000000.0))
        
        for x in range(row):
            cpu_int = int(cpu*10.0)
            if x<cpu_num:
                device.set_led(keyboard_map[1][x], wheel(cpu_int))
            else:
                device.set_led(keyboard_map[1][x], (0,0,0))

            vmem_int = int(vmem*10.0)
            if x<vmem_num:
                device.set_led(keyboard_map[2][x], wheel(vmem_int))
            else:
                device.set_led(keyboard_map[2][x], (0,0,0))
                
            smem_int = int(smem*10.0)
            if x<smem_num:
                device.set_led(keyboard_map[3][x], wheel(smem_int))
            else:
                device.set_led(keyboard_map[3][x], (0,0,0))
                
            disk_int = int(disk_diff/1000.0)
            if x<disk_num:
                device.set_led(keyboard_map[4][x], wheel(disk_int))
            else:
                device.set_led(keyboard_map[4][x], (0,0,0))
                
            eth_int = int(eth_diff/1000.0)
            if x<eth_num:
                device.set_led(keyboard_map[5][x], wheel(eth_int))
            else:
                device.set_led(keyboard_map[5][x], (0,0,0))
        
        
        
        
        print("")
        time.sleep(SPEED)
        