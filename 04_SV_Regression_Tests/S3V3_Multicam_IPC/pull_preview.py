import json
import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *

positionDict = {
    "1": [0, 0, 960, 540],
    "2": [960, 0, 960, 540],
    "3": [0, 540, 960, 540],
    "4": [960, 540, 960, 540]
}


def pull_preview(IP, position):
    data = read_json_file('pull_preview.json')
    data['RenderSpecs'][0]['CompositionSpec'][0]['Geometry'] = positionDict[position]
    # print(json.dumps(tea_re_data, indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if response.json()['Code'] == 201:
        print('Create Pull And Preview Success')
        return True
    else:
        print('Create Pull And Preview Fail')
        return False


def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 XXXX.py -iP=XXX -p=1')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('--position', '-p', type=str, default='1', help='The position of the frame,default is 1')

    args = parser.parse_args()
    IP = args.ip
    POSITION = args.position
    pull_preview(IP, POSITION)


if __name__ == '__main__':
    main()
