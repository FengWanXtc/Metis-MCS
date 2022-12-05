import sys
import argparse
sys.path.append('../../Libraries')

from environmentlib import *
from mediatasklib import *
from functionlib import *


GeneralCamType = Global_GeneralCamType


def change_json_file(filename, Name, DeviceId, Geometry):
    data = read_json_file(filename)
    data[Name] = {}
    # print(data)
    data[Name]["DeviceId"] = DeviceId
    data[Name]["Geometry"] = Geometry
    # write
    with io.open('json_templates/{}'.format(filename), "w") as jsonfile:
        json.dump(data, jsonfile, indent=2)
    # print(data)


def create_one_frame_preview(argc_ip, name, camType, camNum, geometry):
    cre_of_pr_data = read_json_file('create_preview.json')
    cre_of_pr_data['VideoSpecs'][0]['Name'] = name
    cre_of_pr_data['RenderSpecs'][0]['CompositionSpec'][0]['SourceName'] = name
    # 设置DeviceId
    DeviceId = get_Video_DeviceId_by_internal_camera(argc_ip, camType, camNum)
    cre_of_pr_data['VideoSpecs'][0]['DeviceId'] = DeviceId

    # 设置窗口位置
    cre_of_pr_data['RenderSpecs'][0]['CompositionSpec'][0]['Geometry'] = geometry
    # 将新的MCS相关信息写进一个Json文件，后续只需要读取这个文件，比起get接口获取信息耗时少，方便change geometry
    change_json_file("FrameData.json", name, DeviceId, geometry)
    # print(json.dumps(cre_of_pr_data, indent=2))

    try:
        response = post_mt_create_update(ip=argc_ip, data=cre_of_pr_data)
    except:
        print('Post Create Task Failed')
        print(response.status_code)
        return False

    if (response.json()['Code'] == 201):
        print('Create one frame preview {} Success'.format(name))
        return True
    else:
        print('Create one frame preview {} Fail'.format(name))
        print(response.json())
        return False




def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 create_preview.py -n=teacher -ct=HDMI -cn=0 -g=0,0,960,540')
    # 指定哪个HDMI口
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('--name', '-n', type=str, default='Teacher', help='The name of the frame,default is Teacher')
    parser.add_argument('--camtype', '-ct', type=str, default=GeneralCamType, help='The camera type,default is HDMI')
    parser.add_argument('--camnum', '-cn', type=str, default='1', help='The camera order,default is 1')
    parser.add_argument('--geometry', '-g', type=str, default='0,0,960,540',
                        help='The geometry of the frame,default is 0,0,960,540')
    args = parser.parse_args()
    # 获取Geometry
    IP = args.ip
    NAME = args.name
    CAMNUM = args.camnum
    CAMTYPE = args.camtype
    GEOMETRY = list(map(int, args.geometry.split(',')))
    create_one_frame_preview(IP, NAME, CAMTYPE, CAMNUM, GEOMETRY)


if __name__ == '__main__':
    main()
