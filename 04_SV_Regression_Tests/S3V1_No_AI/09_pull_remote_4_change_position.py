import os
import time

action_list = ['08_pull_remote_four_rtsp.py',
               'create_update.py -mn=RTSP_Pull_4F -jf=change_position_08'
               ]


def act_story():
    for items in action_list:
        os.system('python {}'.format(items))
        time.sleep(2)


if __name__ == '__main__':
    act_story()
