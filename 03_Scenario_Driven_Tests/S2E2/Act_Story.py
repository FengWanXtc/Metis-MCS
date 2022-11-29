import sys
sys.path.append('../../Libraries')
from environmentlib import *
from functionlib import *

Description = '''
***************************Description***************************
Four Frames : 1 is Director , 2 is Student , 
              3 is Blackboard , 4 is PPT .
0.Create four frames:
1.Maximize Frame 1
2.Maximize Frame 2
3.Maximize Frame 3
4.Maximize Frame 4
5.Exit 
*****************************************************************
'''
warningStr = '''
**********************************
Warning:Please input right number!
**********************************
'''
station_init = ['create_one_frame_preview.py -n=Teacher -ct={} -cn=1 -g=0,0,960,540'.format(Global_GeneralCamType),
                'create_one_frame_preview.py -n=Student -ct={} -cn=2 -g=960,0,960,540'.format(Global_GeneralCamType),
                'create_one_frame_preview.py -n=Blackboard -ct={} -cn=3 -g=0,540,960,540'.format(Global_GeneralCamType),
                'create_one_frame_preview.py -n=PPT -ct={} -cn=1 -g=960,540,960,540'.format(Global_GeneralCamType_other),
                ]
station_0 = {
    1: ['change_geometry.py -n=Teacher -g=0,0,1920,1080',

        ],
    2: ['change_geometry.py -n=Student -g=0,0,1920,1080',

        ],
    3: ['change_geometry.py -n=Blackboard -g=0,0,1920,1080',

        ],
    4: ['change_geometry.py -n=PPT -g=0,0,1920,1080',

        ]
}
station_1 = {
    0: [
        'change_geometry.py -n=Teacher -g=0,0,960,540',
    ],
    2: ['change_geometry.py -n=Teacher -g=0,0,960,540',
        'change_geometry.py -n=Student -g=0,0,1920,1080'

        ],
    3: ['change_geometry.py -n=Teacher -g=0,0,960,540',
        'change_geometry.py -n=Blackboard -g=0,0,1920,1080',
        1
        ],
    4: ['change_geometry.py -n=Teacher -g=0,0,960,540',
        'change_geometry.py -n=PPT -g=0,0,1920,1080',

        ]
}

station_2 = {
    0: [
        'change_geometry.py -n=Student -g=960,0,960,540',
    ],
    1: ['change_geometry.py -n=Student -g=960,0,960,540',
        'change_geometry.py -n=Teacher -g=0,0,1920,1080',

        ],
    3: ['change_geometry.py -n=Student -g=960,0,960,540',
        'change_geometry.py -n=Blackboard -g=0,0,1920,1080',

        ],
    4: ['change_geometry.py -n=Student -g=960,0,960,540',
        'change_geometry.py -n=PPT -g=0,0,1920,1080',

        ]
}

station_3 = {
    0: [
        'change_geometry.py -n=Blackboard -g=0,540,960,540',
    ],
    1: ['change_geometry.py -n=Blackboard -g=0,540,960,540',
        'change_geometry.py -n=Teacher -g=0,0,1920,1080',

        ],
    2: ['change_geometry.py -n=Blackboard -g=0,540,960,540',
        'change_geometry.py -n=Student -g=0,0,1920,1080',

        ],
    4: ['change_geometry.py -n=Blackboard -g=0,540,960,540',
        'change_geometry.py -n=PPT -g=0,0,1920,1080',

        ]
}

station_4 = {
    0: [
        'change_geometry.py -n=PPT -g=960,540,960,540',
    ],
    1: ['change_geometry.py -n=PPT -g=960,540,960,540',
        'change_geometry.py -n=Teacher -g=0,0,1920,1080',

        ],
    2: ['change_geometry.py -n=PPT -g=960,540,960,540',
        'change_geometry.py -n=Student -g=0,0,1920,1080',

        ],
    3: ['change_geometry.py -n=PPT -g=960,540,960,540',
        'change_geometry.py -n=Blackboard -g=0,0,1920,1080',

        ]
}

station_5 = ['delete_all_tasks.py']

switch_list = {
    0: station_0,
    1: station_1,
    2: station_2,
    3: station_3,
    4: station_4,
    5: station_5
}

if __name__ == '__main__':
    act_story(station_init, sleeptime=0)
    present_number = 0
    while True:
        print(Description)
        try:
            number = int(input('Please input a number :'))
        except:
            print(warningStr)
            continue
        if number == present_number or number < 0 or number > 5:
            print(warningStr)
            continue
        if number == 5:
            act_story(station_5, sleeptime=0.2)
            break
        act_story(switch_list[present_number][number], sleeptime=0.2)
        present_number = number
