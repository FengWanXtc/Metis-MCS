import sys
import datetime
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
    'student_push.py'
]


def act_story():
    for items in action_list:
        os.system('python {}'.format(items))
        time.sleep(1)

    preTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("*********** The Test Start Time is {} ************".format(preTime))


if __name__ == '__main__':
    act_story()
