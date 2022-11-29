1. 环境要求
在S4E8的基础上运行该场景脚本

2台小站
教师端：本地管理1个HDMI配老师，1个IPC配学生，1个HDMI IN 配PPT
学生端：本地管理1个HDMI配老师，1个IPC配学生

显示器要求：分辨率1920*1080

2. 脚本执行方式

方式：python Act_Story.py
            场景内容：  按照提示输入近端和远端小站IP地址
            1.近端渲染Trasnform一路
            2.远端拉Transform
            3.近端推Transform
            4.近端动态修改Transform分辨率，反复5次，近端和远端拉取的流视频分辨率动态变化
