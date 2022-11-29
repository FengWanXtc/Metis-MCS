import sys
import threading

sys.path.append('../../Libraries')
from functionlib import *

Near_IP = input("Please Input Near-End Metis IP: ")
Far_IP = input("Please Input Far-End Metis IP: ")
Anno = "************************************"

scriptlist = [
    '4F-4.1DR-4.2S-4.3T-4.4RT.py -ip={}'.format(Near_IP),
    'Director_push.py -t={target} -ip={main}'.format(target=Near_IP, main=Far_IP),
    'create_update.py -mn=Basic_MCS -jf=D_T_Compose -ip={}'.format(Near_IP),
    'CM_Server.py -mn=Basic_MCS -t={}'.format(Far_IP),
    'remove.py -mn=Basic_MCS -sn=Compositor,Compositor_Record -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=03_T_S_Compose -ip={}'.format(Near_IP),
    'CM_Record.py -mn=Basic_MCS -rn=T_S -ip={}'.format(Near_IP)
]


def act_basic(ScriptList, sleeptime=5):
    # 先依次执行前面操作
    for items in ScriptList:
        os.system('python {}'.format(items))
        # print(items)
        # input("Press  Enter  Key  to  do Next")
        time.sleep(sleeptime)


if __name__ == '__main__':
    act_basic(scriptlist, sleeptime=5)

