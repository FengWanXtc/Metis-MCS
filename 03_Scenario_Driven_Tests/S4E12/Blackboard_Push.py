import argparse
import sys
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def basic():
    # 设置对应的MCS
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('--target', '-t', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip
    Target = args.target

    data = read_json_file('Blackboard_Push.json')
    # CAM1、CAM2、CAM_IN 的 DeviceId基本已定,需修改的是IPC
    DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType='IPC', aiStrategy='blackboard')
    data['VideoSpecs'][0]['DeviceId'] = DeviceId
    data["ServerSpecs"][0]["URI"] = "tcp://{}:6671".format(Target)

    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('Blackboard Push Test Pass!')
    else:
        print('Blackboard Push Test Fail!')
        print(response.json())


if __name__ == '__main__':
    basic()
