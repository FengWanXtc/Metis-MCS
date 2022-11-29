import sys
import argparse

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *
from authlib import post_auth
from mediadevicelib import get_md_video_in


def get_IPC_response(hostIP):
    # 传入一个字符型数字，根据数字找内容
    # 利用Video in 获取 4个 IPC 摄像头
    token = post_auth(username='admin', password='admin').headers['Token']
    # print(token)
    ip = hostIP
    response = get_md_video_in(ip, token)
    return response.json()["VideoIns"]


def create_preview(IP, mcsname, name, position):
    cre_data = read_json_file('create_preview_IPC.json')
    cre_data["Name"] = mcsname
    VideoIns = get_IPC_response(IP)
    item = get_item(VideoIns, name)
    cre_data["VideoSpecs"][0]["DeviceId"] = item["DeviceId"]
    algorithm = name.title()
    cre_data['VideoAiSpecs'][0]['Name'] = cre_data['VideoAiSpecs'][0]['Algorithm'] = "{} Tracking".format(algorithm)
    cre_data['VideoAiSpecs'][0]['SourceName'] = cre_data["VideoSpecs"][0]["Name"] = algorithm
    cre_data["RenderSpecs"][0]["CompositionSpec"][0]["SourceName"] = algorithm

    if position == '1':
        cre_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [0, 0, 960, 540]
    elif position == '2':
        cre_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [960, 0, 960, 540]
    elif position == '3':
        cre_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [0, 540, 960, 540]
    else:
        cre_data["RenderSpecs"][0]["CompositionSpec"][0]["Geometry"] = [960, 540, 960, 540]
    try:
        response = post_mt_create_update(ip=IP, data=cre_data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Create one frame preview {} Success'.format(name))
        return True
    else:
        print('Create one frame preview {} Fail'.format(name))
        return False


def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 create_one_frame_preview.py --name=Teacher --frame_number=1')
    parser.add_argument('--mcsname', '-mn', type=str, default='IPC_T', help='The name of the mcstask')
    parser.add_argument('--name', '-n', type=str, default='Teacher', help='The name of the frame,default is Teacher')
    parser.add_argument('--position', '-p', type=str, default='1', help='The position of the frame,default is 1')
    parser.add_argument('-ip', type=str, default='', help='The IP Address')

    args = parser.parse_args()
    IP = args.ip
    MCSNAME = args.mcsname
    NAME = args.name
    POSITION = args.position

    create_preview(IP, MCSNAME, NAME, POSITION)


if __name__ == '__main__':
    main()
