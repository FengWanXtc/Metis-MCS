import argparse
import sys

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def main():
    parser = argparse.ArgumentParser(description='usage: python3 XXXX --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-mcsname', '-mn', type=str, required=True, help='The MCS Name')
    parser.add_argument('-target', '-t', required=True, help='The Target Metis to push Stream')
    args = parser.parse_args()
    IP = args.ip
    TARGET = args.target
    MCSNAME = args.mcsname
    # 设置对应的MCS
    data = read_json_file('V_A_Server.json')
    data['Name'] = MCSNAME
    data["ServerSpecs"][0]["URI"] = "wp://{}:6673".format(TARGET)
    data["ServerSpecs"][1]["URI"] = "wp://{}:6676".format(TARGET)
    # CAM1、CAM2、CAM_IN 的 DeviceId基本已定,需修改的是IPC
    # print(json.dumps(data,indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.url)

    except:
        print('Far End 1 Audio and Video Push Failed.')
        print(response.status_code)
    # print(response.status_code)

    if response.json()['Code'] == 201:
        print('Far End 1 Audio and Video Push Pass!')
    else:
        print('Far End 1 Audio and Video Push Fail!')
        print(response.json())


if __name__ == '__main__':
    main()
