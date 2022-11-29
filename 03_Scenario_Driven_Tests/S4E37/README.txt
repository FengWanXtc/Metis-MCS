1. 环境要求
关闭 UFW sudo disable ufw
2台小站
主设备：1个HDMI摄像头（0配置教师算法) 1个usb摄像头（4配置学生算法），接上一台laptop（配置ppt识别算法），本地管理添加一路IPC摄像头（配置板书提取算法）
辅设备：2个HDMI摄像头（0配置教师算法，1配置学生算法）
显示器要求：分辨率1920*1080

2. 脚本执行方式

方式：python Act_Story.py
            1: 远端拉流
            2：本地推拉
            3：远端推流
            5：更改回显画面
            4：进行录制
            5：宫格变换
            6：录制（暂停，继续，停止操作）
            7：compose tcp推 拉 + 回显
            8：compose rtmp推拉 + 回显
            9：transform 推拉 + 回显

删除任务 用 python delete_all_tasks.py  -ip=XX.XXX.XXX.XXX