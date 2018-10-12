from cue_sdk import *
import os

# Load CUE DLL. Provide path to DLL yourself.
username = os.getlogin()
path_to_sdk_dll = "C:\\Users\\%s\\Google Drive\\nerd stuff\\keyboard\\CUESDK_2.18.127\\CUESDK\\redist\\i386\\CUESDK_2013.dll" % username
Corsair = CUESDK(path_to_sdk_dll)
# Gives us exclusive access to controling the lighting and turns everything off.
Corsair.RequestControl(CAM.ExclusiveLightingControl)

# Sets the color of the H key to white.
Corsair.SetLedsColors(CorsairLedColor(CLK.H, 255, 255, 255))

# Sets the color of the A and B key to green
Corsair.SetLedsColors([CorsairLedColor(CLK.A, 0, 255, 0), CorsairLedColor(CLK.B, 0, 255, 0)])

# Define a callback function for SetLedsColorsAsync
def example_callback(context, result, error):
    assert context == "test123"
    print(context, result, error)

# Asynchronously set the color of the E key to white. Pass in a callback and an arbitrary context.
Corsair.SetLedsColorsAsync(CorsairLedColor(CLK.E, 255, 255, 255), example_callback, "test123")

# (Note: The appears before the result because it's async.)
# Returns number of Corsair devices.
Corsair.GetDeviceCount()

# Takes zero-based index of device and returns a namedtuple with the device info.
Corsair.GetDeviceInfo(0)

# Returns a named tuple with the led positions + count of the keyboard.
Corsair.GetLedPositions(0)

# Returns the led id (CLK enum) for the key name. Relative to logical layout (e.g. on an AZERTY keyboard it will return Q, not A)
Corsair.GetLedIdForKeyName('a')

# Performs protocol handshake and returns details. Already called when the CUE class is initialized, no need to call for it yourself.
Corsair.PerformProtocolHandshake()

# Protocol details are stored here when called handshake is performed on init.
Corsair.ProtocolDetails

# Release control back to CUE.
Corsair.ReleaseControl(CAM.ExclusiveLightingControl)
