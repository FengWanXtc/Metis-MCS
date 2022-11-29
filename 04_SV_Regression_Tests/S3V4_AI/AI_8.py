import os
import sys
sys.path.append('../../Libraries')
from functionlib import *


scriptlist = ['AI_2_remote.py',
              'create_update.py -mn=AI_2_Push -jf=AI_2_push_render',
              'create_update.py -mn=AI_2_Pull -jf=AI_2_remote_render',
              'delete_task_by_name.py -n=AI_2_Push',
              'AI_Audio_push.py',
              'delete_task_by_name.py -n=AI_2_Pull',
              'post_background.py -bg=jpg',
              'post_background.py -bg=null',
              'create_update.py -mn=AI_3_Push_Audio -jf=AI_5_record'
              ]


def act_basic(ScriptList):
    # 先依次执行前面操作
    for items in ScriptList:
        os.system('python {}'.format(items))
        # print(items)
        input("\n*************** Please Press Enter Key to do Next Action ******************")


if __name__ == '__main__':
    act_basic(scriptlist)
    # os.system('python resume.py -mn=Basic_MCS -sn=Teacher_Record,Computer_Record')
