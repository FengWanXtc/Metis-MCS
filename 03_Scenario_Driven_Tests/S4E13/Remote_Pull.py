import argparse
import json
import sys
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def basic():
    # 设置对应的MCS
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip
    data = read_json_file('Remote_Pull.json')
    DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType='IPC', aiStrategy='student')
    data['VideoSpecs'][1]['DeviceId'] = DeviceId
    # print(json.dumps(data,indent=2))
    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('Remote_Pull Test Pass!')
    else:
        print('Remote_Pull Test Fail!')
        print(response.json())


if __name__ == '__main__':
    basic()
