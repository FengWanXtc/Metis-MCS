import sys
import threading
import time

sys.path.append('../../Libraries')
from functionlib import *

Near_IP = input("Please Input Near-End Metis IP: ")
Far_IP = input("Please Input Far-End Metis IP: ")
Anno = "*********************************************************"

scriptlist = ['create_update.py -mn=Basic_MCS -jf=D_TAi_SAi_PCAi_Render -ip={}'.format(Near_IP),
              'remove.py -mn=Basic_MCS -sn=Render_test -ip={}'.format(Near_IP),
              'create_update.py -mn=Basic_MCS -jf=TP_Render -ip={}'.format(Near_IP),
              'remove.py -mn=Basic_MCS -sn=Render_test -ip={}'.format(Near_IP),
              'create_update.py -mn=Basic_MCS -jf=D_T_S_RT_Render -ip={}'.format(Near_IP),
              'remove.py -mn=Basic_MCS -sn=Render_test -ip={}'.format(Near_IP),
              'create_update.py -mn=Basic_MCS -jf=D_RT_RT2_RT3_Render -ip={}'.format(Near_IP),
              'V_A_2_Push.py -ip={main} -t={target}'.format(main=Far_IP, target=Near_IP),
              'remove.py -mn=Basic_MCS -sn=Teacher_Record,Student_Record,Computer_Record -ip={}'.format(Near_IP)
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
