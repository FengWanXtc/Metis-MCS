1. 环境要求
HDMI_IN口接一台PC配置PPT算法,HDMI_CAM_1 口接教师摄像头配置教师算法，本地管理添加IPC摄像头为学生内置算法

2. 脚本执行方式为:
脚本可以按任意顺序执行，执行完一个脚本后10s自动执行delete_all_tasks.py结束当前任务
因为目前还不支持VideoTransformSpecs动态修改，所以设置了自动删除任务

python 17.7.1 VideoTransformSpecs Dynamic task configuration.py 回显启动一个四宫格，第一宫格导播用VideoComposeSpecs组合成的四个画面，再用VideoTransformSpecs设置为反转，但不进行反转

python 17.7.2 Dynamically set FlipMethod to flip vertically.py 回显启动一个四宫格，第一宫格导播用VideoComposeSpecs组合成的四个画面，再用VideoTransformSpecs进行垂直翻转

python 17.7.3  FlipMethod is dynamically set to flip horizontally 回显启动一个四宫格，第一宫格导播用VideoComposeSpecs组合成的四个画面，再用VideoTransformSpecs进行水平翻转

python 17.7.4 Set other parameters dynamically in Flip mode.py 回显启动一个四宫格，第一宫格导播用VideoComposeSpecs组合成的四个画面，再用VideoTransformSpecs进行水平翻转，并设置旋转90度

python 17.7.5 Update the Rotate parameter of Operation in VideoTransformSpecs.py 回显启动一个四宫格，不带VideoTransformSpecs，等待10s后再起一个带VideoTransformSpecs并设置旋转90度

python 17.7.6  Dynamically modify Rotation.py 回显启动一个90度旋转的导播，5s后删除任务启动一个180度旋转的导播，5s后删除任务启动一个270度旋转的导播，因为目前不带VideoTransformSpecs不支持动态修改，因此需要先删除任务

python 17.7.7  Update the Crop parameter for Operation in VideoTransformSpecs.py 回显启动一个四宫格，第一宫格导播用VideoComposeSpecs组合成的四个画面，并使用VideoTransformSpecs进行剪裁保留原来9/16大小

python 17.7.8 Dynamically modified Geometry.py 回显启动一个带剪裁的四宫格，不断改变剪裁的大小，一共启动四次

python 17.7.9 Update the RateAdjust parameter for Operation in VideoTransformSpecs.py 启动导播将导播画面帧率调整为5，看到画面明显卡顿则测试正常

python 17.7.10  Dynamically modify FrameRate.py 启动导播将导播画面帧率调整为25、15、5，看到画面逐渐变卡顿则测试正常



