import json
import sys
import argparse

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def create_preview(IP, device, mcsname, name, position):
    cre_data = read_json_file('create_preview_with_audio.json')
    cre_data["VideoSpecs"][0]["Name"] = cre_data["RenderSpecs"][0]["CompositionSpec"][0]["SourceName"] = name
    cre_data['VideoCodecSpecs'][0]['SourceName'] = name
    DeviceId = get_DeviceId_by_devicePath("video{}".format(device))
    cre_data["VideoSpecs"][0]["DeviceId"] = DeviceId
    cre_data["Name"] = mcsname
    if mcsname.find("HDMI") != -1:
        cre_data["VideoSpecs"][0]['Format'] = "UYVY"
    else:
        cre_data["VideoSpecs"][0]['Format'] = "YUY2"

    if position == '1':
        cre_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [0, 0, 960, 540]
    elif position == '2':
        cre_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [960, 0, 960, 540]
    elif position == '3':
        cre_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [0, 540, 960, 540]
    else:
        cre_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [960, 540, 960, 540]
    try:
        response = post_mt_create_update(ip=IP, data=cre_data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if response.json()['Code'] == 201:
        print('Create one frame preview {} With Audio Success'.format(name))
        return True
    else:
        print('Create one frame preview {} With Audio Fail'.format(name))
        print(response.json())
        # print(json.dumps(cre_data, indent=2))
        return False


def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 create_one_frame_preview.py --name=Teacher --frame_number=1')
    parser.add_argument('--device', '-d', type=str, default='0', help='The camera of the port,default is 0')
    parser.add_argument('--mcsname', '-mn', type=str, default='mcs0.3', help='The name of the mcstask')
    parser.add_argument('--name', '-n', type=str, default='Teacher', help='The name of the frame,default is Teacher')
    parser.add_argument('--position', '-p', type=str, default='1', help='The position of the frame,default is 1')
    parser.add_argument('-ip', type=str, default='', help='The IP Address')

    args = parser.parse_args()
    IP = args.ip
    args = parser.parse_args()
    DEVICE = args.device
    MCSNAME = args.mcsname
    NAME = args.name
    POSITION = args.position

    create_preview(IP, DEVICE, MCSNAME, NAME, POSITION)


if __name__ == '__main__':
    main()
