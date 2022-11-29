import os
import time

IP = input("Please Input An Host IP to Test: ")
Far_IP = input("Please Input Far_End IP to Test: ")


# 创建4个IPC摄像头
Anno = "***************************************************"
scriptlist = ['remote_pull_IPC.py -r=48/ch2 -p=1 -t=IPC1 -n=IPC1 -ip={}'.format(IP),
              'remote_pull_IPC.py -r=57/ch1 -p=2 -t=IPC2 -n=IPC2 -ip={}'.format(IP),
              'remote_pull_IPC.py -r=57/ch2 -p=3 -t=IPC3 -n=IPC3 -ip={}'.format(IP),
              'remote_pull_IPC.py -r=56/ch1 -p=4 -t=IPC4 -n=IPC4 -ip={}'.format(IP)
              ]


def act(actlist):
    for items in actlist:
        os.system('python {}'.format(items))
        time.sleep(2)


if __name__ == '__main__':
    act(scriptlist)
    # 删除2路IPC摄像头
    input(Anno + "\nPlease Press Enter Key to *Delete IPC1 IPC2* Task.")
    os.system('python delete_task_by_name.py -n=IPC1 -ip={}'.format(IP))
    os.system('python delete_task_by_name.py -n=IPC2 -ip={}'.format(IP))

    # 创建2路带AI 导播教师(HDMI+IPC)
    input(Anno + "\nPlease Press Enter Key to *Create AI 2 Frame* Task.")
    os.system('python IPC_AI_USB_D_2.py -ip={}'.format(IP))

    # 删除导播任务
    input(Anno + "\nPlease Press Enter Key to Delete Director Tasks.")
    os.system('python delete_task_by_name.py -n=IPC_AI_D_T_USB'.format(IP))

    # 开启加audio推流录制任务
    input(Anno + "\nPlease Press Enter Key to  *Create AI 2 Frame with Audio* Tasks.")
    os.system('python IPC_AI_USB_D_2_with_audio.py -ip={}'.format(IP))

    input(Anno + "\nPlease Press Enter Key to create remote rtsp pull Task.")
    os.system('python rtsp_pull.py -mn=RTSP_Pull -ip={host} -uri={uri}'.format(host=Far_IP, uri=IP))
    # 删除全部任务
    input(Anno + "\nPlease Press Enter Key to Delete all Tasks.")
    os.system('python delete_all_tasks.py -ip={}'.format(IP))
    os.system('python delete_all_tasks.py -ip={}'.format(Far_IP))
