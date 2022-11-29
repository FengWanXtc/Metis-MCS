1. 环境要求
推流小站配置IPC学生内置算法,拉流小站配置HDMI教师摄像头和IPC学生内置算法

2. 脚本执行方式为:
python create_remote.py 启动远端推流，因为该模块测试需要录制远端（在其余脚本执行完之前请不要删除该任务）

python 17.9.1 RecordSpecs Dynamic task configuration.py 四宫格回显，一格本地回显三格远端拉流，四路录制，结束需要手动执行delete_all_tasks.py删除任务生成录制文件

python 17.9.2 Dynamic Change time.py 四宫格回显，一格本地回显三格远端拉流，四路分段录制2700s，等待10s后动态修改为10s的分段录制，结束需要手动执行delete_all_tasks.py删除任务生成录制文件

python 17.9.3 Dynamically modify invalid time values 动态修改分段录制时间为异常值，观察是否生成的录制文件仍然为10s，结束需要手动执行delete_all_tasks.py删除任务生成录制文件

python 17.9.4 Remove Recording task.py 动态删除录制任务

python 17.9.5 Update records by size.py 按照录制文件大小进行分段录制，大小设为1M，结束需要手动执行delete_all_tasks.py删除任务生成录制文件

python 17.9.6  Dynamically modify size.py 动态修改录制文件大小为3M，结束需要手动执行delete_all_tasks.py删除任务生成录制文件

python 17.9.6  Dynamically modify size.py 动态修改录制文件大小为异常值，观察是否生成的录制文件仍然为1M，结束需要手动执行delete_all_tasks.py删除任务生成录制文件

python 17.9.8 Remove Updates remote video recording after a recording task.py 动态删除录制任务

python 17.9.9 Remove Updates the recording end after a recording task.py 动态删除录制任务后再动态开启录制

python 17.9.10 Remove Updates the compose audio and video after recording the task.py 动态删除录制和CodecSpecs任务后再动态开启录制
运行结束后执行 删除任务脚本 delete_all_tasks.py 删除远端小站任务

