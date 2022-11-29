import sys

sys.path.append('../../Libraries')
from functionlib import *

Anouncestr = '''
*****************************************
Please press Enter key to do next Action:
'''

Anno = "***************************************************"

action_list = ['01_pull_remote.py',
               '01_pull_remote.py -mn=Remote_2 -p=2',
               '01_pull_remote.py -mn=Remote_3 -p=3',
               'student_push_preview.py -p=4',
               'delete_task_by_name.py -n=Remote_1',
               'teacher_record_preview.py -p=1',
               'delete_task_by_name.py -n=Remote_2',
               'create_update.py -mn=PC_Preview -jf=PC_Preview',
               'delete_task_by_name.py -n=Remote_3',
               'create_update.py -mn=Blackboard_Preview -jf=Blackboard_Preview',
               ]


def act_story():
    for items in action_list:
        if items != action_list[-1]:
            os.system('python {}'.format(items))
            input(Anouncestr)
        else:
            os.system('python {}'.format(items))
            time.sleep(1)
            print("\n*********All Tests End!Please Delete All Tasks*********\n")


if __name__ == '__main__':
    act_story()
