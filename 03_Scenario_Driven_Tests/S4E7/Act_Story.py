import sys

sys.path.append('../../Libraries')
from functionlib import *

Near_IP = input("Please Input Near-End Metis IP: ")
Far_IP = input("Please Input Far-End Metis IP: ")
Anno = "*********************************************************"

scriptlist = ['4F-4.1DR-4.2RW-4.3RW-4.4RW.py -ip={}'.format(Near_IP),
              'Director_push.py -t={target} -ip={main}'.format(main=Far_IP, target=Near_IP),
              'remove.py -mn=Basic_MCS -sn=Remote_pull_2,Remote_pull_3,Audio_pull_2,Audio_pull_3 -ip={}'.format(
                  Near_IP),
              'remove.py -ip={} -mn=Director_push -sn=Teacher_Server,Teacher_Audio_Server,Student_Server,Student_Audio_Server'.format(
                  Far_IP),
              'create_update.py -mn=Basic_MCS -jf=TAi_SAi_BAi_Record -ip={}'.format(Near_IP),
              'V_A_Server.py -ip={main} -mn=Director_push -t={target}'.format(main=Far_IP, target=Near_IP),
              'remove.py -mn=Basic_MCS -sn=Remote_pull_2,Audio_pull_3,TeacherAi_Record,StudentAi_Record,BlackboardAi_Record -ip={}'.format(
                  Near_IP),
              "create_update.py -mn=Basic_MCS -jf=RW_RW_Pull -ip={}".format(Near_IP),
              "V_A_2_Server.py -ip={main} -mn=Director_push -t={target}".format(main=Far_IP, target=Near_IP)
              ]

def act_basic(ScriptList, sleeptime=5):
    # 先依次执行前面操作
    for items in ScriptList:
        os.system('python {}'.format(items))
        # print(items)
        time.sleep(sleeptime)


if __name__ == '__main__':
    act_basic(scriptlist, sleeptime=5)
    # os.system('python resume.py -mn=Basic_MCS -sn=Teacher_Record,Computer_Record')
