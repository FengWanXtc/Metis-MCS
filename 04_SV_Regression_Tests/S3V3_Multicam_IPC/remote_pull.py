import requests
import json
import os
import sys
import argparse

sys.path.append('../../Libraries')

from mediatasklib import *
from functionlib import *


def pull_remote(IP, mcsname, name, position):
    pull_re_data = read_json_file('remote_pull.json')
    # 填写MCS模板内容
    pull_re_data["Name"] = mcsname

    if position == '1':
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [0, 0, 960, 540]
    elif position == '2':
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [960, 0, 960, 540]
    elif position == '3':
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [0, 540, 960, 540]
    else:
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [960, 540, 960, 540]
    try:
        response = post_mt_create_update(ip=IP, data=pull_re_data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Create one frame preview {} Success'.format(name))
        return True
    else:
        print('Create one frame preview {} Fail'.format(name))
        return False


def main():
    parser = argparse.ArgumentParser(description='usage: python3 remote_pull.py --template=four frame')
    parser.add_argument('--ip', '-ip', type=str, default='', help='The ip of the far end station')
    parser.add_argument('--mcsname', '-mn', type=str, default='remote', help='The name of the mcstask')
    parser.add_argument('--name', '-n', type=str, default='remote', help='The name of the frame,default is Teacher')
    parser.add_argument('--position', '-p', type=str, default='1', help='The position of the frame,default is 1')
    args = parser.parse_args()
    IP = args.ip
    MCSNAME = args.mcsname
    NAME = args.name
    POSITION = args.position
    pull_remote(IP, MCSNAME, NAME, POSITION)


if __name__ == '__main__':
    main()
