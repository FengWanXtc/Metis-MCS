import sys
import argparse

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def post_create(argc_ip, jsonfile, mcsname):
    # 封装的读取json文件的函数,保存为一个字典对象data
    data = read_json_file('{}.json'.format(jsonfile))
    data['Name'] = mcsname
    # ***print可以用于查看MCS是怎么样的***
    # print(json.dumps(data, indent=2))

    try:
        response = post_mt_create_update(ip=argc_ip, data=data)
    except:
        print('Post Create Task Failed')
        print(response.status_code)
        return False

    # if response.json()['Code'] == 201 or response.json()['Code'] == 202:
    if response.json()['Code'] == 201:
        print('Create Update :: ({}) Success'.format(jsonfile))
        return True
    else:
        print('Create Update :: ({}) Fail'.format(jsonfile))
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
