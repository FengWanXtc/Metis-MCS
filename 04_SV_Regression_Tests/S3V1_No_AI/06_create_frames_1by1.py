import os
import time

action_list = ['01_pull_remote.py',
               '01_pull_remote.py -mn=Remote_2 -p=2',
               '01_pull_remote.py -mn=Remote_3 -p=3',
               '01_pull_remote.py -mn=Remote_4 -p=4',
               ]


def act_story():
    for items in action_list:
        os.system('python {}'.format(items))
        time.sleep(1)


if __name__ == '__main__':
    act_story()
