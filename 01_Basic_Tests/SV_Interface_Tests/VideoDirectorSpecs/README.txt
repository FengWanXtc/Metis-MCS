1. 环境要求
HDMI_IN口接一台PC配置PPT算法,HDMI_CAM_1 口接教师摄像头配置教师算法，本地管理添加IPC摄像头为学生内置算法

2. 脚本执行方式为:
python create_preview.py 启动一个导播获取摄像头。注意若小站当前无任务执行后续脚本前需要现通过该脚本启一个任务，也可通过APPdemo启动任意导播代替这一步，

python 17.5.1 VideoDirectorSpecs Dynamic task configuration.py 执行下发VideoAiSpecs、VideoDirectorSpec、RenderSpecs修改画面四宫格带AI

python 17.5.2 Dynamically delete the broadcast director policy.py 删除学生单人站立策略

python 17.5.3 Dynamically add the broadcast director policy.py 添加学生单人站立策略

python 17.5.4 Dynamically changes the priority of broadcast policy.py 为了便于测试，将PPT优先级设为了最低，若移动鼠标导播不切PPT则正常

python 17.5.5 Dynamically modify the video source of broadcast director policy.py 将教师走动VideoSource设为教师全景（验证需要教师在黑板范围外走动，如果能切黑板预置位则正常）

python 17.5.6 Dynamically modify Delay parameters.py 将单人学生起立的延时设置为了10s，验证需要导播在教师摄像头时，学生起立延时10s后切学生特写

python 17.5.7 Dynamically modify timeout parameters.py 为了测试方便将PPT的识别HOLD改为了5s，timeout设为了10s，测试时播放视频10s是否会切到其他场景

python 17.5.8 Dynamically modify hold parameters.py 设置PPThold时间为30s，测试可以变化PPT静止后30s看是否回切到其他画面

运行结束后执行 删除任务脚本 delete_all_tasks.py

