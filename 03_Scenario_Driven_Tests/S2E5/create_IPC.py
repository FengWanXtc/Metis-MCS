import argparse
import json
import sys

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *
from mediadevicelib import *

geo_list = [[0, 0, 960, 540], [960, 0, 960, 540], [0, 540, 960, 540], [960, 540, 960, 540]]


def cre_4_IPC(IP):
    cre_4_data = read_json_file('create_IPC.json')
    # print(json.dumps(cre_4_data, indent=2))
    VideoIns = get_md_video_in(ip=IP).json()['VideoIns']
    count = 0
    for VideoIn in VideoIns:
        if VideoIn['DeviceName'].find('IPC') != -1:
            if count == 4:
                break
            # 放进循环就是临时变量，放在外面，append是添加地址
            IPC_Spec = {"Name": 'IPC_{}'.format(str(count)), "DeviceId": VideoIn['DeviceId'],
                        "Width": 1920, "Height": 1080, "FrameRate": 30, "Format": "YUY2"}
            cre_4_data['VideoSpecs'].append(IPC_Spec)
            CompositionSpec = {"Geometry": geo_list[count], "SourceName": 'IPC_{}'.format(str(count))}
            cre_4_data['RenderSpecs'][0]['CompositionSpec'].append(CompositionSpec)
            count += 1
    print(json.dumps(cre_4_data, indent=2))
    # print(VideoIns)

    try:
        response = post_mt_create_update(ip=IP, data=cre_4_data)

    except:
        print('Post Create IPC Task Failed')
        print(response.json())

    if response.json()['Code'] == 201:
        print('Create IPC Task Success')
        return True
    else:
        print('Create IPC Task Fail')
        print(response.json())
        return False


def main():
    parser = argparse.ArgumentParser(description='usage: python3 crete_IPC.py  -ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The ip of Metis Station to push rtsp stream')
    args = parser.parse_args()
    IP = args.ip  # 指定推流小站的IP
    cre_4_IPC(IP)


if __name__ == '__main__':
    main()
