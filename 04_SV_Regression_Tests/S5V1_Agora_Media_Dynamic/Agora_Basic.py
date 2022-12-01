import argparse
import sys

sys.path.append('../../Libraries')
from environmentlib import *
from functionlib import *
from mediatasklib import *
from mediadevicelib import *


def mcs_task(host_ip, tea_camera, stu_camera):
    mcs_data = read_json_file('Agora_Basic.json')

    # 设置视频源DeviceId
    Teacher_DeviceId = get_DeviceId_by_aiStrategy(ip=host_ip, camType=tea_camera, aiStrategy='teacher')
    mcs_data['VideoSpecs'][0]['DeviceId'] = Teacher_DeviceId
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=host_ip, camType=stu_camera, aiStrategy='student')
    mcs_data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    Blackboard_DeviceId = get_DeviceId_by_aiStrategy(ip=host_ip, camType='IPC', aiStrategy='blackboard')
    mcs_data['VideoSpecs'][3]['DeviceId'] = Blackboard_DeviceId

    # 设置音频输入DeviceId
    AudioIns = get_md_audio_in(ip=host_ip).json()['AudioIns']
    for AudioIn in AudioIns:
        if AudioIn['DeviceName'].find("BuiltIn USB Audio Capture") != -1:
            mcs_data['AudioSpecs'][0]['DeviceId'] = AudioIn['DeviceId']
        if AudioIn['DeviceName'].find("BuiltIn HDMI") != -1:
            mcs_data['AudioSpecs'][1]['DeviceId'] = AudioIn['DeviceId']

    # 设置音频输出DeviceId
    AudioOuts = get_md_audio_out(ip=host_ip).json()['AudioOuts']

    for AudioOut in AudioOuts:
        if AudioOut['DeviceName'].find('BuiltIn USB Audio') != -1:
            mcs_data['PlaySpecs'][0]['DeviceId'] = AudioOut['DeviceId']

    print(json.dumps(mcs_data, indent=2))

    try:
        response = post_mt_create_update(ip=host_ip, data=mcs_data)
    except:
        print('Post Create Task Failed')
        print(response.status_code)
        return False

    if response.json()['Code'] == 201:
        print('Agora Near End Basic Success')
        return True
    else:
        print('Agora Near End Basic Fail')
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

    mcs_task(IP, TCAM, SCAM)
