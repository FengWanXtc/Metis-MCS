import argparse
import sys
sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *


def director():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip

    databody = read_json_file('AI_1.json')
    # databody = read_json_file('AI.json')
    databody["VideoSpecs"][0]['DeviceId'] = get_DeviceId_by_aiStrategy(ip=IP, camType=Global_TeacherCamType, aiStrategy='teacher')
    databody["VideoSpecs"][1]['DeviceId'] = get_DeviceId_by_aiStrategy(ip=IP, camType=Global_StudentCamType, aiStrategy='student')

    try:
        response = post_mt_create_update(ip=IP, data=databody)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('AI_1 Test Pass!')
    else:
        print('AI_1 Test Fail!')
        print(response.json())


def main():

    director()


if __name__ == '__main__':
    main()
