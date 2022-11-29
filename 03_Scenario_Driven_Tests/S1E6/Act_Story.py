import argparse
import sys
sys.path.append('../../Libraries')
from functionlib import *
import paramiko

hostname = HOST_IP
# Careful the host Metis-station
port = 22
login = 'user'
password = 'User@1949!'

scriptlist = [
    '4F-4.1DR-4.2T-4.3S-4.4RC.py',
    'delete_all_tasks.py'
]

checkStr = 'tegra194-vi5 15c10000.vi: corr_err: discarding frame'


def execCmd():
    execmd = 'echo user | sudo -S tail -n 5 /var/log/kern.log'
    s = paramiko.SSHClient()  # 创建SSH对象
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接主机
    s.connect(hostname=hostname, port=port, username=login, password=password)  # 连接服务器
    stdin, stdout, stderr = s.exec_command(execmd)  # 执行命令
    outputBytes = stdout.read() + stderr.read()
    outputStr = outputBytes.decode("utf-8")
    return outputStr


def act():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('--times', '-t', type=int, default=10, help='The IP address of the METIS')
    args = parser.parse_args()
    TIMES = args.times
    while True:
        if TIMES > 0:
            os.system('python {}'.format(scriptlist[0]))
            time.sleep(1)
            outputStr = execCmd()
            if outputStr.find(checkStr) != -1:
                print("Loop Remain times is " + str(TIMES))
                print(outputStr)
                break
            else:
                TIMES -= 1
                os.system('python {}'.format(scriptlist[1]))
                print("Loop Remain times is " + str(TIMES))
        else:
            print("Loop for 10 times end")
            break


if __name__ == '__main__':
    act()
