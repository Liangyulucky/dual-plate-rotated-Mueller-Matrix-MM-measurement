import time
import os
import sys
from ctypes import *

# 加载 Thorlabs Kinesis 库的路径
kinesis_folder = r"C:\Program Files\Thorlabs\Kinesis"

if sys.version_info < (3, 8):
    os.chdir(kinesis_folder)
else:
    os.add_dll_directory(kinesis_folder)

# 加载库
device_manager = WinDLL("Thorlabs.MotionControl.DeviceManager.dll")
kcubeservo = WinDLL("Thorlabs.MotionControl.KCube.DCServo.dll")

# 加载 DeviceManager 和 KCube Servo DLL
device_manager = WinDLL("Thorlabs.MotionControl.DeviceManager.dll")
kcubeservo = WinDLL("Thorlabs.MotionControl.KCube.DCServo.dll")

# 设置 DeviceManager 函数的参数和返回类型
device_manager.TLI_BuildDeviceList.restype = c_short
device_manager.TLI_GetDeviceListSize.restype = c_short
device_manager.TLI_GetDeviceListExt.argtypes = [POINTER(c_char), c_int]
device_manager.TLI_GetDeviceListExt.restype = None

# 设置 KCube DCServo 函数的参数和返回类型
kcubeservo.CC_Open.argtypes = [c_char_p]
kcubeservo.CC_Open.restype = c_short
kcubeservo.CC_StartPolling.argtypes = [c_char_p, c_int]
kcubeservo.CC_StartPolling.restype = c_short
kcubeservo.CC_StopPolling.argtypes = [c_char_p]
kcubeservo.CC_StopPolling.restype = None
kcubeservo.CC_Close.argtypes = [c_char_p]
kcubeservo.CC_Close.restype = c_short
kcubeservo.CC_ClearMessageQueue.argtypes = [c_char_p]
kcubeservo.CC_ClearMessageQueue.restype = c_short
kcubeservo.CC_Home.argtypes = [c_char_p]
kcubeservo.CC_Home.restype = c_short
kcubeservo.CC_MoveToPosition.argtypes = [c_char_p, c_int]
kcubeservo.CC_MoveToPosition.restype = c_short
kcubeservo.CC_RequestStatusBits.argtypes = [c_char_p]
kcubeservo.CC_RequestStatusBits.restype = c_short
kcubeservo.CC_GetStatusBits.argtypes = [c_char_p]
kcubeservo.CC_GetStatusBits.restype = c_ulong
kcubeservo.CC_RequestPosition.argtypes = [c_char_p]
kcubeservo.CC_RequestPosition.restype = c_short
kcubeservo.CC_GetPosition.argtypes = [c_char_p]
kcubeservo.CC_GetPosition.restype = c_int
kcubeservo.CC_SetVelParams.argtypes = [c_char_p, c_double, c_double, c_double]
kcubeservo.CC_SetVelParams.restype = c_short
kcubeservo.CC_StopImmediate.argtypes = [c_char_p]
kcubeservo.CC_StopImmediate.restype = c_short

def initialize_device(serial_num):
    # 构建设备列表
    ret = device_manager.TLI_BuildDeviceList()
    if ret != 0:
        print(f"TLI_BuildDeviceList failed with error code: {ret}")
        return False

    buffer_size = 1024
    buffer = create_string_buffer(buffer_size)
    device_manager.TLI_GetDeviceListExt(buffer, buffer_size)

    devices_str = buffer.value.decode('utf-8', errors='ignore')
    devices = devices_str.strip().split(',')
    if serial_num.value.decode('utf-8') not in devices:
        print("未找到指定的设备")
        return False

    if kcubeservo.CC_Open(serial_num) != 0:
        print("无法打开设备")
        return False

    print("设备已成功打开")
    kcubeservo.CC_StartPolling(serial_num, c_int(500))
    kcubeservo.CC_ClearMessageQueue(serial_num)
    time.sleep(1)
    return True


def close_device(serial_num):
    kcubeservo.CC_StopPolling(serial_num)
    kcubeservo.CC_Close(serial_num)
    print("设备已关闭")


def home_device(serial_num):
    print("正在归零设备...")
    kcubeservo.CC_Home(serial_num)

    homing_complete = False
    while not homing_complete:
        kcubeservo.CC_RequestStatusBits(serial_num)
        status = kcubeservo.CC_GetStatusBits(serial_num)
        homing_complete = (status & 0x00000400) != 0  # 检查Homing完成位
        time.sleep(0.1)

    print("归零完成")
