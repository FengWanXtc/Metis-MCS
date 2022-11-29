import json
import sys
import argparse
sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *
from mediadevicelib import *


def create_remote(IP):
    cre_rem_data = read_json_file('remote_push.json')
    VideoIns = get_md_video_in(ip=IP).json()['VideoIns']
    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find(Global_GeneralCamType) != -1:
            Student_DeviceId = VideoIn['DeviceId']
            break
    if Global_GeneralCamType != 'HDMI':
        cre_rem_data["VideoSpecs"][0]["Format"] = 'YUY2'
    else:
        cre_rem_data["VideoSpecs"][0]["Format"] = 'UYVY'

    cre_rem_data['VideoSpecs'][0]['DeviceId'] = Student_DeviceId
    print(json.dumps(cre_rem_data,indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=cre_rem_data)
    except:
        print('Post Create Task Failed.')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('S1E1 Student Test Pass!')
    else:
        print('S1E1 Student Test Fail!')


def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 student_create_remote.py -ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The ip of the host pc which push camera stream')
    args = parser.parse_args()
    IP = args.ip
    create_remote(IP)


if __name__ == '__main__':
    main()
