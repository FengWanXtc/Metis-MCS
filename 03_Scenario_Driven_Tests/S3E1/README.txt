1. 环境要求
教师端：2个摄像头（Global_StudentCamType, Global_TeacherCamType）
学生端1：1个摄像头（设置为HDMI_CAM_1）
学生端2：1个HDMI摄像头（设置为HDMI_CAM_1）
显示器要求：分辨率1920*1080

2. 脚本执行方式为:
python 脚本名.py  

教师端:
SSH 当前小站 （测试方式可选）
（1）终端输入  python Teacher-4F-1RA-2T-3S-4RA.py
        进行故事动画演绎，动画流程如下：
        ①创建四宫格窗口，1宫为声网推流1（不带录制），2宫为教师摄像头回显，3宫为学生摄像头回显，4宫为声网推流2（不带录制）
        ②等待两端学生加入
        ③测试三台小站的音频互动

学生端1：
SSH 第二台小站
①终端输入  python Student-3F-1RA-2RA-3S.py 
创建三宫格窗口，1宫为声网推流1（不带录制），2宫为声网推流2（不带录制），3宫为学生摄像头回显

学生端2：
SSH 第三台小站
①终端输入  python Student-3F-1RA-2RA-3S.py
创建三宫格窗口，1宫为声网推流1（不带录制），2宫为声网推流2（不带录制），3宫为学生摄像头回显

教师端:
SSH 当前小站 （测试方式可选）
（2）终端输入  python replace_frame_animation.py
        ①自动对四宫格的窗口进行顺时针与逆时针各三圈的宫格位置变换，之后回归原位
        ②删除所有窗口
        至此动画结束



（3）也可以执行单功能脚本，做各种动作
        ① python create_remote.py  （-n=1 -p=1）
        创建一宫格推流窗口，-n后跟推流1或2，-p后跟宫格位置，有独立TaskId
        ②python create_preview_teacher.py 
        创建一宫格教师窗口，有独立TaskId
        ③python create_preview_student.py 
        创建一宫格学生窗口，有独立TaskId
        ④python replace_frame.py （-n=Teacher -p=3）
        单独更换每一宫格窗口位置，-n后跟name，-p后跟指定的窗口位置，
        ⑤python replace_frame_animation.py
        自动对四宫格的窗口进行顺时针与逆时针各三圈的宫格位置变换，之后回归原位
        ⑥python delete_task_by_action_name.py   (-n=Teacher)
        参数化构建，可以删除某一个动作任务，可跟参数有Teacher与Student等，
        删除对应动作的任务，不跟参数，默认为删除第①步执行的动作任务 创建的窗口
        ⑧python delete_all_tasks.py
         删除当前创建的所有任务


