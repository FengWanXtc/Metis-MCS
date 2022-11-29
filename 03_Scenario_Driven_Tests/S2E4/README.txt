1. 环境要求
1个HDMI摄像头，1个USB摄像头
本地管理摄像头需要为开启状态
显示器要求：分辨率1920*1080

2. 脚本执行方式为:
python 脚本名.py  

3.场景内容：
	  ①python  rtsp_push.py （参数化构建）
                     -u1=HDMI_stream    (推流HDMI的URL，自定义，缺省值是myStream1)
	     开启一路HDMI和USB摄像头RTSP推流任务
	   ②python delete_all_tasks.py （参数化构建）
	     -ip=10.12.XXXX
                     删除指定小站IP的所有任务


多路摄像头推流 
需要使用vlc工具，在有vlc的开发机上 拉取  rtsp://{小站IP}:8554/metis/ch{i}
                           有几个摄像头推流，i的值最大可以填几

