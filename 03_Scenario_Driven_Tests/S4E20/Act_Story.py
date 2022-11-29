import sys

sys.path.append('../../Libraries')
from functionlib import *

Near_IP = input("Please Input Near-End Metis IP: ")
Far_IP = input("Please Input Far-End Metis IP: ")
Anno = "************************************"

scriptlist = [
    '4F-CM_RW_RW_RW.py -ip={}'.format(Near_IP),
    'Director_push.py -t={target} -ip={main}'.format(main=Far_IP, target=Near_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_1_1 -ip={}'.format(Near_IP),
    'RTMP_Push.py -mn=Basic_MCS -t={target} -ip={main}'.format(main=Near_IP, target=Far_IP),
    'RTMP_Pull.py -mn=Director_push -ip={}'.format(Far_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_1_2 -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_1_3 -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_1_2 -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_1_1 -ip={}'.format(Near_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_1_0 -ip={}'.format(Near_IP)
]


def act_basic(ScriptList, sleeptime=2):
    # 先依次执行前面操作
    for items in ScriptList:
        os.system('python {}'.format(items))
        # print(items)
        time.sleep(sleeptime)


if __name__ == '__main__':
    act_basic(scriptlist, sleeptime=5)


"""
    'remove.py -mn=Basic_MCS -sn=Compose_RtspPush -ip={}'.format(Near_IP),
    'remove.py -mn=Director_push -sn=RTMP_Pull -ip={}'.format(Far_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_1_2 -ip={}'.format(Near_IP),
    'RTMP_Push.py -mn=Basic_MCS -t={target} -ip={main}'.format(main=Near_IP, target=Far_IP),
    'RTMP_Pull.py -mn=Director_push -ip={}'.format(Far_IP),
    'remove.py -mn=Basic_MCS -sn=Compose_RtspPush -ip={}'.format(Near_IP),
    'remove.py -mn=Director_push -sn=RTMP_Pull -ip={}'.format(Far_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_1_3 -ip={}'.format(Near_IP),
    'RTMP_Push.py -mn=Basic_MCS -t={target} -ip={main}'.format(main=Near_IP, target=Far_IP),
    'RTMP_Pull.py -mn=Director_push -ip={}'.format(Far_IP),
    'remove.py -mn=Basic_MCS -sn=Compose_RtspPush -ip={}'.format(Near_IP),
    'remove.py -mn=Director_push -sn=RTMP_Pull -ip={}'.format(Far_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_1_2 -ip={}'.format(Near_IP),
    'RTMP_Push.py -mn=Basic_MCS -t={target} -ip={main}'.format(main=Near_IP, target=Far_IP),
    'RTMP_Pull.py -mn=Director_push -ip={}'.format(Far_IP),
    'remove.py -mn=Basic_MCS -sn=Compose_RtspPush -ip={}'.format(Near_IP),
    'remove.py -mn=Director_push -sn=RTMP_Pull -ip={}'.format(Far_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_1_1 -ip={}'.format(Near_IP),
    'RTMP_Push.py -mn=Basic_MCS -t={target} -ip={main}'.format(main=Near_IP, target=Far_IP),
    'RTMP_Pull.py -mn=Director_push -ip={}'.format(Far_IP),
    'remove.py -mn=Basic_MCS -sn=Compose_RtspPush -ip={}'.format(Near_IP),
    'remove.py -mn=Director_push -sn=RTMP_Pull -ip={}'.format(Far_IP),
    'create_update.py -mn=Basic_MCS -jf=Compose_1_0 -ip={}'.format(Near_IP),
    'RTMP_Push.py -mn=Basic_MCS -t={target} -ip={main}'.format(main=Near_IP, target=Far_IP),
    'RTMP_Pull.py -mn=Director_push -ip={}'.format(Far_IP),
    'remove.py -mn=Basic_MCS -sn=Compose_RtspPush -ip={}'.format(Near_IP),
    'remove.py -mn=Director_push -sn=RTMP_Pull -ip={}'.format(Far_IP)
"""