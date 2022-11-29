import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def audio_push(IP):
    data = read_json_file('Audio_01_push.json')
    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(TaskId)
    except:
        print('Audio Push Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Audio Push Task Success')
        return True
    else:
        print('Audio Push Task Fail')
        return False


def main():
    parser = argparse.ArgumentParser(description='usage: python3 XXXXX.py --ip=XXXXX')
    parser.add_argument('-ip', type=str, default='', help='The ip of the station.')
    args = parser.parse_args()
    IP = args.ip
    audio_push(IP)


if __name__ == '__main__':
    main()
