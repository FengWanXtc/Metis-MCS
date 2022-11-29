import argparse
import json
import sys

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def main():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-mcsname', '-mn', type=str, required=True, help='The MCS Name')
    args = parser.parse_args()
    IP = args.ip
    MCSNAME = args.mcsname
    # 设置对应的MCS
    data = read_json_file('RTMP_Pull.json')
    data['Name'] = MCSNAME
    data["CodecStreamSpecs"][0]["URI"] = "rtmp://{}/metis/test".format(IP)
    # CAM1、CAM2、CAM_IN 的 DeviceId基本已定,需修改的是IPC
    # print(json.dumps(data,indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.url)

    except:
        print('Compose Stream RTMP Pull Failed.')
        print(response.status_code)
    # print(response.status_code)

    if response.json()['Code'] == 201 or response.json()['Code'] == 202:
        print('Compose Stream RTMP Pull Pass!')
    else:
        print('Compose Stream RTMP Pull Fail!')
        print(response.json())


if __name__ == '__main__':
    main()
