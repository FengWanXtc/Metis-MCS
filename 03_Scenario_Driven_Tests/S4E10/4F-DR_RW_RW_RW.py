import argparse
import sys
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def S4E3_Basic():
    # 设置对应的MCS
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip

    S4E3_data = read_json_file('4F-DR_RW_RW_RW.json')
    # CAM1、CAM2、CAM_IN 的 DeviceId基本已定,需修改的是IPC
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType='IPC', aiStrategy='student')
    S4E3_data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    Blackboard_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType='IPC', aiStrategy='blackboard')
    S4E3_data['VideoSpecs'][3]['DeviceId'] = Blackboard_DeviceId
    # print(json.dumps(S4E3_data, indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=S4E3_data)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('S4E10 Basic Test Pass!')
    else:
        print('S4E10 Basic Test Fail!')
        print(response.json())


if __name__ == '__main__':
    S4E3_Basic()
