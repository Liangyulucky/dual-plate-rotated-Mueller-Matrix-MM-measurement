from device_control import *
# 设置速度参数

def set_velocity(serial_num, min_vel = c_double(50.0), accel = c_double(50.0), max_vel = c_double(100.0)):
    kcubeservo.CC_SetVelParams(serial_num, min_vel, accel, max_vel)


# 移动电机到目标角度位置
def move_to_position(serial_num, target_angle, counts_per_degree = 1919.6, tolerance=50):
    position = c_int(int(target_angle * counts_per_degree))
    kcubeservo.CC_MoveToPosition(serial_num, position)

    moving = True
    while moving:
        kcubeservo.CC_RequestPosition(serial_num)
        current_position = kcubeservo.CC_GetPosition(serial_num)
        # current_angle = current_position / counts_per_degree
        # print(f"当前计数值: {current_position}, 目标计数值: {position.value}, 当前角度: {current_angle % 360}")

        if abs(current_position - position.value) <= tolerance:
            # print("已到达目标位置，正在停止电机...")
            moving = False
        else:
            time.sleep(0.5)

    kcubeservo.CC_StopImmediate(serial_num)
    time.sleep(0.5)


# 获取当前位置
def get_current_position(serial_num, counts_per_degree = 1919.6):
    kcubeservo.CC_RequestPosition(serial_num)
    current_position = kcubeservo.CC_GetPosition(serial_num)
    return current_position / counts_per_degree
