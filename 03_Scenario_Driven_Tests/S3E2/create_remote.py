import argparse
import sys

sys.path.append('../../Libraries')
from functionlib import *
from mediatasklib import *


def create_remote(IP, name, geometry, identity):
    cre_re_data = read_json_file('create_remote.json')
    cre_re_data['Name'] = name
    cre_re_data['RtcStreamSpec']['Identity'] = identity
    cre_re_data['RenderSpecs'][0]['CompositionSpec'][0]['Geometry'] = geometry

    try:
        response = post_mt_create_update(ip=IP, data=cre_re_data)

    except:
        print('Post Create Task Failed')
        print(response.json())

    if response.json()['Code'] == 201:
        print('Create Agora Pull Frame {} Success'.format(name))
        return True
    else:
        print('Create Agora Pull Frame {} Fail'.format(name))
        print(response.json())
        return False


def main():
    parser = argparse.ArgumentParser(description='usage: python3 create_remote.py --name=1')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('--name', '-n', type=str, default='Remote_1', help='The Name of the remote MCS .')
    parser.add_argument('--geometry', '-g', type=str, default='0,0,960,540', help='The position of the frame.')
    parser.add_argument('--identity', '-i', type=str, default='RT_1',
                        help='The identity ( Remote Teacher 1 )of the Agora Identity.')
    args = parser.parse_args()
    IP = args.ip
    NAME = args.name
    GEOMETRY = list(map(int, args.geometry.split(',')))
    IDENTITY = args.identity
    create_remote(IP, NAME, GEOMETRY, IDENTITY)


if __name__ == '__main__':
    main()
