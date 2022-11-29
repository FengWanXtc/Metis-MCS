import os
import time

Far_End_IP = input("Please Input Far End Host IP to Pull Streams: ")
Far_End_2_IP = input("Please Input Far End (Another) Host IP to Pull and Push Streams: ")

Anouncestr = '\n******Please press Enter key to do next Action******\n'

action_list = ['USB_With_Audio_NoRender.py',
               'pull_preview.py -ip={}'.format(Far_End_IP),
               'pull_push_preview.py -ip={}'.format(Far_End_2_IP),
               'delete_all_tasks.py',
               'delete_all_tasks.py -ip={}'.format(Far_End_IP),
               'delete_all_tasks.py -ip={}'.format(Far_End_2_IP),
               'HDMI_With_Audio_NoRender.py',
               'pull_preview.py -ip={}'.format(Far_End_IP),
               'pull_push_preview.py -ip={}'.format(Far_End_2_IP),
               'delete_all_tasks.py',
               'delete_all_tasks.py -ip={}'.format(Far_End_IP),
               'delete_all_tasks.py -ip={}'.format(Far_End_2_IP),
               ]


def act_story():
    for items in action_list:
        if items != action_list[-1]:
            os.system('python {}'.format(items))
            input(Anouncestr)
        else:
            os.system('python {}'.format(items))
            time.sleep(1)
            print("\n***************All Tests End!*************\n")


if __name__ == '__main__':
    act_story()
