import datetime
import os
import time

Far_End_IP = input("Please Input Far End Host IP to Pull Streams: ")

Anouncestr = '\n******Please press Enter key to do next Action******\n'

action_list = ['HDMI_With_Audio_NoRender.py',
               'pull_preview.py -ip={}'.format(Far_End_IP),
               ]

action_list_2 = ['USB_With_Audio_NoRender.py',
                 'pull_preview.py -ip={}'.format(Far_End_IP),
                 ]


def act_story(lists):
    for items in lists:
        if items != lists[-1]:
            os.system('python {}'.format(items))
            input(Anouncestr)
        else:
            os.system('python {}'.format(items))
            time.sleep(1)

        preTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("*********** The Test Start Time is {} ************".format(preTime))


if __name__ == '__main__':
    act_story(action_list)
    input("After 45 Minutes Please Press Enter Key to Start USBCameraTest")
    os.system('python delete_all_tasks.py')
    os.system('python delete_all_tasks.py ip={}'.format(Far_End_IP))
    act_story(action_list_2)
