

1. 环境要求
2台小站
教师端：1个HDMI摄像头配置教师算法 1个IPC配置学生算法，接上一台laptop（配置ppt识别算法），本地管理添加一路IPC摄像头（配置板书提取算法）
学生端：1个HDMI摄像头配置教师算法 1个IPC配置学生算法
显示器要求：分辨率1920*1080

2. 脚本执行方式

方式：python Act_Story.py
            场景内容：
            ①先执行S4E5的场景内容
            ②将回显变成导播，老师特写，学生特写和PPT
            ③移除回显
            ④重新下发回显为一宫格拉流画面
            ⑤移除回显
            ⑥重新下发回显四宫格，导播，老师，学生及一路远端拉流
            ⑦再拉两路流（声网用RTC specs）以及RenderSpecs 修改老师及学生宫格的resource name变成远端拉流，回显变成导播，三路拉流
            ⑧推远端小站的教师和学生摄像头流
            ⑨移除老师，学生，PPT全景录制

