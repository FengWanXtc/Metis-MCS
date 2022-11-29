import sys

sys.path.append('../../Libraries')
from functionlib import *

Near_IP = input("Please Input Near-End Metis IP: ")
Far_IP = input("Please Input Far-End Metis IP: ")
Anno = "************************************"

scriptlist = [
    'TransformBasic.py -ip={}'.format(Near_IP),
    'Remote_Pull.py -ip={}'.format(Far_IP),
    'TransformPush.py -ip={main} -t={target}'.format(main=Near_IP, target=Far_IP),
    'remove.py -mn=Basic_MCS -sn=VideoTransform,VideoTransform_Server -ip={}'.format(Near_IP),
    'remove.py -mn=Director_push -sn=Remote_pull -ip={}'.format(Far_IP),
    'create_update.py -ip={} -jf=Pull_Again -mn=Director_push'.format(Far_IP),
    'Transform.py -w=1920 --h=1080 -ip={main} -t={target}'.format(main=Near_IP, target=Far_IP),
    'remove.py -mn=Basic_MCS -sn=VideoTransform,VideoTransform_Server -ip={}'.format(Near_IP),
    'remove.py -mn=Director_push -sn=Remote_pull -ip={}'.format(Far_IP),
    'create_update.py -ip={} -jf=Pull_Again -mn=Director_push'.format(Far_IP),
    'Transform.py -w=1080 --h=720 -ip={main} -t={target}'.format(main=Near_IP, target=Far_IP),
    'remove.py -mn=Basic_MCS -sn=VideoTransform,VideoTransform_Server -ip={}'.format(Near_IP),
    'remove.py -mn=Director_push -sn=Remote_pull -ip={}'.format(Far_IP),
    'create_update.py -ip={} -jf=Pull_Again -mn=Director_push'.format(Far_IP),
    'Transform.py -w=640 --h=480 -ip={main} -t={target}'.format(main=Near_IP, target=Far_IP),
    'remove.py -mn=Basic_MCS -sn=VideoTransform,VideoTransform_Server -ip={}'.format(Near_IP),
    'remove.py -mn=Director_push -sn=Remote_pull -ip={}'.format(Far_IP),
    'create_update.py -ip={} -jf=Pull_Again -mn=Director_push'.format(Far_IP),
    'Transform.py -w=480 --h=270 -ip={main} -t={target}'.format(main=Near_IP, target=Far_IP),
    'remove.py -mn=Basic_MCS -sn=VideoTransform,VideoTransform_Server -ip={}'.format(Near_IP),
    'remove.py -mn=Director_push -sn=Remote_pull -ip={}'.format(Far_IP),
    'create_update.py -ip={} -jf=Pull_Again -mn=Director_push'.format(Far_IP),
    'Transform.py -w=1920 --h=1080 -ip={main} -t={target}'.format(main=Near_IP, target=Far_IP),
]


def act_basic(ScriptList, sleeptime=2):
    # 先依次执行前面操作
    for items in ScriptList:
        os.system('python {}'.format(items))
        # print(items)
        time.sleep(sleeptime)


if __name__ == '__main__':
    act_basic(scriptlist, sleeptime=3)

