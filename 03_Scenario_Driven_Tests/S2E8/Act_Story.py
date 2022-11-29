import sys
sys.path.append('../../Libraries')
from environmentlib import *
from functionlib import *
import paramiko

hostname = HOST_IP
# Careful the host Metis-station
port = 22
login = 'user'
password = 'User@1949!'

scriptlist = ['create_one_frame_preview.py -n=Teacher -ct={} -cn=1 -g=0,0,960,540'.format(Global_GeneralCamType),
              'create_one_frame_preview.py -n=Student -ct={} -cn=2 -g=960,0,960,540'.format(Global_GeneralCamType),
              'delete_all_tasks.py'
              ]
checkStr = 'tegra194-vi5 15c10000.vi: corr_err: discarding frame'


def exeCmd():
    execmd = 'echo user | sudo -S tail -n 5 /var/log/kern.log'
    s = paramiko.SSHClient()  # 创建SSH对象
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接主机
    s.connect(hostname=hostname, port=port, username=login, password=password)  # 连接服务器
    stdin, stdout, stderr = s.exec_command(execmd)  # 执行命令
    outputBytes = stdout.read() + stderr.read()
    outputStr = outputBytes.decode("utf-8")
    return outputStr


def act():
    count = 10
    while True:
        if count > 0:
            os.system('python {}'.format(scriptlist[0]))
            time.sleep(1)
            os.system('python {}'.format(scriptlist[1]))
            time.sleep(1)
            outputStr = exeCmd()
            if outputStr.find(checkStr) != -1:
                print("Loop Remain times is " + str(count))
                print(outputStr)
                break
            else:
                count -= 1
                os.system('python {}'.format(scriptlist[2]))
                print("Loop Remain times is " + str(count))
        else:
            print("Loop for 5 times end")
            break


if __name__ == '__main__':
    act()
