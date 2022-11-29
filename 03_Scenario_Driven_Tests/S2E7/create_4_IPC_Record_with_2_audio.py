import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *
from mediadevicelib import *


def create_4_IPC_record(IP):
    cre_4_IPC_re_data = read_json_file('create_4_IPC_Record_with_2_audio.json')
    VideoIns = get_md_video_in(ip=IP).json()["VideoIns"]
    DeviceIdList = []
    for VideoIn in VideoIns:
        if VideoIn['DeviceName'].find("IPC") != -1:
            DeviceIdList.append(VideoIn['DeviceId'])

    for i in range(4):
        cre_4_IPC_re_data['VideoSpecs'][i]['DeviceId'] = DeviceIdList[i]
    # print(json.dumps(cre_4_IPC_re_data['VideoSpecs'], indent=2))
    # print(cre_4_IPC_re_data["VideoSpecs"])

    try:
        response = post_mt_create_update(ip=IP, data=cre_4_IPC_re_data)
        # print(response.json())
    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('Create 4 IPC With 2 Audio Record Success!')
    else:
        print('Create 4 IPC With 2 Audio Record Failed!')
        print(json.dumps(response.json(), indent=2))


def main():
    parser = argparse.ArgumentParser(description='usage: python3 crete_IPC.py  -ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The ip of Metis Station to push rtsp stream')
    args = parser.parse_args()
    IP = args.ip  # 指定推流小站的IP
    create_4_IPC_record(IP)


if __name__ == '__main__':
    main()
