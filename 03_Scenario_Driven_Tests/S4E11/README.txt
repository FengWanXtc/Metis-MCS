1. 环境要求
2台小站
教师端：1个HDMI摄像头配置教师算法 1个IPC配置学生算法，接上一台laptop（配置ppt识别算法），本地管理添加一路IPC摄像头（配置板书提取算法）
学生端：1个HDMI摄像头配置教师算法 1个IPC配置学生算法
显示器要求：分辨率1920*1080

2. 脚本执行方式

方式：python Act_Story.py
            场景内容：
            ①本地小站拉3路流,1路导播带录制,混合导播+本地3路拉流,进行编码
            ②回显为Compose导播+3路拉流
            ③Compose 导播+T+S+PC
            ④回显2路Compose+2路远端
            ⑤录制2路Compose+1路远端+1路教师
            ⑥RTMP推流两路Compose
            ⑦远端RTMP拉流两路Compose并且回显
            ⑧近端RTMP推流学生
            ⑨远端RTMP拉流学生并且修改回显为导播+3路RTMP拉流
            ⑩移除Compose 1 Spec，两路音视频拉流
            11.修改回显为Compose，教师，学生，板书特写

