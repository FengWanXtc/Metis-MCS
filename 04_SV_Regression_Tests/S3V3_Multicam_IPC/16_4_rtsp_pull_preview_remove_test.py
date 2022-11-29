import os
import time

# 创建4个IPC摄像头
Anno = "***************************************************"
scriptlist = ['remote_pull_IPC.py -r=48 -p=1 -t=IPC1 -n=IPC1',
              'remote_pull_IPC.py -r=58 -p=2 -t=IPC2 -n=IPC2',
              'remote_pull_IPC.py -r=57 -p=3 -t=IPC3 -n=IPC3',
              'remote_pull_IPC.py -r=56 -p=4 -t=IPC4 -n=IPC4'
              ]


def act(actlist):
    for items in actlist:
        os.system('python {}'.format(items))
        time.sleep(2)


if __name__ == '__main__':
    act(scriptlist)
    # 删除4 路IPC摄像头拉流任务
    input(Anno + "\nPlease Press Enter Key to *Delete All Pulling* Task.")
    os.system('python delete_all_tasks.py')

    # 创建4 路IPC摄像头Preview
    input(Anno + "\nPlease Press Enter Key to *Create 4 IPC Preview* Task.")
    os.system('python IPC_4_Preview.py')

    # 删除全部任务
    input(Anno + "\nPlease Press Enter Key to Delete all Tasks.")
    os.system('python delete_all_tasks.py')

    # 本地管理重命名
    input(Anno + "\nPlease *Rename* IPC AliasName on Local Manage Webpage and then Press Enter Key\n")
    input(Anno + "\nPlease Press Enter Key to *Create New Alias Name 4 IPC Preview* Task.")
    os.system('python IPC_4_Preview.py')

    # 删除全部任务
    input(Anno + "\nPlease Press Enter Key to Delete all Tasks.")
    os.system('python delete_all_tasks.py')

    # 删除2个摄像头
    input(Anno + "\nPlease *Delete* 2 IPC Camera on Local Manage Webpage and then Press Enter Key\n")
    input(Anno + "\nPlease Press Enter Key to *Create New Alias Name 4 IPC Preview With 2 Deleted* Task.")
    os.system('python IPC_4_Preview.py')

    input(Anno + "\nPlease Press Enter Key to Delete all Tasks.")
    os.system('python delete_all_tasks.py')


