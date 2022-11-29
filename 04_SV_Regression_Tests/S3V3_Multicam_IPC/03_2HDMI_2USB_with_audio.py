import os
import time
import sys
sys.path.append('../../Libraries')
from environmentlib import *
# 创建2HDMI ,2USB
Announce = '''
*************************************************************
Please Input A Metis Station IP Address to pull remote stream
*************************************************************
'''
Anno = "***************************************************"

Host_IP = input("Please Input An Host IP to Test: ")
IP = input("Please Input Far_End IP to Test: ")

scriptlist = ['create_preview.py -d={} -mn=HDMI0 -p=1 -n=Teacher -ip={}'.format(Global_TeacherCamType,Host_IP),
              'create_preview.py -d={} -mn=HDMI1 -p=2 -n=Student -ip={}'.format(Global_StudentCamType,Host_IP),
              'create_preview.py -d={} -mn=HDMI2 -p=3 -n=USB1 -ip={}'.format(Global_BlackBoardCamType,Host_IP),
              'create_preview.py -d={} -mn=USB0 -p=4 -n=USB2 -ip={}'.format(Global_PPTCamType,Host_IP),
              'delete_task_by_name.py -n=HDMI1 -ip={}'.format(Host_IP),
              'create_preview_with_audio.py -d={} -p=1 -mn=HDMI1 -n=HDMI1 -ip={}'.format(Global_TeacherCamType,Host_IP)
              ]


def act(actlist):
    for items in actlist:
        os.system('python {}'.format(items))
        time.sleep(1)


def act_press(actlist):
    for items in actlist:
        os.system('python {}'.format(items))
        input("\n*********************Please Press Enter Key to do next Action******************")


if __name__ == '__main__':
    act(scriptlist)
    input(Anno + "\nPlease Press Enter Key to pull Streams on Far End.")
    os.system('python pull_preview.py -ip={} -p=1'.format(IP))
    # 删除HDMI和audio任务
    input(Anno + "\nPlease Press Enter Key to Start Delete HDMI1 Task.")
    os.system('python delete_task_by_name.py -n=HDMI1 -ip={}'.format(Host_IP))
    # os.system('python delete_all_tasks.py -ip={}'.format(IP))
    # 加上单宫回显
    input(Anno + "\nPlease Press Enter Key to Start create HDMI1 Preview without audio.")
    os.system('python create_preview.py -d={} -mn=HDMI0 -p=1 -n=Teacher -ip={}'.format(Global_TeacherCamType,Host_IP))
    # 删除2个USB回显
    input(Anno + "\nPlease Press Enter Key to Delete 2 USB Preview Tasks")
    os.system('python delete_task_by_name.py -n=USB1 -ip={}'.format(Host_IP))
    os.system('python delete_task_by_name.py -n=USB2 -ip={}'.format(Host_IP))
    # 加上1个USB+audio回显
    input(Anno + "\nPlease Press Enter Key to Add USB1 Preview with Audio.")
    os.system('python create_preview_with_audio.py -d={} -p=3 -mn=USB1 -n=USB1 -ip={}'.format(Global_BlackBoardCamType,Host_IP))
    # 再次创建远端拉流task

    # 删除近端与远端全部任务
    input(Anno + "\nPlease Press Enter Key to Delete all Tasks.")
    print("Near-end:")
    os.system('python delete_all_tasks.py')
    print("Remote:")
    os.system('python delete_all_tasks.py -ip={}'.format(IP))