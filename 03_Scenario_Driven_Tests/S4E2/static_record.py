import sys
import argparse
sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from mediadevicelib import *
from functionlib import *


def static_record(IP):
    static_re_data = read_json_file('static_record.json')

    VideoIns = get_md_video_in(ip=IP).json()['VideoIns']
    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find(Global_GeneralCamType_other) != -1:
            DeviceId = VideoIn['DeviceId']
            static_re_data['VideoSpecs'][0]['DeviceId'] = DeviceId
            break

    try:
        response = post_mt_create_update(ip=IP, data=static_re_data)

    except:
        print("Create one frame task Failed!")
        print(response.json())

    if response.json()['Code'] == 201:
        print('Create static record task Success!')
    else:
        print('Create static record task  Failed!')
        print(response.json())


def main():
    parser = argparse.ArgumentParser(description='usage: python3 static_record.py -ip=XXX')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip
    static_record(IP)


if __name__ == '__main__':
    main()
