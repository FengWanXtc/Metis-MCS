import sys
import argparse
import json

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def change_geometry(geometry, name):
    change_geo_data = read_json_file('create_preview.json')
    change_geo_data['Name'] = change_geo_data['VideoSpecs'][0]['Name'] = name
    change_geo_data['RenderSpecs'][0]['CompositionSpec'][0]['SourceName'] = name
    change_geo_data['RenderSpecs'][0]['CompositionSpec'][0]['Geometry'] = geometry
    # 不用接口请求获取DeviceId,而是通过读取文件，能更省时
    DeviceId = read_json_file('FrameData.json')[name]['DeviceId']
    change_geo_data['VideoSpecs'][0]['DeviceId'] = DeviceId
    # print(change_geo_data)
    # print(json.dumps(change_geo_data, indent=2))

    try:
        response = post_mt_create_update(ip='', data=change_geo_data)
    except:
        print('Update Task which MCS Name is {} Fail.'.format(name))
        print(response.status_code)
        return False
    if (response.json()['Code'] == 201):
        print('Change {} Geometry Success!'.format(name))
        return True
    else:
        print('Change {} Geometry Fail.'.format(name))
        print(response.json())
        return False

def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 change_geometry.py --name=Teacher --geometry=x,y,weight,height')
    parser.add_argument('--geometry', '-g', type=str, default='0,0,960,540',
                        help='The geometry of the screen ,default is 0,0,960,540')
    parser.add_argument('--name', '-n', required=True, help='The name of the action ,default USB1')
    args = parser.parse_args()
    # change str to list
    GEOMETRY = list(map(int, args.geometry.split(',')))
    # change list str items into int items
    NAME = args.name
    change_geometry(GEOMETRY, NAME)


if __name__ == '__main__':
    main()
