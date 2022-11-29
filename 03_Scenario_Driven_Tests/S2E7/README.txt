1. 环境要求
4个IPC网络摄像头，要求本地管理页面配置4个IPC摄像头，不带上算法
显示器要求：分辨率1920*1080

2. 脚本执行方式为:
python 脚本名.py  

3.场景内容：
	  ①python  create_4_IPC_Record_with_1_audio.py
	     开启4路IPC 回显 1路录制 同时带音频，对麦克风说几句话
	   ②python delete_all_tasks.py
	    关闭任务，进入/home/user/Videos/eswin 目录
                    观察是否生成了IPC_1_Record.mp4



