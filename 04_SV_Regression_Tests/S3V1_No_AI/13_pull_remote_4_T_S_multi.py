import sys

sys.path.append('../../Libraries')
from functionlib import *

Anouncestr = '''
*****************************************
Please press Enter key to do next Action
*****************************************
'''

action_list = ['06_create_frames_1by1.py',
               'student_push.py',
               'teacher_record.py',
               'delete_task_by_name.py -n=Teacher_Record',
               'teacher_record.py',
               'delete_task_by_name.py -n=Remote_1',
               'delete_task_by_name.py -n=Remote_2',
               '01_pull_remote.py',
               '01_pull_remote.py -mn=Remote_2 -p=2'
               ]


def act_story():
    for items in action_list:
        os.system('python {}'.format(items))
        input(Anouncestr)


if __name__ == '__main__':
    act_story()
