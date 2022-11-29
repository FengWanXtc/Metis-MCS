import argparse
import json
import sys

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def main():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-target', '-t', required=True, help='The Target Metis to push Stream')
    parser.add_argument('-TCam', type=str, default='HDMI', help='The Teacher Cam Type')
    parser.add_argument('-SCam', type=str, default='IPC', help='The Student Cam Type')
    args = parser.parse_args()
    IP = args.ip
    TCAM = args.TCam
    SCAM = args.SCam
    # 设置对应的MCS
    data = read_json_file('Director_push.json')

    Teacher_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=TCAM, aiStrategy='teacher')
    data['VideoSpecs'][0]['DeviceId'] = Teacher_DeviceId
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=SCAM, aiStrategy='student')
    data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    # CAM1、CAM2、CAM_IN 的 DeviceId基本已定,需修改的是IPC
    # print(json.dumps(data,indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('Director Push Test Pass!')
    else:
        print('Director Push Test Fail!')
        print(response.json())


if __name__ == '__main__':
    main()
