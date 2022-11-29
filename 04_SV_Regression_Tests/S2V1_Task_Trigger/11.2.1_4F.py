import argparse
import sys

sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *

TeacherCamType = Global_TeacherCamType
StudentCamType = Global_StudentCamType


def S1E2_test():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-TCam', type=str, default=TeacherCamType, help='The Teacher Cam Type')
    parser.add_argument('-SCam', type=str, default=StudentCamType, help='The Student Cam Type')

    args = parser.parse_args()
    IP = args.ip
    SCAM = args.SCam
    TCAM = args.TCam

    MCS_data = read_json_file('11.2.1_4F.json')
    # print(json.dumps(S1E2_data, indent=2))
    Teacher_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=TCAM, aiStrategy='teacher')
    MCS_data['VideoSpecs'][0]['DeviceId'] = Teacher_DeviceId
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=SCAM, aiStrategy='student')
    MCS_data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    Blackboard_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType="IPC", aiStrategy='blackboard')
    MCS_data['VideoSpecs'][2]['DeviceId'] = Blackboard_DeviceId

    try:
        response = post_mt_create_update(ip=IP, data=MCS_data)
    except:
        print('Post Create Task Failed')
        print(response.status_code)
        return False

    if response.json()['Code'] == 201:
        print('S2V1 Case 1 Test Success')
        return True
    else:
        print('S2V1 Case 1 Test Fail')
        print(response.json())
        return False


if __name__ == '__main__':
    S1E2_test()
