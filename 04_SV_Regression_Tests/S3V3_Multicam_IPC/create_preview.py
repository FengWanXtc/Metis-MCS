import json
import sys
import argparse

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *
from environmentlib import *
from mediadevicelib import *

def create_preview(IP, device, mcsname, name, position):
    cre_data = read_json_file('create_preview.json')
    cre_data["VideoSpecs"][0]["Name"] = cre_data["RenderSpecs"][0]["CompositionSpec"][0]["SourceName"] = name
    VideoIns = get_md_video_in(ip=IP).json()['VideoIns']

    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find(device) != -1:
            cre_data['VideoSpecs'][0]['DeviceId'] = VideoIn['DeviceId']
            break

    if mcsname.find("IPC") != -1 or mcsname.find("USB") != -1:
        cre_data["VideoSpecs"][0]['Format'] = "YUY2"
    else:
        cre_data["VideoSpecs"][0]['Format'] = "UYVY"

    cre_data["Name"] = mcsname
    if position == '1':
        cre_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [0, 0, 960, 540]
    elif position == '2':
        cre_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [960, 0, 960, 540]
    elif position == '3':
        cre_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [0, 540, 960, 540]
    else:
        cre_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [960, 540, 960, 540]

    # print(json.dumps(cre_data,indent=2))
    try:
        response = post_mt_create_update(ip=IP, data=cre_data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if response.json()['Code'] == 201:
        print('Create one frame preview {} Success'.format(name))
        return True
    else:
        print('Create one frame preview {} Fail'.format(name))
        print(response.json())
        return False


def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 create_one_frame_preview.py --name=Teacher --frame_number=1')
    parser.add_argument('--device', '-d', type=str, default='HDMI', help='The camera of the port,default is 0')
    parser.add_argument('--mcsname', '-mn', type=str, default='MCS', help='The name of the mcstask')
    parser.add_argument('--name', '-n', type=str, default='Teacher', help='The name of the frame,default is Teacher')
    parser.add_argument('--position', '-p', type=str, default='1', help='The position of the frame,default is 1')
    parser.add_argument('-ip', type=str, default='10.12.224.140', help='The IP Address')

    args = parser.parse_args()
    IP = args.ip
    DEVICE = args.device
    MCSNAME = args.mcsname
    NAME = args.name
    POSITION = args.position

    create_preview(IP, DEVICE, MCSNAME, NAME, POSITION)


if __name__ == '__main__':
    main()
