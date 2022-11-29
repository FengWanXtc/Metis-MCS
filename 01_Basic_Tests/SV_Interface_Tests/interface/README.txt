1. 环境要求
小站配置一个教师和一个学生摄像头

2. 脚本执行方式为:
python create_preview.py 启动一个小站的回显便于测试

python 17.10.1 Current MCS query.py 调用inspection接口查询当前下发的MCS

python 17.10.2 Current task query.py 调用tasks接口获取当前下发MCS的名称

python 17.10.3 Current subtask query.py 调用GET mediatask/{MCS_Name}/{Spec_Name}获取当前mcs中的spec内容

python 17.10.4 Multi-task query.py 下发两个MCS任务，用tasks接口获取当前下发MCS的名称

python 17.10.5 Sub-media task snapshot.py 先删除当前任务后，重新下发MCS并加入远端互动，后测试snapshot接口给远端推流画面截图。需要检查videos/eswin下是否有截图文件生产，无需停止任务。

python 17.10.6 MIOS query.py 检查目标下站的MIOS设置

python 17.10.7  keyframe post.py 对目标小站下发keyframe关键帧

运行结束后执行 删除任务脚本 delete_all_tasks.py 删除近端和远端小站任务

