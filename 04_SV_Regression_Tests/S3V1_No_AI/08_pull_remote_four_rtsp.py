import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def pull_remote(ip, mcsname):
    pull_re_data = read_json_file('08_pull_remote_four_rtsp.json')
    pull_re_data["Name"] = mcsname
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
    parser.add_argument('--mcsname', '-mn', type=str, default='RTSP_Pull_4F', help='The name of MCS name.')
    parser.add_argument('-ip', type=str, default='', help='The ip of the station.')
    args = parser.parse_args()
    IP = args.ip
    MCSNAME = args.mcsname
    pull_remote(IP, MCSNAME)


if __name__ == '__main__':
    main()
