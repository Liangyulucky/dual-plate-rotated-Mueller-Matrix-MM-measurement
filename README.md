# Dual-rotating-retarder Mueller Matrix Measurement System
# 双波片旋转缪勒矩阵测量系统

[English](#english) | [中文](#中文)

---

<a name="english"></a>
# English Version

## Project Overview
This project implements a dual-rotating-retarder polarization measurement system, utilizing Thorlabs KDC101 drivers and PRM1Z8 motorized rotation stages to automatically control the Polarization State Generator (PSG) and Polarization State Analyzer (PSA). It captures images using a Hikvision industrial camera for analysis and calculation of the sample's Mueller matrix.

## Theoretical Foundation
The design and implementation of this project are based on the following research paper:

Deng, L.; Fan, Z.; Chen, B.; Zhai, H.; He, H.; He, C.; Sun, Y.; Wang, Y.; Ma, H. A Dual-Modality Imaging Method Based on Polarimetry and Second Harmonic Generation for Characterization and Evaluation of Skin Tissue Structures. Int. J. Mol. Sci. 2023, 24, 4206. https://doi.org/10.3390/ijms24044206

This paper introduces a dual-modality imaging method based on polarimetry and second harmonic generation for characterizing and evaluating skin tissue structures. Our project adopts the dual-rotating-retarder Mueller matrix measurement technique from this method.

## System Optical Path Diagram
The following diagram illustrates the hardware optical path of our system:
(https://github.com/user-attachments/assets/a2a7ec71-af6b-48cd-bc1e-af99b53bdec8)
*Figure 1: Hardware optical path diagram of the dual-rotating-retarder Mueller matrix measurement system*

In this setup:
1. Light from the source first passes through the Polarization State Generator (PSG)
2. The light then passes through the sample
3. Next, the light passes through the Polarization State Analyzer (PSA)
4. Finally, the image is captured by a Hikvision industrial camera

Both PSG and PSA are controlled by Thorlabs PRM1Z8 motorized rotation stages and KDC101 drivers, allowing precise angle adjustments.

## Key Features
1. Control of PRM1Z8 motorized rotation stages to specified angles using Thorlabs KDC101 drivers
2. Image capture using Hikvision industrial camera
3. Multi-threaded operation for parallel control and image capture
4. Data storage in a specified directory

## Hardware Requirements
- 2x Thorlabs KDC101 drivers
- 2x Thorlabs PRM1Z8 motorized rotation stages (for PSG and PSA)
- Hikvision industrial camera (generic model)

## Software Requirements
- Python 3.10
- Thorlabs Kinesis software (including SDK library)
- Required Python libraries:
  - threading
  - time
  - ctypes (for loading Thorlabs SDK)
  - cv2 (OpenCV, for image capture)

## Installation Steps
1. Ensure Python 3.10 is installed
2. Install required Python libraries
3. Install Thorlabs Kinesis software:
   - Download and install Kinesis software from the Thorlabs website
   - Default installation path is `C:\Program Files\Thorlabs\Kinesis`
   - Installing Kinesis software automatically includes the required SDK library
4. Hikvision camera SDK is included in MvImport and doesn't require separate installation

## Usage
1. Connect Thorlabs KDC101 drivers to the computer and PRM1Z8 motorized rotation stages to the drivers
2. Ensure the Hikvision industrial camera is properly connected and recognized by the system
3. Set the correct serial numbers and initial angles
4. Run the main program:
```
python main.py
````
5. The program will automatically control PSG and PSA motor rotations and capture images at each angle combination

## Configuration
Before running the program, ensure the following parameters are correctly set:

- `serial_num_PSG`: Serial number of the KDC101 driver for PSG
- `serial_num_PSA`: Serial number of the KDC101 driver for PSA
- `initial_angle_PSG`: Initial angle of PSG
- `initial_angle_PSA`: Initial angle of PSA
- `target_angles_PSG`: List of target angles for PSG
- `target_angles_PSA`: List of target angles for PSA
- `path`: Directory for image and data storage

## Notes
- Ensure the `Data` folder exists in the program's running directory, or the program will create it automatically
- The program uses multi-threading; ensure your system supports concurrent operations
- Image capture may take some time; please be patient while the program completes
- When using Thorlabs devices, follow all manufacturer safety guidelines and operating instructions
- If you modified the Thorlabs Kinesis software installation path, update the SDK path in `device_control.py`. The default path is:
  ```
  kinesis_folder = r"C:\Program Files\Thorlabs\Kinesis"
  ```

## Troubleshooting
If you encounter device communication issues, check:
1. KDC101 driver serial numbers are correct
2. Driver and motor connections are stable
3. Thorlabs Kinesis software and SDK are correctly installed
4. No other programs are occupying the serial ports

If image capture fails, confirm:
1. Hikvision camera is properly connected
2. Camera drivers are correctly installed

## Thorlabs Resources
- [KDC101 Driver User Manual](https://www.thorlabs.com/thorproduct.cfm?partnumber=KDC101)
- [PRM1Z8 Motorized Rotation Stage User Manual](https://www.thorlabs.com/thorproduct.cfm?partnumber=PRM1Z8)
- [Thorlabs Kinesis Software Download](https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=Motion_Control)
- [Thorlabs Technical Support](https://www.thorlabs.com/support.cfm)

## Hikvision Resources
- [Hikvision Industrial Camera Product Page](https://www.hikrobotics.com/en/machinevision/visionproduct)
- [Hikvision Technical Support](https://www.hikrobotics.com/en/support)

## References
Deng, L.; Fan, Z.; Chen, B.; Zhai, H.; He, H.; He, C.; Sun, Y.; Wang, Y.; Ma, H. A Dual-Modality Imaging Method Based on Polarimetry and Second Harmonic Generation for Characterization and Evaluation of Skin Tissue Structures. Int. J. Mol. Sci. 2023, 24, 4206. https://doi.org/10.3390/ijms24044206

## Contact
For any questions or suggestions, please contact liangyu_deng@163.com

---

<a name="中文"></a>
# 中文版本

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
如有任何问题或建议，请联系 liangyu_deng@163.com
