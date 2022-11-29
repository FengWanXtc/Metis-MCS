import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *
from mediadevicelib import *
from environmentlib import *


def create_preview(IP, IDENTITY):
    # 读取MCS
    cre_data = read_json_file('2F-2.1TSPA-2.2RA.json')
    # print(json.dumps(cre_data, indent=2))
    # 根据video in 接口获取第一个摄像头的DeviceId
    VideoIns = get_md_video_in(ip=IP).json()['VideoIns']
    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find(Global_GeneralCamType) != -1:
            DeviceId = VideoIn['DeviceId']
            break

    cre_data['VideoSpecs'][0]['DeviceId'] = DeviceId
    cre_data['RtcStreamSpec']['Identity'] = IDENTITY
    # print(json.dumps(cre_data, indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=cre_data)

    except:
        print('Post Create Task Failed')
        print(response)
        print(response.json())

    if response.json()['Code'] == 201:
        print('Create one frame Push and Pull Task Success')
        return True
    else:
        print('Create one frame Push and Pull Task Fail')
        print(response.json())
        return False


def main():
    parser = argparse.ArgumentParser(
        description='usage: python 2F-2.1TSPA-2.2RA.py -ip=10.12.224.XXX')
    parser.add_argument('-ip', type=str, default='', help='The IP of the Metis Station.Default is Present')
    parser.add_argument('--identity', '-i', type=str, default='Student_1', help='The Identity,default is Student_1')

    args = parser.parse_args()
    IP = args.ip
    IDENTITY = args.identity

    create_preview(IP, IDENTITY)


if __name__ == '__main__':
    main()
