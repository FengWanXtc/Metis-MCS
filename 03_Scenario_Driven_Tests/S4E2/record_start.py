import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def record_start(IP):
    record_data = read_json_file('record_start.json')

    try:
        response = post_mt_create_update(ip=IP, data=record_data)
    except:
        print('Post Record Action Failed.')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Post Record Frame Success')
        return True
    else:
        print('Post Record Frame Success')
        return False


def main():
    parser = argparse.ArgumentParser(description='usage: python3 dynamic_record.py')
    parser.add_argument('-ip', type=str, default='', help='The Host IP')
    args = parser.parse_args()
    IP = args.ip
    record_start(IP)


if __name__ == '__main__':
    main()
