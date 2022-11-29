import sys
import os
import argparse
import time

sys.path.append('../../Libraries')

action_list = ['create_remote.py -n=Remote_1 -g=0,0,960,540 -i=RT_1',
               'create_remote.py -n=Remote_2 -g=960,0,960,540 -i=RT_2',
               'create_remote.py -n=Remote_3 -g=0,540,960,540 -i=RT_3',
               'create_remote.py -n=Remote_4 -g=960,540,960,540 -i=RT_4',
               ]


def act_story():
    for items in action_list:
        os.system('python {}'.format(items))
        time.sleep(1)


if __name__ == '__main__':
    act_story()
