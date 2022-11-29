1. 环境要求
教师端：3个HDMI摄像头（分别设置为Teacher、Student、Blackbord），1个USB摄像头（本地管理页面设置为USB1）
显示器要求：分辨率1920*1080

2. 脚本执行方式为:
python 脚本名.py  

教师端:
SSH 当前小站 （测试方式可选）
（1）终端输入  python Act_Story.py
        进行故事动画演绎，动画流程如下：
        ①创建四宫格窗口，1宫为教师摄像头回显，2宫为学生摄像头回显，3宫为黑板摄像头回显，4宫为USB摄像头回显
        ②按照提示信息，可输入数字0、1、2、3、4、5
        ③其中数字0为显示四宫格画面，数字1为全屏显示第1宫格画面、数字2为全屏显示第2宫格画面、数字3为全屏显示第3宫格画面、
           数字4为全屏显示第4宫格画面、数字5为删除所有任务并退出
        ④输入其他不在范围内数字，会出现错误提示信息
        至此动画结束

（2）也可以执行单功能脚本，做各种动作
        ① python createa_one_frame_preview.py  （-n=Teacher -f=1）
        创建每一宫格窗口，-n后跟name，-f后跟宫格位置，有独立TaskId
        ②python replace_frame.py （-n=Teacher -p=3）
        单独更换每一宫格窗口位置，-n后跟name，-p后跟指定的窗口位置，
        ③python replace_frame_animation.py
        自动对四宫格的窗口进行顺时针与逆时针各三圈的宫格位置变换，之后回归原位
        ④python delete_task_by_action_name.py   (-n=Teacher)
        参数化构建，可以删除某一个动作任务，可跟参数有Teacher与Student等，
        删除对应动作的任务，不跟参数，默认为删除第①步执行的动作任务 创建的窗口
        ⑤python change_geometry.py （-n=Teacher -c=0,0,960,540）
        参数化构建，指定第四宫格窗口进行位置切换，前两个数0，0 为宫格窗口左上角距离显示器左上角（x，y）偏移坐标，后两个数（960，540）为该窗口的分辨率。
        ⑥python delete_all_tasks.py
         删除当前创建的所有任务


