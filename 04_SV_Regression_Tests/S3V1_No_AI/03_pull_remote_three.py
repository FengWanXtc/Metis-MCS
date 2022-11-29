import sys
import argparse
import time

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def pull_remote_three(IP):
    data = read_json_file('03_pull_remote_three.json')
    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(TaskId)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Create Remote three frames Success')
        return True
    else:
        print('Create Remote three frames Fail')
        return False


def main():
    parser = argparse.ArgumentParser(description='usage: python3 pull_remote.py --template=four frame')
    parser.add_argument('-ip', type=str, default='', help='The ip of the station.')
    args = parser.parse_args()
    IP = args.ip
    os.system('python 01_pull_remote.py -ip={}'.format(IP))
    time.sleep(2)
    pull_remote_three(IP)


if __name__ == '__main__':

    main()
