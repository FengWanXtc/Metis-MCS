import sys
import threading

sys.path.append('../../Libraries')
from functionlib import *

Near_IP = input("Please Input Near-End Metis IP: ")
Far_IP = input("Please Input Far-End Metis IP: ")
Anno = "************************************"

scriptlist = [
    '4F-CM_RW_RW_RW.py -ip={}'.format(Near_IP),
    'Director_push.py -t={target} -ip={main}'.format(target=Near_IP, main=Far_IP),
    'create_update.py -mn=Basic_MCS -jf=12_CM_D_T_S_PC -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=12_CM2_RW2_Render -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=12_CM2_T_RW2_Record -ip={}'.format(Near_IP),
    'RTMP_Push.py -mn=Basic_MCS -t={target} -ip={main}'.format(target=Far_IP, main=Near_IP),
    'RTMP_Pull.py -mn=Director_push -ip={}'.format(Far_IP),
    'RTMP_Push_Student.py -mn=Basic_MCS -t={target} -ip={main}'.format(target=Far_IP, main=Near_IP),
    'RTMP_Pull_Student.py -mn=Director_push -ip={}'.format(Far_IP),
    'remove.py -mn=Basic_MCS -sn=Compositor,TcpVideoA_pull,TcpVideoB_pull,TcpAudioA_pull,TcpAudioB_pull -ip={}'.format(
        Near_IP),
    'remove.py -mn=Director_push -sn=RTMP_Pull -ip={}'.format(Far_IP),
    'create_update.py -mn=Basic_MCS -jf=15_CM_TAi_SAi_B_Render -ip={}'.format(Near_IP)
]


def act_basic(ScriptList, sleeptime=2):
    # 先依次执行前面操作
    for items in ScriptList:
        os.system('python {}'.format(items))
        # print(items)
        time.sleep(sleeptime)


if __name__ == '__main__':
    act_basic(scriptlist, sleeptime=2)

