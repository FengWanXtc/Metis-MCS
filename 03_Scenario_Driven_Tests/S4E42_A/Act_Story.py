import sys

sys.path.append('../../Libraries')
from functionlib import *

Near_IP = input("Please Input Near-End Metis IP: ")
Far_IP = input("Please Input Far-End Metis IP: ")
Anno = "************************************"

scriptlist = ['4F-4.1DR-4.2S-4.3T-4.4RT.py -ip={}'.format(Near_IP),
              'Director_push.py -ip={}'.format(Far_IP),
              'remove.py -mn=Basic_MCS -ip={} -sn=Rtc_Spec'.format(
                  Near_IP),
              'create_update.py -mn=Basic_MCS -jf=CM_D_T -ip={}'.format(Near_IP),
              'create_update.py -mn=Basic_MCS -jf=CM_Record_Render -ip={}'.format(Near_IP),
              'remove.py -mn=Basic_MCS -ip={} -sn=Compositor,Compose_Record,Rtc_Spec,Compositor_h264_Codec'.format(
                  Near_IP),
              'create_update.py -mn=Basic_MCS -jf=CM_T_S -ip={}'.format(Near_IP),
              'remove.py -mn=Basic_MCS -ip={} -sn=Compositor,Compose_Record,Rtc_Spec,Compositor_h264_Codec'.format(
                  Near_IP),
              'create_update.py -mn=Basic_MCS -jf=CM_D_T_P -ip={}'.format(Near_IP),
              'remove.py -mn=Basic_MCS -ip={} -sn=Compositor,Compose_Record,Rtc_Spec,Compositor_h264_Codec'.format(
                  Near_IP),
              'create_update.py -mn=Basic_MCS -jf=CM_D_T_S_P -ip={}'.format(Near_IP),
              'remove.py -mn=Basic_MCS -ip={} -sn=Compositor,Compose_Record,Rtc_Spec,Compositor_h264_Codec'.format(
                  Near_IP)
              ]


def act_episode(ScriptList):
    # 故事演绎脚本,传入动作列表依次执行动作
    for items in ScriptList:
        os.system('python {}'.format(items))
        # input(":: Please Press Enter Key to do Next Action")
        time.sleep(2)
    print('Episode Ends.Thanks for Watching')


if __name__ == '__main__':
    act_episode(scriptlist)
