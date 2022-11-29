1. 环境要求
教师端：2个HDMI摄像头（HDMI_CAM_0、CAM_1），1个IPC网络摄像头用于拉流
学生端：1个HDMI摄像头（HDMI_CAM_1）
显示器要求：分辨率1920*1080

2. 脚本执行方式为:
python 脚本名.py  

教师端:
SSH 当前小站 
①终端输入  python 4F-4.1D1PAR-4.2T-4.3S-4.4RC.py
开启四宫格，1宫导播带录制声网推流，2宫为教师摄像头回显，3宫为学生摄像头回显，4宫为远端IPC网络摄像头拉流
②终端输入 python change_position.py
将1<->4宫，2<->3宫格 仅进行一次切换

学生端:
SSH 另一台小站
①终端输入 python Student-4F-4.1DR-4.2R1A-4.3S-4.4R.py
开启四宫格，1宫为带录制导播，2宫为教师端声网拉流，3宫为学生摄像头回显，4宫为远端IPC网络摄像头拉流
②终端输入 python Student_change_position.py
将1<->4宫，2<->3宫格 仅进行一次切换

python delete_all_tasks.py

结束当前的任务
