import os
import time

action_list = ['rtsp_pull.py -mn=RTSP_1 -p=1 -uri=48/ch1',
               'rtsp_pull.py -mn=RTSP_2 -p=2 -uri=56/ch2',
               'rtsp_pull.py -mn=RTSP_3 -p=3 -uri=57/ch1',
               'rtsp_pull.py -mn=RTSP_4 -p=4 -uri=57/ch2',
               ]


def act_story():
    for items in action_list:
        os.system('python {}'.format(items))
        time.sleep(1)


if __name__ == '__main__':
    act_story()
