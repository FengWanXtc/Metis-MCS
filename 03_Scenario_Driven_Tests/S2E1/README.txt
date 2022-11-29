1. 环境要求
教师端：3个HDMI (Global_GeneralCamType类型) 摄像头，1个USB (Global_GeneralCamType_Other类型)  摄像头，需要在本地管理将摄像头打开
显示器要求：分辨率1920*1080



2. 脚本执行方式为:
python 脚本名.py  

教师端:
SSH 当前小站 （测试方式可选）
（1）终端输入  python Act_Story.py
        进行故事动画演绎，动画流程如下：
        ①创建四宫格窗口，1宫为教师摄像头回显，2宫为学生摄像头回显，3宫为黑板摄像头回显，4宫为USB摄像头回显
        ②依次对四宫格的窗口进行顺时针与逆时针各三圈的宫格位置变换，之后回归原位
        ③依次删除第①步创建的1、2、3宫格窗口
        ④对第四宫格窗口进行位置变换到第一宫格，再放大其画面，之后回归原位
        ⑤重新执行第①步，创建回前三宫窗口
        ⑥删除所有窗口
        至此动画结束

（2）也可以执行单功能脚本，做各种动作
        ① python create_one_frame_preview.py  （-ip=10.12.224.135 -n=teacher -ct=HDMI -cn=0 -g=0,0,960,540）
        创建每一宫格窗口，
        -ip:   指定对应小站创建任务，缺省值为脚本所在的小站IP地址
        -n ：生成的MCS Name    （缺省值为Teacher）
        -ct:   指定回显摄像头类型 （可选值HDMI,USB,IPC ，缺省值为 HDMI）
        -cn:  对应摄像头的序列号 （HDMI -  0,1,IN    USB-4,5,6,7   IPC-1,2,3,4  缺省值为 HDMI）
        -g :    生成的窗口宫格位置   (缺省值为0,0,960,540)
        ②python change_geometry_animation.py
        自动对四宫格的窗口进行顺时针与逆时针各三圈的宫格位置变换，之后回归原位
        ③python delete_task_by_action_name.py   (-n=Teacher -ip=10.12.224.135)
        参数化构建，可以删除指定MCS Name的任务，必须
         -ip: 删除指定IP小站的所有任务，缺省值为当前脚本所在的小站IP
         -n:  为对应MCS Name 任务，必填参数

        ④python change_geometry.py （-n=Teacher  -g=0,0,960,540）
        参数化构建，指定第四宫格窗口进行位置切换，前两个数0，0 为宫格窗口左上角距离显示器左上角（x，y）偏移坐标，后两个数（960，540）为该窗口的分辨率。
        -n:  为对应MCS Name 任务，必填参数
        -g :  生成的窗口宫格位置   (缺省值为0,0,960,540)

        ⑥python delete_all_tasks.py（-ip=10.12.224.135）
         删除当前创建的所有任务
         -ip: 删除指定IP小站的所有任务，缺省值为当前脚本所在的小站IP


