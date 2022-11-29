import argparse
import sys
sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *
from mediadevicelib import get_md_audio_in


def Basic(Host, TCam, SCam, BCam):
    # 设置对应的MCS
    AudioIns = get_md_audio_in(ip=Host).json()['AudioIns']
    Data = read_json_file('Basic.json')

    Teacher_DeviceId = get_DeviceId_by_aiStrategy(ip=Host, camType=TCam, aiStrategy='teacher')
    Data['VideoSpecs'][0]['DeviceId'] = Teacher_DeviceId
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=Host, camType=SCam, aiStrategy='student')
    Data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    Blackboard_DeviceId = get_DeviceId_by_aiStrategy(ip=Host, camType=BCam, aiStrategy='blackboard')
    Data['VideoSpecs'][3]['DeviceId'] = Blackboard_DeviceId

    for AudioIn in AudioIns:
        if AudioIn['DeviceName'].find("BuiltIn USB Audio Capture") != -1:
            AudioDeviceId = AudioIn['DeviceId']
            Data['AudioSpecs'][0]['DeviceId'] = AudioDeviceId

    try:
        response = post_mt_create_update(ip=IP, data=Data)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('S4E1 Basic Test Pass!')
    else:
        print('S4E1 Basic Test Fail!')
        print(response.json())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default=Global_NearEnd, help='The IP address of the METIS')
    parser.add_argument('-TCam', type=str, default=Global_TeacherCamType, help='The Teacher Cam Type')
    parser.add_argument('-SCam', type=str, default=Global_StudentCamType, help='The Student Cam Type')
    parser.add_argument('-BCam', type=str, default=Global_BlackBoardCamType, help='The Blackboard Cam Type')
    args = parser.parse_args()
    IP = args.ip
    SCAM = args.SCam
    TCAM = args.TCam
    BCAM = args.BCam

    Basic(IP, TCAM, SCAM, BCAM)
