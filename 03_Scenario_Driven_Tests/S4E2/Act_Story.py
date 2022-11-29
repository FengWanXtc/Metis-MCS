import sys

sys.path.append('../../Libraries')
from functionlib import *

actionlist = ['static_record.py',
              'dynamic_preview.py',
              'record_start.py',
              'delete_task_by_name.py -n=static_record',
              'static_record.py',
              'remove.py -mn=S4E2_Dynamic -sn=Dynamic_Record',
              'delete_all_tasks.py'
              ]


# 进行动作脚本
def act():
    for item in actionlist:
        os.system('python {}'.format(item))
        time.sleep(5)


if __name__ == '__main__':
    act()
