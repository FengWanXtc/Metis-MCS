import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *


def main():
    parser = argparse.ArgumentParser(description='usage: python delete_task_by_name --ip=10.12.224.135 -n=Teacher')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('--name', '-n', required=True, help='The Name of MCS Task')
    args = parser.parse_args()
    IP = args.ip
    NAME = args.name
    response = delete_mt_MCS_Name(IP, NAME)
    # print(response.json())

    if response.json()['Code'] == 200:
        print('Delete MCS_Name ({}) Success!'.format(NAME))
    else:
        print('Delete MCS_Name ({}) Fail!'.format(NAME))
        print(response.text)
        return False


if __name__ == '__main__':
    main()
