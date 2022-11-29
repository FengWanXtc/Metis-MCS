import sys
import argparse

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *

def read_json_file(filename):
    # path = os.path.abspath(os.path.join(os.getcwd(), "../json_templates/"))
    path = 'json_gen'
    filepath = path + '/' + filename
    file = open(filepath, 'r')
    data = json.load(file)
    return data

def post_create(argc_ip, jsonfile, mcsname):

    data = read_json_file('{}.json'.format(jsonfile))
    try:
        response = post_mt_remove(ip=argc_ip, data=data)
    except:
        print('Post remove Task Failed')
        print(response.status_code)
        return False

    if response.json()['Code'] == 200:
        print('remove ({}) Success'.format(jsonfile))
        return True
    else:
        print('remove ({}) Fail'.format(jsonfile))
        print(response.json())
        return False


def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 create_one_frame_preview.py -n=teacher -ct=HDMI -cn=0 -g=0,0,960,540')
    # 指定哪个HDMI口
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('--jsonfile', '-jf', type=str, required=True, help='The JsonFile to create update')
    parser.add_argument('-mcsname', '-mn', type=str, required=True, help='The MCS Name')
    args = parser.parse_args()
    # 获取Geometry
    IP = args.ip
    JSONFILE = args.jsonfile
    MCSNAME = args.mcsname
    post_create(IP, JSONFILE, MCSNAME)


if __name__ == '__main__':
    main()
