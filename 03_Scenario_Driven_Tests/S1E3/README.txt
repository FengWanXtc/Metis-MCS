1. 环境要求
教师端：1个HDMI摄像头（默认HDMI_CAM_0口）
显示器要求：分辨率1920*1080

2. 脚本执行方式为:
python 脚本名.py  

教师端:
SSH 当前小站 （测试方式可选）
（1）终端输入  python Act_Story.py
        进行故事动画演绎，动画流程如下：
        ①创建Background，小站背景变化
        ②创建单宫格回显窗口，占左上角1/4屏
        ③删除第②步创建的宫格
        ④删除第①步的背景
        ⑤重新执行第①步创建背景
        ⑥重新执行第②步创建单宫格回显，占全屏
        ⑦删除第⑤步创建的宫格窗口
        ⑧删除第⑥步创建的背景
        至此动画结束

（2）也可以执行单功能脚本，做各种动作
        ① python create_one_frame_preview.py  （-ip=10.12.224.135 -n=teacher -ct=HDMI -cn=0 -g=0,0,960,540）
        创建每一宫格窗口，
        -ip:   指定对应小站创建任务，缺省值为脚本所在的小站IP地址
        -n ：生成的MCS Name    （缺省值为Teacher）
        -ct:   指定回显摄像头类型 （可选值HDMI,USB,IPC ，缺省值为 HDMI）
        -cn:  对应摄像头的序列号 （HDMI -  0,1,IN    USB-4,5,6,7   IPC-1,2,3,4  缺省值为 HDMI）
        -g :    生成的窗口宫格位置   (缺省值为0,0,960,540)

        ②python create_UI.py  （参数化构建）
        可跟参数为 -i=True ，默认为False ，如果为True就恢复初始背景（null）

        ③python delete_all_tasks.py   (参数化构建)
        可跟参数为 -ip，删除指定IP的小站任务，默认为当前脚本存放的小站

        ④python delete_task_by_action_name.py   (-n=Teacher -ip=10.12.224.135)
        参数化构建，可以删除指定MCS Name的任务，必须
         -ip: 删除指定IP小站的所有任务，缺省值为当前脚本所在的小站IP
         -n:  为对应MCS Name 任务，必填参数


