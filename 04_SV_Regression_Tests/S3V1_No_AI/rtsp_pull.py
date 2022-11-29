import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def pull_remote(ip, mcsname, position, uri):
    pull_re_data = read_json_file('rtsp_pull.json')
    pull_re_data["Name"] = mcsname
    pull_re_data['CodecStreamSpecs'][0]['URI'] = "rtsp://10.12.224.{}".format(uri)
    if position == '1':
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [0, 0, 960, 540]
    elif position == '2':
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [960, 0, 960, 540]
    elif position == '3':
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [0, 540, 960, 540]
    else:
        pull_re_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [960, 540, 960, 540]
    try:
        response = post_mt_create_update(ip=ip, data=pull_re_data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Create one frame preview {} Success'.format(mcsname))
        return True
    else:
        print('Create one frame preview {} Fail'.format(mcsname))
        return False


def main():
    parser = argparse.ArgumentParser(description='usage: python3 pull_remote.py --template=four frame')
    parser.add_argument('--mcsname', '-mn', type=str, default='Remote_1', help='The name of MCS name.')
    parser.add_argument('-ip', type=str, default='', help='The ip of the station.')
    parser.add_argument('--position', '-p', type=str, default='1', help='The position of the frame,default is 1')
    parser.add_argument('-uri', type=str, default='48/ch1', help='The URI of RTSP IPC Pull.')

    args = parser.parse_args()
    IP = args.ip
    MCSNAME = args.mcsname
    POSITION = args.position
    URI = args.uri
    pull_remote(IP, MCSNAME, POSITION, URI)


if __name__ == '__main__':
    main()
