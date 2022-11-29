import argparse
import os
import sys
import time

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *
from environmentlib import *

def push(IP):
    databody = read_json_file('AI_2_push.json')
    databody['VideoSpecs'][0]["DeviceId"] = get_DeviceId_by_aiStrategy(ip=IP, camType=Global_TeacherCamType, aiStrategy='teacher')
    databody['VideoSpecs'][1]['DeviceId'] = get_DeviceId_by_aiStrategy(ip=IP, camType=Global_StudentCamType, aiStrategy='student')

    try:
        response = post_mt_create_update(ip=IP, data=databody)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('AI_2 Push Test Pass!')
    else:
        print('AI_2 Push Test Fail!')
        print(response.json())


def remote(IP):
    databody = read_json_file('AI_2_remote.json')
    try:
        response = post_mt_create_update(ip=IP, data=databody)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('AI_2 Pull Test Pass!')
    else:
        print('AI_2 Pull Test Fail!')
        print(response.json())


def audio_push(IP):
    databody = read_json_file('AI_3_push.json')
    databody['VideoSpecs'][0]["DeviceId"] = get_DeviceId_by_aiStrategy(ip=IP, camType='HDMI', aiStrategy='teacher')
    databody['VideoSpecs'][1]['DeviceId'] = get_DeviceId_by_aiStrategy(ip=IP, camType='USB', aiStrategy='student')

    try:
        response = post_mt_create_update(ip=IP, data=databody)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('AI_3 Push With Audio Test Pass!')
    else:
        print('AI_3 Push With Audio Test Fail!')
        print(response.json())


def main():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip

    push(IP)  # 远端推流
    time.sleep(2)
    remote(IP)  # 近端拉流
    time.sleep(3)
    print("Delete Task 1")
    os.system("python delete_task_by_name.py -n=AI_2_Push")
    time.sleep(5)
    audio_push(IP)


if __name__ == '__main__':
    main()
