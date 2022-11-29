import argparse
import sys
sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *

TeacherCamType = Global_TeacherCamType
StudentCamType = Global_StudentCamType


def S1E1_Test():
    # 设置对应的MCS
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-TCam', type=str, default=TeacherCamType, help='The Teacher Cam Type')
    parser.add_argument('-SCam', type=str, default=StudentCamType, help='The Student Cam Type')
    parser.add_argument('-logfile', type=str, default=None, help='LogFile Name')

    args = parser.parse_args()
    IP = args.ip
    SCAM = args.SCam
    TCAM = args.TCam
    LOGFILE = args.logfile

    if LOGFILE is not None:
        # 此步骤是设置LogFile
        environmentlib.Whether_Log_File = True
        environmentlib.modify_cfg("FileName", LOGFILE)

    S1E1_data = read_json_file('11.2.1_4F.json')

    Teacher_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=TCAM, aiStrategy='teacher')
    S1E1_data['VideoSpecs'][0]['DeviceId'] = Teacher_DeviceId
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=SCAM, aiStrategy='student')
    S1E1_data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    # print(json.dumps(S1E1_data, indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=S1E1_data)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('S1E1 Teacher Test Pass!')
    else:
        print('S1E1 Teacher Test Fail!')
        print(json.dumps(S1E1_data, indent=2))
        print(response.json())


if __name__ == '__main__':
    S1E1_Test()
