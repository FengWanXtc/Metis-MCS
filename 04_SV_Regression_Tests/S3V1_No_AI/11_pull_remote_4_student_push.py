import time
import os


action_list = ['06_create_frames_1by1.py',
               'student_push.py'
               ]


def act_story():
    for items in action_list:
        os.system('python {}'.format(items))
        time.sleep(2)


if __name__ == '__main__':
    act_story()
