from threadingclass import *
from cameralab import *

def main():

    #打开相机
    camera = Camera()
    if not camera.open_camera():
        sys.exit()
    if not camera.configure_camera(exposure_time=800):
        sys.exit()
    if not camera.start_grabbing():
        sys.exit()

    # 两个设备的序列号
    serial_num_PSG = c_char_p(b"27256947")  # 第一个设备序列号27256947
    serial_num_PSA = c_char_p(b"27004239")  # 第二个设备序列号27004239

    # 创建同步屏障
    barrier = threading.Barrier(2)

    initialize_device_thread(serial_num_PSG, device_name="PSG")
    initialize_device_thread(serial_num_PSA, device_name="PSA")

    print("所有设备初始化完成，开始同步移动和拍照...")

    initial_angle_PSG = 110
    initial_angle_PSA = 85
    points = 31
    path = 'D:\dual-plate MM measurement\dual-plate MM measurement\Air_Data'

    # 设置角度序列
    interval_PSG = 6
    angles_PSG = list(range(0, (points - 1) * interval_PSG + 1, interval_PSG))
    target_angles_PSG = [(angle + initial_angle_PSG) for angle in angles_PSG]

    interval_PSA = 5 * interval_PSG
    angles_PSA = list(range(0, (points - 1) * interval_PSA + 1, interval_PSA))
    target_angles_PSA = [(angle + initial_angle_PSA) for angle in angles_PSA]

    ### 第二部分：设备同步移动和拍照 - 使用线程
    thread_PSG = threading.Thread(target=control_device, args=(serial_num_PSG, target_angles_PSG, initial_angle_PSG, "设备PSG",path, camera,barrier))
    thread_PSA = threading.Thread(target=control_device, args=(serial_num_PSA, target_angles_PSA, initial_angle_PSA, "设备PSA",path, camera,barrier))

    # 启动移动和拍照线程
    thread_PSG.start()
    thread_PSA.start()

    # 等待所有移动线程完成
    thread_PSG.join()
    thread_PSA.join()

    print("所有设备操作已完成")

    # 关闭设备
    camera.stop_grabbing()
    camera.close_camera()

    close_device(serial_num_PSG)
    close_device(serial_num_PSA)

if __name__ == "__main__":
    main()