import sys
sys.path.append('../../Libraries')
from functionlib import *

scriptlist = ['create_UI.py -t=png',
              'create_preview.py -cn=1 -g=0,0,960,540',
              'delete_all_tasks.py',
              'create_UI.py -t=jpg',
              'create_preview.py -cn=1 -g=0,0,1920,1080',
              'delete_all_tasks.py',
              'create_UI.py -t=null',
              ]


def act():
    for items in scriptlist:
        os.system('python {}'.format(items))
        time.sleep(5)


if __name__ == '__main__':
    act()

