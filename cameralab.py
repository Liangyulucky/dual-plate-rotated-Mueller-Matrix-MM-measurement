import sys
import ctypes
from ctypes import *
import os
import numpy as np
from PIL import Image
from MvImport.MvCameraControl_class import *

class Camera:
    def __init__(self):
        self.cam = MvCamera()
        self.handle = None

    def open_camera(self, index=0):
        # 枚举设备
        deviceList = MV_CC_DEVICE_INFO_LIST()
        ret = MvCamera.MV_CC_EnumDevices(MV_GIGE_DEVICE | MV_USB_DEVICE, deviceList)
        if ret != MV_OK or deviceList.nDeviceNum == 0:
            print("未发现设备或枚举失败")
            return False

        # 选择设备
        mvcc_dev_info = cast(deviceList.pDeviceInfo[index], POINTER(MV_CC_DEVICE_INFO)).contents

        # 创建句柄
        ret = self.cam.MV_CC_CreateHandle(mvcc_dev_info)
        if ret != MV_OK:
            print("创建相机句柄失败，错误码：", ret)
            return False

        # 打开设备
        ret = self.cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0)
        if ret != MV_OK:
            print("打开设备失败，错误码：", ret)
            return False

        # 获取 PayloadSize（每帧图像数据大小）
        payload_size = MVCC_INTVALUE()
        memset(byref(payload_size), 0, sizeof(MVCC_INTVALUE))
        ret = self.cam.MV_CC_GetIntValue("PayloadSize", payload_size)
        if ret != MV_OK:
            print("获取 PayloadSize 失败，错误码：", ret)
            return False
        else:
            self.nPayloadSize = payload_size.nCurValue

        return True

    def configure_camera(self, exposure_time=10000.0):
        # 设置触发模式为软触发
        ret = self.cam.MV_CC_SetEnumValue("TriggerMode", MV_TRIGGER_MODE_ON)
        if ret != MV_OK:
            print("设置触发模式失败，错误码：", ret)
            return False

        ret = self.cam.MV_CC_SetEnumValue("TriggerSource", MV_TRIGGER_SOURCE_SOFTWARE)
        if ret != MV_OK:
            print("设置触发源失败，错误码：", ret)
            return False

        # 设置曝光时间
        ret = self.cam.MV_CC_SetFloatValue("ExposureTime", exposure_time)
        if ret != MV_OK:
            print("设置曝光时间失败，错误码：", ret)
            return False

        return True

    def start_grabbing(self):
        # 开始取流
        ret = self.cam.MV_CC_StartGrabbing()
        if ret != MV_OK:
            print("开始取流失败，错误码：", ret)
            return False
        return True

    def stop_grabbing(self):
        # 停止取流
        ret = self.cam.MV_CC_StopGrabbing()
        if ret != MV_OK:
            print("停止取流失败，错误码：", ret)
            return False
        return True

    def close_camera(self):
        # 关闭设备
        ret = self.cam.MV_CC_CloseDevice()
        if ret != MV_OK:
            print("关闭设备失败，错误码：", ret)
            return False

        # 销毁句柄
        ret = self.cam.MV_CC_DestroyHandle()
        if ret != MV_OK:
            print("销毁句柄失败，错误码：", ret)
            return False
        return True

    def capture_image(self):
        # 触发软触发拍照
        ret = self.cam.MV_CC_SetCommandValue("TriggerSoftware")
        if ret != MV_OK:
            print("软触发命令发送失败，错误码：", ret)
            return None

        # 分配足够的内存空间
        data_buf = (c_ubyte * self.nPayloadSize)()
        stFrameInfo = MV_FRAME_OUT_INFO_EX()
        memset(byref(stFrameInfo), 0, sizeof(MV_FRAME_OUT_INFO_EX))

        # 获取一帧图像
        ret = self.cam.MV_CC_GetOneFrameTimeout(data_buf, self.nPayloadSize, stFrameInfo, 1000)
        if ret == MV_OK:
            print(f"成功获取一帧图像，宽度：{stFrameInfo.nWidth}, 高度：{stFrameInfo.nHeight}")
            return data_buf, stFrameInfo
        else:
            print("获取图像失败，错误码：", hex(ret))
            return None


def save_image(data_buf, stFrameInfo, count, save_path):
    # 创建保存路径（如果不存在）
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 将数据转换为 numpy 数组
    data = np.ctypeslib.as_array(data_buf, shape=(stFrameInfo.nFrameLen,))

    # 根据像素格式进行处理，这里假设为 Mono8
    if stFrameInfo.enPixelType == PixelType_Gvsp_Mono8:
        image = data.reshape((stFrameInfo.nHeight, stFrameInfo.nWidth))
        img = Image.fromarray(image)
    else:
        # 如果是其他格式，例如 Bayer，需要进行格式转换
        # 使用 SDK 提供的像素格式转换函数 MV_CC_ConvertPixelType
        # 这里需要根据实际情况实现格式转换
        print("不支持的像素格式，需要进行转换")
        return False

    # 构建完整的保存文件路径
    filename = f"{count}.tif"
    filepath = os.path.join(save_path, filename)

    # 保存图像为 .tif 文件
    img.save(filepath)
    print(f"图像已保存为 {filepath}")
    return True
