import argparse
import sys

sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *

TeacherCamType = Global_TeacherCamType
StudentCamType = Global_StudentCamType

def S1E5_Main():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-TCam', type=str, default=TeacherCamType, help='The Teacher Cam Type')
    parser.add_argument('-SCam', type=str, default=StudentCamType, help='The Student Cam Type')
    args = parser.parse_args()
    IP = args.ip
    SCAM = args.SCam
    TCAM = args.TCam

    S1E5_data = read_json_file('4F-4.1D1PAR-4.2T-4.3S.json')
    Teacher_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=TCAM, aiStrategy='teacher')
    S1E5_data['VideoSpecs'][0]['DeviceId'] = Teacher_DeviceId
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=SCAM, aiStrategy='student')
    S1E5_data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    # print(json.dumps(S1E5_data, indent=2))
    try:
        response = post_mt_create_update(ip=IP, data=S1E5_data)
        # print(TaskId)

    except:
        print('Post Create Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('S1E5 Action (Create 3 Frames) Test Pass!')
        return True
    else:
        print('S1E5 Action (Create 3 Frames) Test Fail!')
        print(response.json())
        return response.json()


if __name__ == '__main__':
    S1E5_Main()
