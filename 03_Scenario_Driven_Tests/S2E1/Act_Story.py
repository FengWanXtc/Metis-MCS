import sys
sys.path.append('../../Libraries')
from environmentlib import *
from functionlib import *

ActionList = ['create_one_frame_preview.py -n=Teacher -ct={} -cn=1 -g=0,0,960,540'.format(Global_GeneralCamType),
              'create_one_frame_preview.py -n=Student -ct=HDMI -cn=2 -g=960,0,960,540'.format(Global_GeneralCamType),
              'create_one_frame_preview.py -n=BlackBoard -ct={} -cn=3 -g=0,540,960,540'.format(Global_GeneralCamType),
              'create_one_frame_preview.py -n=PPT -ct={} -cn=1 -g=960,540,960,540'.format(Global_GeneralCamType_other),
              'change_geometry_animation.py',
              'delete_task_by_name.py -n=Teacher',
              'delete_task_by_name.py -n=Student',
              'delete_task_by_name.py -n=BlackBoard',
              'change_geometry.py -n=PPT -g=0,0,960,540',
              'change_geometry.py -n=PPT -g=0,0,1920,1080',
              'change_geometry.py -n=PPT -g=960,540,960,540',
              'create_one_frame_preview.py -n=Teacher -ct={} -cn=1 -g=0,0,960,540'.format(Global_GeneralCamType),
              'create_one_frame_preview.py -n=Student -ct=HDMI  -cn=2 -g=960,0,960,540'.format(Global_GeneralCamType),
              'create_one_frame_preview.py -n=BlackBoard -ct={} -cn=3 -g=0,540,960,540'.format(Global_GeneralCamType),
              'delete_all_tasks.py'
              ]

if __name__ == '__main__':
    act_story(ActionList, sleeptime=0.1)
