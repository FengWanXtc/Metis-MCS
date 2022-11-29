import datetime
import os
import time

Far_End_IP = input("Please Input Far End Host IP to Pull Streams: ")

Anouncestr = '\n******Please press Enter key to do next Action******\n'

action_list = ['HDMI_With_Audio_NoRender.py',
               'pull_preview.py -ip={}'.format(Far_End_IP),
               'create_update.py -mn=HDMI_0 -jf=Near_End_Record',
               'create_update.py -mn=Pull_Preview -jf=Far_End_Volume -ip={}'.format(Far_End_IP)
               ]


def act_story(lists):
    for items in lists:
        if items != lists[-1]:
            os.system('python {}'.format(items))
            input(Anouncestr)
        else:
            os.system('python {}'.format(items))
            time.sleep(1)
            print("****************All Tests Ends! Please Delete All Tasks***************")


if __name__ == '__main__':
    act_story(action_list)
