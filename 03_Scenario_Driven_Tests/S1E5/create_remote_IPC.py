import sys
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def create_remote_IPC():
    cre_rem_data = read_json_file('create_remote_IPC.json')
    try:
        response = post_mt_create_update(ip='', data=cre_rem_data)
    except:
        print('Post Create Remote IPC Task Failed')
        print(response.json())

    if response.status_code == 200:
        print('S1E5 Action::Create Remote IPC Test Pass!')
        return True
    else:
        print('S1E5 Action::Create Remote IPC Test Fail!')
        print(response.json())
        return response.json()


if __name__ == '__main__':
    create_remote_IPC()
