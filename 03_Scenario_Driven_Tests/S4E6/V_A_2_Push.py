import argparse
import json
import sys

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def main():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-target', '-t', required=True, help='The Target Metis to push Stream')
    args = parser.parse_args()
    IP = args.ip
    TARGET = args.target
    # 设置对应的MCS
    # 由于小站资源有限，只能先推另外两路摄像头流
    data = read_json_file('V_A_2_Push.json')
    data["ServerSpecs"][0]["URI"] = "wp://{}:6675".format(TARGET)
    data["ServerSpecs"][1]["URI"] = "wp://{}:6676".format(TARGET)
    data["ServerSpecs"][2]["URI"] = "wp://{}:6677".format(TARGET)
    data["ServerSpecs"][3]["URI"] = "wp://{}:6678".format(TARGET)

    # print(json.dumps(data,indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('Director Push Test Pass!')
    else:
        print('Director Push Test Fail!')
        print(response.json())


if __name__ == '__main__':
    main()
