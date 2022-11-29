import argparse
import sys
sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *


def main():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-target', '-t', required=True, help='The Target Metis to push Stream')
    args = parser.parse_args()
    IP = args.ip
    TARGET = args.target
    # 设置对应的MCS
    data = read_json_file('Director_push.json')
    Teacher_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=Global_TeacherCamType, aiStrategy='teacher')
    data['VideoSpecs'][0]['DeviceId'] = Teacher_DeviceId
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=Global_StudentCamType, aiStrategy='student')
    data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    data["ServerSpecs"][0]["URI"] = "wp://{}:6671".format(TARGET)
    data["ServerSpecs"][1]["URI"] = "wp://{}:6672".format(TARGET)
    # CAM1、CAM2、CAM_IN 的 DeviceId基本已定,需修改的是IPC
    # print(json.dumps(data,indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response.status_code)
    # print(response.status_code)

    if response.json()['Code'] == 201:
        print('Director Push Test Pass!')
    else:
        print('Director Push Test Fail!')
        print(response.json())


if __name__ == '__main__':
    main()
