import sys
import threading

sys.path.append('../../Libraries')
from functionlib import *

Near_IP = input("Please Input Near-End Metis IP: ")
Far_IP = input("Please Input Far-End Metis IP: ")
Anno = "************************************"

scriptlist = [
    '4F-DR_RW_RW_RW.py -ip={}'.format(Near_IP),
    'Director_push.py -t={target} -ip={main}'.format(target=Near_IP, main=Far_IP),
    'create_update.py -mn=Basic_MCS -jf=07_D_3RW_Compose -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=07_3_V_A_Codec -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=07_D_3RW_Render -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=07_D_3RW_Record -ip={}'.format(Near_IP),
    'CM_Server.py -mn=Basic_MCS -t={target} -ip={main}'.format(target=Far_IP, main=Near_IP),
    'remove.py -mn=Basic_MCS -sn=Compositor,Compositor_Record,CompositorAudio -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=08_D_Compose -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=08_CM_Default_Transform -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=08_TF_3RW_Render -ip={}'.format(Near_IP),
    'TF_Record.py -mn=Basic_MCS -rn=D -ip={}'.format(Near_IP),
    'remove.py -mn=Basic_MCS -sn=Compositor_Server -ip={}'.format(Near_IP),
    'remove.py -mn=Director_push -sn=Remote_pull -ip={}'.format(Far_IP),
    'create_update.py -mn=Director_push -jf=Far_end_pull -ip={}'.format(Far_IP),
    'TF_Server.py -mn=Basic_MCS -t={target} -ip={main}'.format(target=Far_IP, main=Near_IP),
    'remove.py -mn=Basic_MCS -sn=VideoTransform,VideoTransform_Record,Compositor,VideoTransform_Server -ip={}'.format(Near_IP),
    'remove.py -mn=Director_push -sn=Remote_pull -ip={}'.format(Far_IP),
    'create_update.py -mn=Basic_MCS -jf=09_D_3W_Compose -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=09_CM_480_Transform -ip={}'.format(Near_IP),
    'TF_Record.py -mn=Basic_MCS -rn=D_3RW -ip={}'.format(Near_IP),
    'create_update.py -mn=Director_push -jf=Far_end_pull -ip={}'.format(Far_IP),
    'TF_Server.py -mn=Basic_MCS -t={}'.format(Far_IP),
    'remove.py -mn=Basic_MCS -sn=VideoTransform,VideoTransform_Record,Compositor,VideoTransform_Server -ip={}'.format(Near_IP),
    'remove.py -mn=Director_push -sn=Remote_pull -ip={}'.format(Far_IP),
    'remove.py -mn=Basic_MCS -sn=Remote_pull_Record,Remote_pull_2_Record,Remote_pull_3_Record -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=10_T_2RW_Transform -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=10_D_T_2RW_TF_Compose -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=10_CM_T_2RW_Render -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=10_CM_T_2RW_Record -ip={}'.format(Near_IP),
    'create_update.py -mn=Director_push -jf=Far_end_pull -ip={}'.format(Far_IP),
    'CM_Video_Push.py  -mn=Basic_MCS -t={target} -ip={main}'.format(target=Far_IP, main=Near_IP),
    'create_update.py -mn=Basic_MCS -jf=11_9_Render -ip={}'.format(Near_IP)
]


def act_basic(ScriptList, sleeptime=5):
    # 先依次执行前面操作
    for items in ScriptList:
        os.system('python {}'.format(items))
        # print(items)
        time.sleep(sleeptime)


if __name__ == '__main__':
    act_basic(scriptlist, sleeptime=2)

