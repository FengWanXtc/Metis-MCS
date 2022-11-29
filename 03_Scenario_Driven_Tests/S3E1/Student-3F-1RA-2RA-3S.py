import sys
import argparse
sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *
from mediadevicelib import *


def student_create_frame(IP, IDENTITY, Scam):
    stu_cr_data = read_json_file('Student-3F-1RA-2RA-3S.json')
    stu_cr_data['RtcStreamSpec']['Identity'] = IDENTITY
    # print(json.dumps(stu_cr_data, indent=2))
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=Scam, aiStrategy='student')
    stu_cr_data['VideoSpecs'][0]['DeviceId'] = Student_DeviceId
    
    AudioIns = get_md_audio_in(ip=IP).json()['AudioIns']
    for AudioIn in AudioIns:
        # Builtin USB Audio Playback
        if AudioIn['DeviceName'].find("BuiltIn USB Audio Capture") != -1:
            AudioDeviceId = AudioIn['DeviceId']
    stu_cr_data['AudioSpecs'][0]['DeviceId'] = AudioDeviceId
    print(json.dumps(stu_cr_data, indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=stu_cr_data)
    except:
        print("POST Student-End Task Fail!")
        print(response.json())

    if response.json()['Code'] == 201:
        print('S3E1 Student-End Test Pass!')
    else:
        print(response.json())
        print('S3E1 Student-End Test Fail!')


def main():
    parser = argparse.ArgumentParser(description='usage: python3 StudentXXXXXX.py -ip=10.12.224.XX')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('--identity', '-i', type=str, default='Student_1', help='The Identity,default is Student_1')
    parser.add_argument('-SCam', type=str, default=Global_StudentCamType, help='The Student Cam Type')

    args = parser.parse_args()
    IP = args.ip
    IDENTITY = args.identity
    SCAM = args.SCam
    student_create_frame(IP, IDENTITY, SCAM)


if __name__ == '__main__':
    main()
