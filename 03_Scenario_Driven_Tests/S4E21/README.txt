1. 环境要求

教师端：本地管理1个HDMI配老师，1个IPC配学生，1个HDMI IN 配PPT，再加一个IPC配上板书提取算法
学生端：本地管理1个HDMI配老师，1个IPC配学生

显示器要求：分辨率1920*1080

2. 脚本执行方式

方式：python Act_Story.py
    1.近端回显4宫 导播 教师 学生 拉流 ，导播路录制， 有教师学生PPT板书算法
    2.远端推流一路音视频
    3.compose 1路本地音视频 + RTMP 推出 ，远端拉取
    4.Compose 本地导播+PPT路
    5.Compose 本地导播+PPT路+远端 音视频
    6.Compose 重新变回 本地导播+PPT路
    7.Compose  变成导播
    8.Compose  变成导播+远端
    9.移除Compose录制
    10.Compose 本地导播+PPT路 音视频 (此时PC可以播放音乐)+远端 音视频  ，并且进行录制
    11.移除Compose录制

    后面步骤顺序参照上面描述，检查录制的文件音视频效果


    对应Case 列表
    Metis station Z510_story4_video dynamic compose scene test_01  - 06