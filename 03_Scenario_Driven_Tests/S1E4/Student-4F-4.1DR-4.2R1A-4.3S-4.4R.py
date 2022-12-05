import sys
import argparse

sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *

TeacherCamType = Global_TeacherCamType
StudentCamType = Global_StudentCamType

def S1E4_Student(IP, SCAM):
    Student_data = read_json_file('Student-4F-4.1DR-4.2R1A-4.3S-4.4R.json')
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=SCAM, aiStrategy='student')
    Student_data['VideoSpecs'][0]['DeviceId'] = Student_DeviceId
    response = post_mt_create_update(ip=IP, data=Student_data)
    # print(json.dumps(Student_data, indent=2))

    if response.json()['Code'] == 201:
        print('S1E4 Student-End Test Pass!')
    else:
        print('S1E4 Student-End Test Fail!')
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
    S1E4_Student(IP, SCAM)


if __name__ == '__main__':
    main()
