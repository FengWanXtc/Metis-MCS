脚本运行方式:
python + 脚本名

1.  python  01_2HDMI_2USB_preview.py
    场景要求：2个HDMI摄像头，2个USB摄像头
     动作流程： ①依次创建 4个单宫格摄像头回显任务 窗口依次为（HDMI0、HDMI1、USB0、USB1）
                       ② (1)python delete_all_tasks.py    可以删除所有任务
                           (2) python delete_task_by_action_name.py -n=HDMI1  删除对应窗口任务（可选参数HDMI0、HDMI1、USB0、USB1）


2. python  02_3HDMI_1USB_preview.py
    场景要求：2个HDMI摄像头，2个USB摄像头,HDMI_IN口接一台PC
    动作流程： ①依次创建 4个单宫格摄像头回显任务 窗口依次为（HDMI0、HDMI1、HDMI2、USB0）
             ②按回车删除第一个宫格
             ③ (1)python delete_all_tasks.py    可以删除所有任务
                (2) python delete_task_by_action_name.py -n=HDMI1  删除对应窗口任务（可选参数HDMI0、HDMI1、HDMI2、USB0、PC）


3. python  03_2HDMI_2USB_with_audio.py
   场景要求： 2台小站
            近端小站： 2个HDMI摄像头，2个USB摄像头
    * 按回车进行下一个步骤 *
    输入近端小站的IP地址和远端小站的IP地址
    依次创建 4个单宫格摄像头回显任务 窗口依次为（HDMI0、HDMI1、HDMI2、USB0）
    删除第一个宫格，进行HDMI+Audio推流回显
    对远端小站进行音视频拉流回显,验证音视频推拉效果
    删除第一宫格，进行HDMI回显
    删除两路USB回显
    进行USB+Audio推流回显，验证音视频推拉效果
    删除近端和远端所有任务

4. python  04_2HDMI_2USB_with_audio_push_pull.py
   场景要求： 2台小站
            近端小站： 2个HDMI摄像头，2个USB摄像头
            远端小站： 1个HDMI摄像头
    * 按回车进行下一个步骤 *
    输入近端小站的IP地址和远端小站的IP地址
    依次创建 4个单宫格摄像头回显任务 窗口依次为（HDMI0、HDMI1、HDMI2、USB0）
    删除第一个宫格，进行HDMI1+Audio推流 同时远端拉流回显
    对远端小站进行音视频拉流回显,同时推流本地HDMI摄像头,验证两端音视频推拉效果
    删除第二宫格，进行HDMI2回显+录制
    删除两路USB回显+HDMI2录制回显任务
    删除近端和远端所有任务

5. python  05_2HDMI_2USB_with_audio_push_pull_record.py
   场景要求： 2台小站
            近端小站： 2个HDMI摄像头，2个USB摄像头
            远端小站： 1个HDMI摄像头
    * 按回车进行下一个步骤 *  注意观察复制屏的效果，执行场景和5一样
    输入近端小站的IP地址和远端小站的IP地址
    依次创建 4个单宫格摄像头回显任务 窗口依次为（HDMI0、HDMI1、HDMI2、USB0）
    删除第一个宫格，进行HDMI+Audio推流 同时拉流回显
    对远端小站进行音视频拉流回显,同时推流本地HDMI摄像头,验证两端音视频推拉效果
    删除第一宫格，进行HDMI回显
    删除两路USB回显
    进行USB+Audio推流回显，验证音视频推拉效果
    删除近端和远端所有任务


6.  06_2HDMI_2USB_video_out.py
   场景要求： 2台小站
            近端小站： 2个HDMI摄像头，2个USB摄像头 ,接双显示器DP+HDMI，为复制屏
            远端小站： 1个HDMI摄像头
    * 按回车进行下一个步骤 *  注意观察复制屏的效果，执行场景和5一样

