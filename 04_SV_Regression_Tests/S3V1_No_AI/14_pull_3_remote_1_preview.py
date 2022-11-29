import os
import time

Anouncestr = '\n******Please press Enter key to do next Action******\n'

action_list = ['01_pull_remote.py',
               '01_pull_remote.py -mn=Remote_2 -p=2',
               '01_pull_remote.py -mn=Remote_3 -p=3',
               'student_push.py',
               'teacher_record_preview.py -p=4'
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
