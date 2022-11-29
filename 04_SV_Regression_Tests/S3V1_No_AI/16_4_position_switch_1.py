import sys

sys.path.append('../../Libraries')
from functionlib import *

Anouncestr = '''
*****************************************
Please press Enter key to do next Action:
'''

Anno = "***************************************************"

action_list = [
    'create_update.py -mn=PC_Preview -jf=PC_Preview',
    'create_update.py -mn=Blackboard_Preview -jf=Blackboard_Preview',
    '01_pull_remote.py',
    '01_pull_remote.py -mn=Remote_4 -p=4',
    'teacher_record.py',
    'student_push.py',
    'delete_task_by_name.py -n=Blackboard_Preview',
    'delete_task_by_name.py -n=Remote_1',
    'delete_task_by_name.py -n=Remote_4',
    'create_update.py -mn=Blackboard_Preview -jf=Blackboard_Preview',
    '01_pull_remote.py',
    '01_pull_remote.py -mn=Remote_4 -p=4',
    'delete_task_by_name.py -n=Blackboard_Preview',
    'delete_task_by_name.py -n=Remote_1',
    'delete_task_by_name.py -n=PC_Preview',
    'delete_task_by_name.py -n=Teacher_Record',
    'delete_task_by_name.py -n=Student_Push',
    'delete_task_by_name.py -n=Remote_4',
    'create_update.py -mn=Remote_One -jf=Remote_One'

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
