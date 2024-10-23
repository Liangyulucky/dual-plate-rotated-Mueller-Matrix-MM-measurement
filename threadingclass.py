import threading
from movement_control import *
from device_control import *
from cameralab import *

def initialize_device_thread(serial_num, device_name):
    # 初始化设备
    if not initialize_device(serial_num):
        return
    home_device(serial_num)
    set_velocity(serial_num)
    print(f"{device_name} 初始化完成")

def control_device_PSG(serial_num, target_angles, initial_angle, device_name, path, camera,barrier):
    # 移动到初始角度
    move_to_position(serial_num, initial_angle)

    # 移动到目标角度
    for angle in target_angles:
        # 移动到目标角度
        move_to_position(serial_num, angle)
        current_angle = get_current_position(serial_num)
        print(f"{device_name} 已到达角度：{current_angle % 360:.2f} 度")

        # 设备到达目标角度后等待同步
        barrier.wait()  # 等待其他设备同步
        time.sleep(0.5) # 等待相机采样

def control_device_PSA(serial_num, target_angles, initial_angle, device_name, path, camera,barrier):
    # 移动到初始角度
    move_to_position(serial_num, initial_angle)
    count = 1

    # 移动到目标角度
    for angle in target_angles:
        # 移动到目标角度
        move_to_position(serial_num, angle)
        current_angle = get_current_position(serial_num)
        print(f"{device_name} 已到达角度：{current_angle % 360:.2f} 度")
        barrier.wait()
        print("所有设备已到达目标位置，正在拍照...")           
        result = camera.capture_image()
        data_buf, stFrameInfo = result
        # 保存图像
        save_image(data_buf, stFrameInfo, count, path)
        count += 1
        # 设备到达目标角度后等待同步

