import sys
import argparse

sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *

TeacherCamType = Global_TeacherCamType
StudentCamType = Global_StudentCamType


def main():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-rtsp', type=str, default="rtsp://10.12.224.57/ch2", help='IPC camera as CodecStream Source.')
    args = parser.parse_args()
    IP = args.ip
    RTSP = args.rtsp
    # 移除Rtc拉流
    data = {
        "Name": "Basic_MCS",
        "SpecNames": ["Student_Pull"]
    }
    response = post_mt_remove(ip=IP, data=data)

    if response.json()['Code'] == 200:
        print('Remove MCS ({}) SpecName ({}) Success'.format("Basic_MCS", "Student_Pull"))
        return True
    else:
        print('Remove MCS ({}) SpecName ({}) Fail'.format("Basic_MCS", "Student_Pull"))
        print(response.json())
    # time.sleep(3)

    MCS_data = read_json_file('11.2.4_IPC_replace.json')
    MCS_data['CodecStreamSpecs'][0]['URI'] = RTSP
    # print(json.dumps(S1E2_data, indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=MCS_data)
    except RuntimeError:
        print('Post Create Task Failed')
        print(response.status_code)
        return False

    if response.json()['Code'] == 201:
        print('S2V1 Case 4:Add IPC Stream Test Success')
        return True
    else:
        print('S2V1 Case 4:Add IPC Stream Test Fail')
        print(response.json())
        return False


if __name__ == '__main__':
    main()
