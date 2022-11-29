import os
import time
import sys
sys.path.append('../../Libraries')
from environmentlib import *

IP = input("Please Input An Host IP to Test: ")   # "127.0.0.1"

scriptlist = ['create_preview.py -d={} -mn=HDMI0 -p=1 -n=Teacher -ip={}'.format(Global_TeacherCamType,IP),
              'create_preview.py -d={} -mn=HDMI1 -p=2 -n=Student -ip={}'.format(Global_StudentCamType,IP),
              'create_preview.py -d={} -mn=USB0 -p=3 -n=USB1 -ip={}'.format(Global_BlackBoardCamType,IP),
              'create_preview.py -d={} -mn=USB1 -p=4 -n=USB2 -ip={}'.format(Global_PPTCamType,IP),
              ]


def act():
    for items in scriptlist:
        os.system('python {}'.format(items))
        time.sleep(1)


if __name__ == '__main__':
    act()
