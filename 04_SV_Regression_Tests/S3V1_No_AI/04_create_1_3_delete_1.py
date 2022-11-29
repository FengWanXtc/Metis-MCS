import sys
import os

sys.path.append('../../Libraries')

action_list = ['03_pull_remote_three.py',
               'delete_task_by_name.py -n=Remote_1',
               'delete_all_tasks.py'

]
Anouncestr = '''
****************************************
Please press Enter key to do next Action
'''

def act_story():
    for items in action_list:
        os.system('python {}'.format(items))
        input(Anouncestr)

if __name__ == '__main__':
    act_story()