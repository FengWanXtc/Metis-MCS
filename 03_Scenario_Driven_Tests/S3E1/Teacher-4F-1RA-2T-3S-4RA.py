import argparse
import sys
sys.path.append('../../Libraries')
from environmentlib import *
from functionlib import *
from mediatasklib import *
from mediadevicelib import *


def S3E1_Teacher(Host, TCam, SCam):
    S3E1_data = read_json_file('Teacher-4F-1RA-2T-3S-4RA.json')
    AudioIns = get_md_audio_in(ip=Host).json()['AudioIns']

    Teacher_DeviceId = get_DeviceId_by_aiStrategy(ip=Host, camType=TCam, aiStrategy='teacher')
    S3E1_data['VideoSpecs'][0]['DeviceId'] = Teacher_DeviceId
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=Host, camType=SCam, aiStrategy='student')
    S3E1_data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId

    for AudioIn in AudioIns:
        if AudioIn['DeviceName'].find("BuiltIn USB Audio Capture") != -1:
            AudioDeviceId = AudioIn['DeviceId']
    S3E1_data['AudioSpecs'][0]['DeviceId'] = AudioDeviceId
    # print(json.dumps(S3E1_data, indent=2))

    print(json.dumps(S3E1_data, indent=2))

    try:
        response = post_mt_create_update(ip=Host, data=S3E1_data)
    except:
        print('Post Create Task Failed')
        print(response.status_code)
        return False

    if response.json()['Code'] == 201:
        print('S3E1 Teacher Test Success')
        return True
    else:
        print('S3E1 Teacher Test Fail')
        print(response.json())
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-TCam', type=str, default=Global_TeacherCamType, help='The Teacher Cam Type')
    parser.add_argument('-SCam', type=str, default=Global_StudentCamType, help='The Student Cam Type')
    args = parser.parse_args()
    IP = args.ip
    SCAM = args.SCam
    TCAM = args.TCam

    S3E1_Teacher(IP, TCAM, SCAM)
