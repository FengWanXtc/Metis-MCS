import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def pull_remote(ip):
    pull_re_4_data = read_json_file('02_pull_remote_four.json')
    try:
        response = post_mt_create_update(ip=ip, data=pull_re_4_data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Create Remote four frames Success')
        return True
    else:
        print('Create Remote four frames Fail')
        return False


def main():
    parser = argparse.ArgumentParser(description='usage: python3 pull_remote.py --template=four frame')
    parser.add_argument('-ip', type=str, default='', help='The ip of the station.')
    args = parser.parse_args()
    IP = args.ip
    pull_remote(IP)


if __name__ == '__main__':
    main()