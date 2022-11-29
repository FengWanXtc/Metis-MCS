import sys

sys.path.append('../../Libraries')
from functionlib import *

Near_IP = input("Please Input Near-End Metis IP: ")
Far_IP = input("Please Input Far-End Metis IP: ")
Anno = "*********************************************************"

scriptlist = ['4F-4.1DR-4.2RW-4.3RW-4.4RW.py -ip={}'.format(Near_IP),
              'Director_push.py -t={target} -ip={main}'.format(main=Far_IP, target=Near_IP),
              'create_update.py -mn=Basic_MCS -jf=RW_Record -ip={}'.format(Near_IP),
              'create_update.py -mn=Basic_MCS -jf=RW2_Record -ip={}'.format(Near_IP),
              'create_update.py -mn=Basic_MCS -jf=Teacher_Record -ip={}'.format(Near_IP),
              'remove.py -mn=Basic_MCS -sn=Teacher_Record -ip={}'.format(Near_IP),
              'create_update.py -mn=Basic_MCS -jf=RW3_Record -ip={}'.format(Near_IP)
              ]


def act_basic(ScriptList, sleeptime=5):
    # 先依次执行前面操作
    for items in ScriptList:
        os.system('python {}'.format(items))
        # print(items)
        time.sleep(sleeptime)


if __name__ == '__main__':
    act_basic(scriptlist, sleeptime=10)
    # os.system('python resume.py -mn=Basic_MCS -sn=Teacher_Record,Computer_Record')
