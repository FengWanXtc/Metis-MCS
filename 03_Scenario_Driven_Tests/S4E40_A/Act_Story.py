import sys

sys.path.append('../../Libraries')
from functionlib import *

Near_IP = input("Please Input Near-End Metis IP: ")
Far_IP = input("Please Input Far-End Metis IP: ")
Anno = "************************************"

scriptlist = ['4F-4.1DR-4.2S-4.3T-4.4RT.py -ip={}'.format(Near_IP),
              'Director_push.py -ip={}'.format(Far_IP),
              'create_update.py -mn=Basic_MCS -jf=T_S_Record -ip={}'.format(Near_IP),
              'remove.py -mn=Basic_MCS -ip={} -sn=Teacher_Record,Student_Record'.format(
                  Near_IP),
              'create_update.py -mn=Basic_MCS -jf=TAi_SAi_PC_Record -ip={}'.format(Near_IP),
              'suspend.py -mn=Basic_MCS -ip={} -sn=Director_Record,TeacherAi_Record,StudentAi_Record,ComputerAi_Record'.format(
                  Near_IP),
              'remove.py -mn=Basic_MCS -ip={} -sn=TeacherAi_Record,StudentAi_Record'.format(
                  Near_IP),
              'resume.py -mn=Basic_MCS -ip={} -sn=TeacherAi_Record,ComputerAi_Record'.format(
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