1. 环境要求
4个IPC网络摄像头，要求本地管理页面配置4个IPC摄像头，不带上算法
显示器要求：分辨率1920*1080

2. 脚本执行方式为:
python 脚本名.py  

3.场景内容： （1）场景 一 ：录制+回显
	    ①运行create_4_IPC_Record脚本 ，启动4路IPC摄像头 回显 带2路录制 IPC1 IPC2
                    ②一段时间后运行 delete_all_tasks 脚本结束后 ，进入/home/user/Videos/eswin
                      目录下观察是否生成了   IPC_1_Record.mp4   与   IPC_2_Record.mp4   文件，看视频录制内容是否正常

                     （2）场景2 ：只录制不回显
	    ①运行create_4_IPC_Record脚本 ，启动4路IPC摄像头 2路录制  IPC3 IPC4
                    ②一段时间后运行 delete_all_tasks 脚本结束后 ，进入/home/user/Videos/eswin
                      目录下观察是否生成了   IPC_3_Record.mp4   与   IPC_3_Record.mp4   文件，看视频录制内容是否正常

