import argparse
import sys
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def basic():
    # 设置对应的MCS
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('--target', '-t', type=str, default='', help='The Target Address of Far End Metis')
    parser.add_argument('--width', '-w', type=int, default=720, help='The Width of Transform Frame')
    parser.add_argument('--height', '--h', type=int, default=480, help='The Height  of Transform Frame')

    args = parser.parse_args()
    IP = args.ip
    WIDTH = args.width
    HEIGHT = args.height
    TARGET = args.target

    data = read_json_file('Transform.json')
    # 设定宽高
    data["VideoTransformSpecs"][0]["Width"] = WIDTH
    data["VideoTransformSpecs"][0]["Height"] = HEIGHT
    data['ServerSpecs'][0]['URI'] = "tcp://{}:6671".format(TARGET)

    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('TransformBasic Test Pass!')
    else:
        print('TransformBasic Test Fail!')
        print(response.json())


if __name__ == '__main__':
    basic()
