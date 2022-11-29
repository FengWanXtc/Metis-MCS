import argparse
import sys
sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *


def main(Host, TCam, SCam):
    # 设置对应的MCS
    Data = read_json_file('Far_Push.json')
    # CAM1、CAM2、CAM_IN 的 DeviceId基本已定,需修改的是IPC

    Teacher_DeviceId = get_DeviceId_by_aiStrategy(ip=Host, camType=TCam, aiStrategy='teacher')
    Data['VideoSpecs'][0]['DeviceId'] = Teacher_DeviceId
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=Host, camType=SCam, aiStrategy='student')
    Data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    # print(json.dumps(S4E3_data, indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=Data)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('S4E1 Far End Test Pass!')
    else:
        print('S4E1 Far End Test Fail!')
        print(response.json())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default=Global_FarEnd, help='The IP address of the METIS')
    parser.add_argument('-TCam', type=str, default=Global_TeacherCamType, help='The Teacher Cam Type')
    parser.add_argument('-SCam', type=str, default=Global_StudentCamType, help='The Student Cam Type')
    args = parser.parse_args()
    IP = args.ip
    SCAM = args.SCam
    TCAM = args.TCam
    main(IP, TCAM, SCAM)

