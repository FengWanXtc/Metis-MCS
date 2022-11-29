import argparse
import sys

sys.path.append('../../Libraries')
from mediatasklib import *


def main():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip
    response = get_mt_tasks(ip=IP)
    Names = response.json()['Names']

    if response.json()['Code'] == 200:
        print('Get Tasks Name Success.Tasks List As Follow:')
        print(Names)
    else:
        print('Get Tasks Name Fail')
        print(response.json())
        return False

    for NameItem in Names:
        # 如果有任务就会继续执行，如果没有就不会执行下面语句
        response = delete_mt_MCS_Name(IP, NameItem, token='')
        if response.json()['Code'] == 200:
            print('Delete MCS_Name {} Success!'.format(NameItem))
        else:
            print('Delete MCS_Name {} Fail!'.format(NameItem))
            print(response.text)
            return False
    print('****************Delete all Tasks Success!****************')


if __name__ == '__main__':
    main()
