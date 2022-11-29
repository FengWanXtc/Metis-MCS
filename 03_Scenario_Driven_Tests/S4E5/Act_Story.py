import sys
import threading
sys.path.append('../../Libraries')
from functionlib import *

Near_IP = input("Please Input Near-End Metis IP: ")
Far_IP = input("Please Input Far-End Metis IP: ")
Anno = "*********************************************************"

scriptlist = ['4F-4.1DR-4.2S-4.3T-4.4RT.py -ip={}'.format(Near_IP),
              'Director_push.py -t={} -ip={}'.format(Near_IP, Far_IP)
              ]


def post_suspend(ip, Data):
    tempurl = "http://{}:6689/mediatask/suspend".format(ip)
    tempHeader = {'Content-type': 'application/json'}
    response = requests.post(url=tempurl, headers=tempHeader, json=Data)
    print(response.json())
    return response


def post_resume(ip, Data):
    tempurl = "http://{}:6689/mediatask/resume".format(ip)
    tempHeader = {'Content-type': 'application/json'}
    response = requests.post(url=tempurl, headers=tempHeader, json=Data)
    print(response.json())
    return response


def act_basic(ScriptList, sleeptime=5):
    # 先依次执行前面操作
    for items in ScriptList:
        os.system('python {}'.format(items))
        # print(items)
        time.sleep(sleeptime)


class myThread(threading.Thread):
    def __init__(self, threadID, name, ip, tData):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.ip = ip
        self.tData = tData

    def run(self):
        print("开始线程：" + self.name)
        # print_time(self.name, self.looptime, 5)
        response = post_suspend(self.ip, self.tData)
        if response.json()["Code"] == 200:
            print("{} Suspend Success".format(self.name))
        else:
            print("{} Suspend Fail".format(self.name))
        # 挂起10秒后恢复
        time.sleep(2)
        response = post_resume(self.ip, self.tData)
        if response.json()["Code"] == 200:
            print("{} Resume Success. ".format(self.name))
        else:
            print("{} Resume Fail. ".format(self.name))
        print("退出线程：" + self.name)


if __name__ == '__main__':
    act_basic(scriptlist, sleeptime=5)
    time.sleep(5)
    # 启动4路录制任务
    print(Anno + '\nBasic Steps End. Start 2 Threads Suspend & Resume Task\n' + Anno)
    # 创建新线程
    data = {"Name": "Basic_MCS", "SpecNames": ["ComputerAi_Record"]}
    thread1 = myThread(1, "Thread-Teacher", Near_IP, data)
    data = {"Name": "Basic_MCS", "SpecNames": ["Teacher_Record"]}
    thread2 = myThread(2, "Thread-PPT", Near_IP, data)
    # 开启新线程
    thread1.start()
    thread2.start()
    #
    thread2.join()
    thread1.join()
    print(Anno + "Suspend and Resume Main Thread End.Start Resume Two Record." + Anno)
    time.sleep(5)

    # os.system('python resume.py -mn=Basic_MCS -sn=Teacher_Record,Computer_Record')
