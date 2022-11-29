import os
import time
import sys
sys.path.append('../../Libraries')
from environmentlib import *
IP = input("Please Input An Host IP to Test: ")

scriptlist_1 = ['create_preview.py -d={} -mn=HDMI0 -p=1 -n=Teacher -ip={}'.format(Global_TeacherCamType,IP),
                'create_preview.py -d={} -mn=HDMI1 -p=2 -n=Student -ip={}'.format(Global_StudentCamType,IP),
                'create_preview.py -d={} -mn=HDMI2 -p=3 -n=USB1 -ip={}'.format(Global_BlackBoardCamType,IP),
                'create_preview.py -d={} -mn=USB0 -p=4 -n=USB2 -ip={}'.format(Global_PPTCamType,IP),
                ]

scriptlist_2 = ['delete_task_by_name.py -n=HDMI0 -ip={}'.format(IP),
                'create_preview.py -d={} -mn=PC -p=1 -n=PC -ip={}'.format(Global_BlackBoardCamType,IP),
                ]

Announce = '''
************************************************************
Please Insert Pc into HDMI IN Port and Set camera status to
open in Local Manager Website.And then press Enter key.
************************************************************
'''


def act(actlist):
    for items in actlist:
        os.system('python {}'.format(items))
        time.sleep(2)


if __name__ == '__main__':
    act(scriptlist_1)
    input(Announce)
    act(scriptlist_2)
