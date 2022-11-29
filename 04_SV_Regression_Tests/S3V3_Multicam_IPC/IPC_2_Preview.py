import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *
from mediadevicelib import get_md_video_in
from authlib import post_auth


def get_IPC_response(hostIP):
    # 传入一个字符型数字，根据数字找内容
    # 利用Video in 获取 4个 IPC 摄像头
    token = post_auth(username='admin', password='admin').headers['Token']
    # print(token)
    ip = hostIP
    response = get_md_video_in(ip,token)
    return response.json()["VideoIns"]


def create_preview(IP):
    cre_data = read_json_file('IPC_2_Preview.json')

    # 获取DeviceId
    VideoIns = get_IPC_response(IP)
    item = get_item(VideoIns, "teacher")
    cre_data["VideoSpecs"][0]["DeviceId"] = item["DeviceId"]

    item = get_item(VideoIns, "student")
    cre_data["VideoSpecs"][1]["DeviceId"] = item["DeviceId"]
    # print(cre_data['VideoSpecs'])

    try:
        response = post_mt_create_update(ip=IP,data=cre_data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if response.json()['Code'] == 201:
        print('Create IPC 2 frame preview Success')
        return True
    else:
        print('Create IPC 2  frame preview Fail')
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip
    create_preview(IP)
