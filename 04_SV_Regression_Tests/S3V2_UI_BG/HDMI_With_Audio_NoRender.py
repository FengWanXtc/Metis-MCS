import sys
import argparse
sys.path.append('../../Libraries')
from functionlib import *
from mediadevicelib import *
from mediatasklib import *
from environmentlib import *


def audio_push(IP):
    data = read_json_file('HDMI_With_Audio_NoRender.json')
    VideoIns = get_md_video_in(ip=IP).json()['VideoIns']

    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find(Global_GeneralCamType) != -1:
            data['VideoSpecs'][0]['DeviceId'] = VideoIn['DeviceId']
            break

    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(TaskId)
    except:
        print('Audio And HDMI Push Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Audio And HDMI Task Success')
        return True
    else:
        print('Audio And HDMI Task Fail')


def main():
    parser = argparse.ArgumentParser(description='usage: python3 XXXXX.py --ip=XXXXX')
    parser.add_argument('-ip', type=str, default='', help='The ip of the station.')
    args = parser.parse_args()
    IP = args.ip
    audio_push(IP)


if __name__ == '__main__':
    main()
