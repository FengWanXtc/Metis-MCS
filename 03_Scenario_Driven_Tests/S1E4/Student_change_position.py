import sys
import argparse

sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *

TeacherCamType = Global_TeacherCamType
StudentCamType = Global_StudentCamType


def stu_change_position(IP, SCAM):
    Student_data = read_json_file('Student-4F-4.1DR-4.2R1A-4.3S-4.4R.json')
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=SCAM, aiStrategy='student')
    Student_data['VideoSpecs'][0]['DeviceId'] = Student_DeviceId
    Student_data["RenderSpecs"][0]['CompositionSpec'][0]['SourceName'] = 'Student'
    Student_data["RenderSpecs"][0]['CompositionSpec'][1]['SourceName'] = 'CodecStreamSpec_pull'
    Student_data["RenderSpecs"][0]['CompositionSpec'][2]['SourceName'] = 'Director'
    Student_data["RenderSpecs"][0]['CompositionSpec'][3]['SourceName'] = 'Director_pull'

    response = post_mt_create_update(ip=IP, data=Student_data)
    # print(json.dumps(Student_data, indent=2))

    if response.json()['Code'] == 201:
        print('Change Student Position Test Pass!')
    else:
        print('Change Student Position Test Fail!')
        print(response.json())
        return response.json()


def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 Student-4F-4.1DR-4.2R1A-4.3S-4.4R.py -ip=XXXX')
    # 指定哪个HDMI口
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-SCam', type=str, default=StudentCamType, help='The Student Cam Type')
    args = parser.parse_args()
    IP = args.ip
    SCAM = args.SCam
    stu_change_position(IP, SCAM)


if __name__ == '__main__':
    main()
    # TaskId = get_TaskId_by_action_name("S2P1_basic")
