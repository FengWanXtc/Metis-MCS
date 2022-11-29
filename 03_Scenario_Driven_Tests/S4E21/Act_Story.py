import sys

sys.path.append('../../Libraries')
from functionlib import *

Near_IP = input("Please Input Near-End Metis IP: ")
Far_IP = input("Please Input Far-End Metis IP: ")
Anno = "************************************"

scriptlist = [
    '4F-CM_RW_RW_RW.py -ip={}'.format(Near_IP),
    'Director_push.py -t={target} -ip={main}'.format(main=Far_IP, target=Near_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_D -ip={}'.format(Near_IP),
    'RTMP_Push.py -mn=Basic_MCS -t={target} -ip={main}'.format(main=Near_IP, target=Far_IP),
    'RTMP_Pull.py -mn=Director_push -ip={}'.format(Far_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_D_P -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_D_P_RW -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_D_P -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_D -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_D_RW -ip={}'.format(Near_IP),
    'remove.py -mn=Basic_MCS -sn=Compose_Record -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_D_P_RW_Audio -ip={}'.format(Near_IP),
    'remove.py -mn=Basic_MCS -sn=Compose_Record -ip={}'.format(Near_IP)
]


def act_basic(ScriptList, sleeptime=5):
    # 先依次执行前面操作
    for items in ScriptList:
        os.system('python {}'.format(items))
        # print(items)
        time.sleep(sleeptime)


if __name__ == '__main__':
    act_basic(scriptlist, sleeptime=5)

