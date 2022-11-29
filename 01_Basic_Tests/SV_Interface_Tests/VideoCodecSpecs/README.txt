1. 环境要求
HDMI_IN口接一台PC配置PPT算法,HDMI_CAM_1 口接教师摄像头配置教师算法，本地管理添加IPC摄像头为学生内置算法,再添加一个为板书提取算法

2. 脚本执行方式为:
python VideoComposeSpecs_Test.py

运行结束后执行 删除任务脚本 delete_all_tasks.py

3.期待结果,7个case均返回PASS
    01: 创建四宫回显，1宫导播，二宫教师，三宫学生，四宫板书
    02：修改教师VideoCodecSpec 的 BitRate 为 2mbps
    03：修改教师VideoCodecSpec 的 BitRate 为  -50mbps
    04: 修改教师VideoCodecSpec 的 BitRate 为  test BPS
    05: 修改教师VideoCodecSpec 的 BitRate 为  512gbps
    06: 修改教师VideoCodecSpec 的 BitRateMode 为  CBR
    07: 修改教师VideoCodecSpec 的 iFrameInterval 为25
    08: 修改教师VideoCodecSpec 的 idrInterval 为 60
    09: 修改教师VideoCodecSpec 的 QpRange 为 [51, 51]