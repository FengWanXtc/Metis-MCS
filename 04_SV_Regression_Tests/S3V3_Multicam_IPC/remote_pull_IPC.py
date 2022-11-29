import requests
import json
import os
import sys
import argparse

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def pull_remote(IP, rtsp, mcsname, name, position):
    pull_re_data = read_json_file('remote_pull_IPC.json')
    pull_re_data["Name"] = mcsname
    # 填写MCS模板内容rtsp://10.12.224.48/ch2
    # 填写URI
    pull_re_data['CodecStreamSpecs'][0]['URI'] = 'rtsp://10.12.224.{}'.format(rtsp)
    # 传入名字，也是TaskId存放名
    pull_re_data['CodecStreamSpecs'][0]['Name'] = pull_re_data['RenderSpecs'][0]['CompositionSpec'][0]['SourceName'] = name
    # 宫格位置
    if position == '1':
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [0, 0, 960, 540]
    elif position == '2':
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [960,0,960,540]
    elif position == '3':
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [0,540,960,540]
    else:
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [960,540,960,540]
    # print(json.dumps(pull_re_data,indent=2))
    if (IP == ''):
        try:
            response = post_mt_create_update(data=pull_re_data)
        except :
            print('Post pull remote Task Failed')
            print(response.json())
    else:
        try:
            response = post_mt_create_update(data=pull_re_data, ip=IP)
        except:
            print('Post pull remote Task Failed')
            print(response.json())


    if (response.json()['Code'] == 201):
        print('Create Remote frame {} Success'.format(name))
        return True
    else:
        print('Create Remote frame {} Fail'.format(name))
        return False


def main():
    parser = argparse.ArgumentParser(description='usage: python3 remote_pull.py --template=four frame')
    parser.add_argument('-ip', type=str, default='', help='The ip of Metis Station to pull remote stream')
    parser.add_argument('--rtsp', '-r', type=str, default='57/ch2', help='The RTSP Address of IPC Camera.')
    parser.add_argument('--mcsname', '-t', type=str, default='remote', help='The name of the mcstask')
    parser.add_argument('--position', '-p', type=str, default='1', help='The position of the frame,default is 1')
    parser.add_argument('--name', '-n', type=str, default='IPC1', help='The name of the frame,default is IPC1')
    args = parser.parse_args()
    IP = args.ip
    RTSP = args.rtsp
    MCSNAME = args.mcsname
    NAME = args.name
    POSITION = args.position
    pull_remote(IP, RTSP, MCSNAME, NAME, POSITION)


if __name__ == '__main__':
    main()
