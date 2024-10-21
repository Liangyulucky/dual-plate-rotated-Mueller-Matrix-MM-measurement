# Dual-rotating-retarder Mueller Matrix measurement





# 双波片旋转缪勒矩阵测量系统

## 项目概述
这个项目实现了一个双板偏振测量系统，使用 Thorlabs KDC101 驱动器和 PRM1Z8 电动旋转位移台来自动化控制偏振态发生器（PSG）和偏振态分析仪（PSA），并通过海康威视工业相机捕获图像进行分析计算出样本Mueller矩阵。

## 理论基础
本项目的设计和实现基于以下研究论文：

Deng, L.; Fan, Z.; Chen, B.; Zhai, H.; He, H.; He, C.; Sun, Y.; Wang, Y.; Ma, H. A Dual-Modality Imaging Method Based on Polarimetry and Second Harmonic Generation for Characterization and Evaluation of Skin Tissue Structures. Int. J. Mol. Sci. 2023, 24, 4206. https://doi.org/10.3390/ijms24044206

这篇论文介绍了一种基于偏振和二次谐波生成的双模态成像方法，用于表征和评估皮肤组织结构。我们的项目借鉴了这种方法中的双波片旋转缪勒矩阵测量技术。

## 系统光路图
下图展示了本系统的硬件光路示意图：
(https://github.com/user-attachments/assets/a2a7ec71-af6b-48cd-bc1e-af99b53bdec8)
*图 1: 双波片旋转缪勒矩阵测量系统的硬件光路示意图*

在这个设置中：
1. 光源发出的光线首先通过偏振态发生器（PSG）
2. 然后光线穿过样品
3. 接着光线通过偏振态分析仪（PSA）
4. 最后由海康威视工业相机捕获图像

PSG 和 PSA 都由 Thorlabs PRM1Z8 电动旋转位移台和 KDC101 驱动器控制，可以精确调整角度。


## 主要功能
1. 使用 Thorlabs KDC101 驱动器控制 PRM1Z8 电动旋转位移台旋转到指定角度
2. 使用海康威视工业相机捕获图像
3. 多线程操作以实现并行控制和图像捕获
4. 数据保存到指定目录

## 硬件要求
- 2x Thorlabs KDC101 驱动器
- 2x Thorlabs PRM1Z8 电动旋转位移台（用于 PSG 和 PSA）
- 海康威视工业相机（通用型号）

## 软件要求
- Python 3.10
- Thorlabs Kinesis 软件（包含 SDK 库）
- 所需的Python库：
  - threading
  - time
  - ctypes（用于加载 Thorlabs SDK）
  - cv2 (OpenCV，用于图像捕获)

## 安装步骤
1. 确保已安装 Python 3.10
2. 安装所需的 Python 库：
3. 安装 Thorlabs Kinesis 软件：
   - 从 Thorlabs 官网下载并安装 Kinesis 软件
   - 默认安装路径为 `C:\Program Files\Thorlabs\Kinesis`
   - 安装 Kinesis 软件会自动包含所需的 SDK 库
4. 海康威视相机SDK库已包含在MvImport中不需要额外安装

## 使用方法
1. 连接 Thorlabs KDC101 驱动器到计算机，并连接 PRM1Z8 电动旋转位移台到驱动器。
2. 确保海康威视工业相机正确连接并被系统识别。
3. 设置正确的串口号和初始角度。
4. 运行主程序：
```
python main.py
````
5. 程序将自动控制 PSG 和 PSA 电机旋转，并在每个角度组合下捕获图像。

## 配置
在运行程序之前，请确保正确设置以下参数：

- `serial_num_PSG`：PSG 设备的 KDC101 驱动器串口号
- `serial_num_PSA`：PSA 设备的 KDC101 驱动器串口号
- `initial_angle_PSG`：PSG 的初始角度
- `initial_angle_PSA`：PSA 的初始角度
- `target_angles_PSG`：PSG 的目标角度列表
- `target_angles_PSA`：PSA 的目标角度列表
- `path`：图像和数据保存的目录

## 注意事项
- 确保 `Data` 文件夹存在于程序运行目录下，或者程序会自动创建它。
- 程序使用多线程，确保您的系统支持并发操作。
- 相机捕获可能需要一定时间，请耐心等待程序完成。
- 使用 Thorlabs 设备时，请遵循制造商的所有安全指南和操作说明。
- 如果修改了 Thorlabs Kinesis 软件的安装路径，需要在 `device_control.py` 文件中更新 SDK 的路径。默认路径为：
  ```
  kinesis_folder = r"C:\Program Files\Thorlabs\Kinesis"
  ```

## 故障排除
如果遇到设备通信问题，请检查：
1. KDC101 驱动器的串口号是否正确
2. 驱动器和电机连接是否稳定
3. Thorlabs Kinesis 软件和 SDK 是否正确安装
4. 是否有其他程序占用了串口

如果图像捕获失败，请确认：
1. 海康威视相机连接是否正常
2. 相机驱动是否正确安装

## Thorlabs 资源
- [KDC101 驱动器用户手册](https://www.thorlabs.com/thorproduct.cfm?partnumber=KDC101)
- [PRM1Z8 电动旋转位移台用户手册](https://www.thorlabs.com/thorproduct.cfm?partnumber=PRM1Z8)
- [Thorlabs Kinesis 软件下载](https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=Motion_Control)
- [Thorlabs 技术支持](https://www.thorlabs.com/support.cfm)

## 海康威视资源
- [海康威视工业相机产品页面](https://www.hikrobotics.com/cn/machinevision/visionproduct)
- [海康威视技术支持](https://www.hikrobotics.com/cn/support)

## 参考文献
Deng, L.; Fan, Z.; Chen, B.; Zhai, H.; He, H.; He, C.; Sun, Y.; Wang, Y.; Ma, H. A Dual-Modality Imaging Method Based on Polarimetry and Second Harmonic Generation for Characterization and Evaluation of Skin Tissue Structures. Int. J. Mol. Sci. 2023, 24, 4206. https://doi.org/10.3390/ijms24044206

## 联系方式
如有任何问题或建议，请联系liangyu_deng@163.com




















# 双波片旋转缪勒矩阵测量系统

## 项目概述
这个项目实现了一个双波片旋转缪勒矩阵测量系统，用于自动化控制偏振态发生器（PSG）和偏振态分析仪（PSA），并通过相机捕获图像进行分析。

## 主要功能
1. 控制 PSG 和 PSA 设备旋转到指定角度
2. 使用相机捕获图像
3. 多线程操作以实现并行控制和图像捕获
4. 数据保存到指定目录

## 系统要求
- Python 3.10
- 所需的Python库：
  - threading
  - time
  - serial
  - cv2 (OpenCV)

## 使用方法
1. 确保所有必要的硬件（PSG、PSA、相机）已正确连接。
2. 设置正确的串口号和初始角度。
3. 运行主程序：python main.py
4. 程序将自动控制 PSG 和 PSA 旋转，并在每个角度组合下捕获图像。

## 配置
在运行程序之前，请确保正确设置以下参数：

- `serial_num_PSG`：PSG 设备的串口号
- `serial_num_PSA`：PSA 设备的串口号
- `initial_angle_PSG`：PSG 的初始角度
- `initial_angle_PSA`：PSA 的初始角度
- `target_angles_PSG`：PSG 的目标角度列表
- `target_angles_PSA`：PSA 的目标角度列表
- `path`：图像和数据保存的目录

## 注意事项
- 确保 `Data` 文件夹存在于程序运行目录下，或者程序会自动创建它。
- 程序使用多线程，确保您的系统支持并发操作。
- 相机捕获可能需要一定时间，请耐心等待程序完成。

## 故障排除
如果遇到设备通信问题，请检查：
1. 串口号是否正确
2. 设备连接是否稳定
3. 是否有其他程序占用了串口

如果图像捕获失败，请确认：
1. 相机连接是否正常
2. 相机驱动是否正确安装

## 联系方式
如有任何问题或建议，请联系liangyu_deng@163.com