7. 07_2HDMI_2USB_audio_out.py
   场景要求： 2台小站
            近端小站： 2个HDMI摄像头，2个USB摄像头
            远端小站： 1个HDMI摄像头,借一个耳机插入显示器
    * 按回车进行下一个步骤 *  注意观察远端小站接受耳机音频
    输入近端小站的IP地址和远端小站的IP地址
    依次创建 4个单宫格摄像头回显任务 窗口依次为（HDMI0、HDMI1、HDMI2、USB0）
    删除第一个宫格，进行HDMI+Audio推流 同时拉流回显
    对远端小站进行音视频拉流回显,同时推流本地HDMI摄像头,验证两端音视频推拉效果，通过耳机听近端推流的声音


8. 08_2rtsp_AI_pull.py
两个IPC rtsp推流需要本地管理配置四个IPC，两个带算法一个教师一个学生
场景内容：
    依次创建4个IPC拉流，再删除前两个，随后下发双宫格，一宫格导播二宫格教师回显 （2个本地管理IPC摄像头作为视频源）

9. 09_2rtsp_AI_pull_with_audio.py
两个IPC rtsp推流需要本地管理配置四个IPC，两个带算法一个教师一个学生，带audio
    依次创建4个IPC拉流，再删除前两个，随后下发双宫格，一宫格导播二宫格教师回显 （2个本地管理IPC摄像头作为视频源）
    随后删除双宫格任务，再次下发，带上Audio推流以及录制的任务
    远端拉到RTSP音视频流,检查近端小站录制导播是否成功


10. 10_2rtsp_AI_HDMI_with_audio.py
   场景要求： 2台小站
            近端小站： 1个HDMI摄像头配置教师算法,本地管理配置IPC摄像头作为学生算法
            远端小站：
    依次创建4个IPC拉流，再删除前两个，随后下发双宫格，一宫格导播二宫格教师回显 （1HDMI作为教师，1IPC作为学生合成导播源）
    随后删除双宫格任务，再次下发，带上Audio推流以及录制的任务
    远端拉到RTSP音视频流，检查近端小站录制导播是否成功


11. 11_2rtsp_AI_USB_with_audio.py
   场景要求： 2台小站
            近端小站： 1个USB摄像头配置学生算法,本地管理配置IPC摄像头作为教师算法
            远端小站：
    依次创建4个IPC拉流，再删除前两个，随后下发双宫格，一宫格导播二宫格教师回显 （1PC作为教师，1USB作为学生合成导播源）
    随后删除双宫格任务，再次下发，带上Audio推流以及录制的任务
    远端拉到RTSP音视频流，检查近端小站录制导播是否成功


12. 12_2rtsp_AI_HDMI_USB_with_audio.py
   场景要求： 2台小站
            近端小站： 1个HDMI摄像头配置教师算法，1个USB摄像头配置学生算法,本地管理配置IPC摄像头作为板书算法
            远端小站：
    依次创建4个IPC拉流，再删除前3个，随后下发3宫格，一宫格导播二宫格教师回显三宫格学生回显 （1HDMI作为教师，1USB作为学生1IPC作为板书摄像头合成导播源）
    随后删除三宫格任务，再次下发，带上Audio推流以及录制的任务
    远端拉到RTSP音视频流，检查近端小站录制导播是否成功


13. 13_4_frames_local_preview.py
rtsp推流需要本地管理配置四个IPC，分别配置教师、学生、黑板和PPT
   场景要求： 1台小站
            近端小站： 本地管理配置四个IPC，配置教师、学生、黑板和PPT
            依次创建4个IPC拉流，再删除4个，随后将本地管理IPC摄像头作为本地回显出来


14. 14_2rtsp_pull_2_preview.py
rtsp推流需要本地管理配置2个IPC，分别配置教师、学生
   场景要求： 1台小站
            近端小站： 本地管理配置2个IPC，配置教师、学生算法
            依次创建4个IPC拉流，再删除2个，随后将本地管理IPC摄像头2个 教师和学生 作为本地二宫格回显出来


15. 15_4_rtsp_pull_preview.py
rtsp推流需要本地管理配置四个IPC，配置教师、学生、黑板和PPT带推流
16 同