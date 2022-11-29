import json
import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def pull_remote(IP, mcsname, uri, position):
    pull_re_data = read_json_file('rtsp_pull.json')
    # 填写MCS模板内容
    pull_re_data["Name"] = mcsname
    pull_re_data['CodecStreamSpecs'][0]['URI'] = "rtsp://{}:8554/metis/test".format(uri)
    if position == '1':
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [0, 0, 960, 540]
    elif position == '2':
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [960, 0, 960, 540]
    elif position == '3':
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [0, 540, 960, 540]
    else:
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [960, 540, 960, 540]
    # print(json.dumps(pull_re_data,indent=2))
    try:
        response = post_mt_create_update(ip=IP, data=pull_re_data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Create RTSP Pull preview {} Success'.format(mcsname))
        return True
    else:
        print('Create RTSP Pull preview {} Fail'.format(mcsname))
        return False


def main():
    parser = argparse.ArgumentParser(description='usage: python3 remote_pull.py --template=four frame')
    parser.add_argument('-ip', type=str, default='', help='The ip of the far end station')
    parser.add_argument('--mcsname', '-mn', type=str, default='remote', help='The name of the mcstask')
    parser.add_argument('-uri', type=str, required=True, help='The URI of Rtsp pull Stream')
    parser.add_argument('--position', '-p', type=str, default='1', help='The position of the frame,default is 1')
    args = parser.parse_args()
    IP = args.ip
    MCSNAME = args.mcsname
    URI = args.uri
    POSITION = args.position
    pull_remote(IP, MCSNAME, URI, POSITION)


if __name__ == '__main__':
    main()
