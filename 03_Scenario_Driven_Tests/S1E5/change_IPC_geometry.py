import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def change_geometry(geometry):
    change_geo_data = read_json_file('create_remote_IPC.json')
    change_geo_data['RenderSpecs'][0]['CompositionSpec'][0]['Geometry'] = geometry

    try:
        response = post_mt_create_update(ip='', data=change_geo_data)
    except:
        print('Change IPC Frame Position Fail')
        print(response.status_code)
        return False

    if (response.json()['Code'] == 201):
        print('Change IPC Frame Position Success!')
        return True
    else:
        print('Change IPC Frame Position Fail!')
        print(response.json())
        return response.json()


def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 change_IPC_geometry.py --geometry=x,y,weight,height')
    parser.add_argument('--geometry', '-g', type=str, default='0,0,960,540',
                        help='The geometry of the screen ,default is 0,0,960,540')
    args = parser.parse_args()
    GEOMETRY = list(map(int, args.geometry.split(',')))
    change_geometry(GEOMETRY)


if __name__ == '__main__':
    main()
