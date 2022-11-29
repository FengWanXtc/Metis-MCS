import sys
import time

sys.path.append('../../Libraries')
from environmentlib import *
from functionlib import *

TeacherCamType = Global_TeacherCamType
StudentCamType = Global_StudentCamType

scriptlist = ['4F-4.1D1PAR-4.2T-4.3S.py -TCam={tea} -SCam={stu}'.format(tea=TeacherCamType, stu=StudentCamType),
              'create_remote_IPC.py',
              'delete_task_by_name_rtc.py -n=S1E5_Main',
              'change_IPC_geometry_animation.py',
              '4F-4.1D1PAR-4.2T-4.3S.py -TCam={tea} -SCam={stu}'.format(tea=TeacherCamType, stu=StudentCamType),
              'delete_task_by_name_rtc.py -n=S1E5_Main',
              'delete_all_tasks.py'
              ]


if __name__ == '__main__':
    act_story(scriptlist, 2)
