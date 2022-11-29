import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def create_preview(IP, mcsname, cameraType, cameraNumber):
    cre_data = read_json_file('remote_push_pull_audio_out.json')
    cameraList = read_json_file("cameraList.json")
    cre_data["Name"] = mcsname
    if cameraType == 'HDMI':
        cre_data['VideoSpecs'][0]['Format'] = 'UYVY'
    else:
        cre_data['VideoSpecs'][0]['Format'] = 'YUY2'

    cre_data['VideoSpecs'][0]['DeviceId'] = cameraList[cameraType][cameraNumber]
    # print(cre_data)
    try:
        response = post_mt_create_update(ip=IP, data=cre_data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Create remote push task Success')
        return True
    else:
        print('Create remote push task Fail')
        return False


def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 create_one_frame_preview.py --name=Teacher --frame_number=1')
    parser.add_argument('--mcsname', '-mn', type=str, default='RemotePush', help='The name of the MCS')
    parser.add_argument('--cameranumber', '-cn', type=str, default='1', help='The camera number')
    parser.add_argument('--cameratype', '-ct', type=str, default='HDMI', help='The camera type HDMI,USB,IPC')
    parser.add_argument('-ip', type=str, default='', help='The ip of the station.')
    args = parser.parse_args()
    IP = args.ip
    CAMERANUMBER = args.cameranumber
    MCSNAME = args.mcsname
    CAMERATYPE = args.cameratype
    create_preview(IP, MCSNAME, CAMERATYPE, CAMERANUMBER)


if __name__ == '__main__':
    main()
