脚本说明：
序号开头的是根据z510 story3 case表格设计的
环境要求： 2台小站，近端和远端
         近端 HDMI 1,2口插HDMI摄像头， HDMI IN口接PC
         远端 HDMI 1,2口插HDMI摄像头

********************************************************************************
重要说明：

推流方式：(比如)python remote_push.py -ct=HDMI -ip=10.12.224.44 -cn=1
        -d指定对应小站推流的摄像头，-ip为对应小站id，-ct 为推流摄像头类型 -cn 为摄像头序列
        可以用python delete_all_tasks.py -ip=10.12.224.44删除对应小站的任务
********************************************************************************

运行方式 （在执行该脚本前先让另外小站推流）
01：python 01_pull_remote.py
content： Represents to generate a single cell remote pull flow window
       -mn  MCS Name,Default is  Remote_1
       -ip  The Host IP of Metis Station
       -p   The position of the frame
     You Can Use Script   'delete_all_tasks.py'  or   'delete_task_by_action_name.py -n=Remote_1'  to remove this task

02：python 02_pull_remote_four.py  （非参数化构建，不需要跟参数）
content：Create Four Frame Agora Pull Frame
备注： 因为是拉4路流，如果小站资源紧张，可以只让某台小站推一次流，参考推流脚本

03：python 03_pull_remote_three.py  （非参数化构建，不需要跟参数）
运行方式 ：
内容： 现创建一个宫格拉流，再创建其他三宫拉流
备注： 执行前可以让其他小站先推流

04：python 04_create_1_3_delete_1.py （非参数化构建，不需要跟参数）
      故事性动作连贯脚本，按回车执行下一个动作
内容： 创建1个左上角单宫拉流，创建1个三宫拉流，删除左上角单宫，删除三宫
备注： 执行前可以让其他小站先推流

05：该case不合MCS0.3已移除

06：python 06_create_frames_1by1.py （非参数化构建，不需要跟参数）
      故事性动作连贯脚本，可以不用按回车，依次创建4个单宫格 **声网** 远端拉流窗口
可以利用脚本   delete_all_tasks.py结束所有窗口，也可以利用delete_task_by_action_name.py -n=Remote_1  结束对应窗口
备注： 执行前可以让其他小站先推流

07：python 07_create_frames_1by1_rtsp.py（非参数化构建，不需要跟参数）
     故事性动作连贯脚本，可以不用按回车，依次创建4个单宫格 **RTSP**  远端窗口  RTSP_1 RTSP_2,..........
可以利用脚本   delete_all_tasks.py结束所有窗口，也可以利用delete_task_by_action_name.py -n=Remote_1  结束对应窗口

08：python 08_pull_remote_four_rtsp.py（非参数化构建，不需要跟参数）
    一次性创建1个4宫格 **RTSP**  远端拉流窗口
    可以利用脚本   delete_all_tasks.py结束这个任务

09：python 09_pull_remote_4_change_position.py（非参数化构建，不需要跟参数）
动作内容：创建4个宫格RTSP拉流窗口，随后进行宫格变换

10：python 10_pull_remote_4_teacher_record.py（非参数化构建，不需要跟参数）
    故事性动作连贯脚本
动作内容：创建4个远端拉流宫格窗口，进行教师端（用的小站CAM_1摄像头）录制，录制的视频保存在 /home/user/Videos/eswin/目录下，
        保存的文件名为Teacher_record.mp4，  delete tasks 后检测录制的内容是否正常
备注： 执行前可以让其他小站先推流


--------------------------------------------------------------------------------------------
注释：前10个case用remote_push.py -ip=XXX 另一台小站进行推流
后续会用remote_push_pull.py 对另一台小站进行推流+拉流回显
--------------------------------------------------------------------------------------------

首先python  remote_push_pull.py -ip=XXXX 让远端一台小站进行推流+拉流回显

11： python 11_pull_remote_4_student_push.py
    故事性动作连贯脚本，依次创建4个拉流窗口，再进行推流本地HDMI 2口摄像头，远端小站能收到画面


12：python 12_pull_remote_4_T_S.py
故事性动作连贯脚本，
动作内容：创建4个远端拉流宫格窗口，再进行推流本地HDMI 2口摄像头，远端小站能收到画面
        随后进行本地教师摄像头录制任务

13：python 13_pull_remote_4_T_S_multi.py
故事性动作连贯脚本，按回车进行下一个动作
动作内容:  依次创建4个远端拉流宫格窗口，随后开启一路教师录制（不带回显）
         本地学生摄像头推流
         然后删除老师录制，重新开启老师录制，删除 2 个 拉流窗口
         再次创建刚刚删除的2个窗口

14: python 14_pull_3_remote_1_preview.py
故事性动作连贯脚本，按回车进行下一个动作
动作内容:  创建1、2、3宫格拉流窗口
          本地推流HDMI_CAM_2学生摄像头
          开启一路 教师回显录制窗口（第4宫格）
          删除所有任务

15: python 15_push_student_4_preview.py (非参数化构建，不需要跟参数）
故事性动作连贯脚本，按回车进行下一个动作
动作内容:  创建1、2、3宫格拉流窗口
          本地推流HDMI_CAM_2 学生摄像头并且回显于第四宫格
          删除一路拉流，开启一路教师回显录制窗口于第一宫格
          删除第二路拉流， 开启HDMI_CAM_IN PPT回显,
          删除第三路拉流，开启IPC板书摄像头回显（本地管理需要添加0403-0001 IPC摄像头）


16: python 16_4_position_switch_1.py (非参数化构建，不需要跟参数）
环境要求：3个HDMI 摄像头 ，1个USB摄像头
备注：
故事性动作连贯脚本，按回车进行下一个动作
动作内容:  创建2，3宫 PPT,板书回显
          创建1，4宫拉流，
          创建教师录制和学生推流，
          删除板书回显和2路拉流，
          恢复板书回显和2路拉流，
          删除PPT，板书回显和一路拉流，
          删除教师录制，学生推流，
          删除一路拉流，
          再回显一路拉流

17: python 17_agora_stability.py (非参数化构建，不需要跟参数）
稳定性测试
动作内容:  创建1、2宫格拉流窗口
                创建3、4宫格回显窗口（对应HDMI_CAM_IN口，USB 1个摄像头）
                启动教师摄像头（HDMI_CAM_1） 录制任务， 启动学生摄像头（HDMI_CAM_2）推流任务
	等待2小时后 删除所有任务

