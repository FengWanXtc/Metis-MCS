脚本说明：
序号开头的是根据z510 story1 case表格设计的
环境要求： 2台小站，近端和远端
         近端 2个摄像头本地管理配置教师和学生算法
         远端 HDMI 1个摄像头

********************************************************************************
重要说明：

推流方式：(比如)python remote_push.py -ct=HDMI -ip=10.12.224.44 -cn=1
        -d指定对应小站推流的摄像头，-ip为对应小站id，-ct 为推流摄像头类型 -cn 为摄像头序列
        可以用python delete_all_tasks.py -ip=10.12.224.44删除对应小站的任务
********************************************************************************

运行方式 （在执行该脚本前先让另外小站推流）
01：python 11.1.1_four_frames_tea.py
content： Represents to generate a single cell remote pull flow window
       -mn  MCS Name,Default is  Remote_1
       -ip  The Host IP of Metis Station
       -p   The position of the frame
     You Can Use Script   'delete_all_tasks.py'  or   'delete_task_by_action_name.py -n=Remote_1'  to remove this task

02：python 02_pull_remote_four.py  （非参数化构建，不需要跟参数）
content：Create Four Frame Agora Pull Frame
备注： 因为是拉4路流，如果小站资源紧张，可以只让某台小站推一次流，参考推流脚本

