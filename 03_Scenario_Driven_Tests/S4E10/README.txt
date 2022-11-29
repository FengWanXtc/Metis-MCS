1. 环境要求
2台小站
教师端：1个HDMI摄像头配置教师算法 1个IPC配置学生算法，接上一台laptop（配置ppt识别算法），本地管理添加一路IPC摄像头（配置板书提取算法）
学生端：1个HDMI摄像头配置教师算法 1个IPC配置学生算法
显示器要求：分辨率1920*1080

2. 脚本执行方式

方式：python Act_Story.py
            场景内容：
            ①本地小站拉3路流,1路导播带录制
            ②混合导播+本地3路拉流,进行编码,随后修改回显为Compose+3路拉流
            ③录制4路+推流导播路
            ④移除录制相关Spec
            ⑤再次拉流另外2路，推流另一台小站另外两路
            ⑥混合导播+3路远端拉流 4分屏
            ⑦录制compose一路
            ⑧混合导播
            ⑨Transform导播一路，使用默认像素
            ⑩修改回显为Transform+3路拉流
            11.进行Transform一路录制
            12.移除本地推compositor一路,远端拉Compositor一路
            13.远端拉Transform，近端推Transform一路
            14.移除Compose，Transform及其录制

            15.混合导播与3路录制
            16.Compose一路Transform 为480P后 回显再推出
            17.Transform进行录制，远端 重新拉Transform一路，查看近远端效果

            18.移除transform相关及推流和compose spec
            19.移除近端3路拉流录制
            20.Transform 修改老师，2路拉流分辨率
            21.Compose 经过 Transform的视频流
            22.录制老师，compose，远端两路拉流
            23.远端移除remote，重新拉remote
            24.近端推compose一路
            25.切换成九宫格

