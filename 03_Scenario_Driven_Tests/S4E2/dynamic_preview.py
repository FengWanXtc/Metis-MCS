import sys
import argparse

sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *
from mediadevicelib import *


def dynamic_preview(IP):
    dynamic_re_data = read_json_file('dynamic_preview.json')
    VideoIns = get_md_video_in(ip=IP).json()['VideoIns']
    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find(Global_GeneralCamType) != -1:
            DeviceId = VideoIn['DeviceId']
            dynamic_re_data['VideoSpecs'][0]['DeviceId'] = DeviceId
            break

    try:
        response = post_mt_create_update(ip=IP, data=dynamic_re_data)
    except:
        print("Create one frame task Failed!")
        print(response.json())

    if response.json()['Code'] == 201:
        print('Create dynamic record task Success!')
    else:
        print('Create dynamic record task Failed!')


def main():
    parser = argparse.ArgumentParser(description='usage: python3 dynamic_record.py')
    parser.add_argument('-ip', type=str, default='', help='The Host IP')
    args = parser.parse_args()
    IP = args.ip
    dynamic_preview(IP)


if __name__ == '__main__':
    main()
