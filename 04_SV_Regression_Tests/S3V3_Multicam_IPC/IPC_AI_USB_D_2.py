import sys
import argparse

sys.path.append('../../Libraries')
from authlib import *
from mediatasklib import *
from functionlib import *
from mediadevicelib import *


def get_IPC_response(hostIP):
    # 传入一个字符型数字，根据数字找内容
    # 利用Video in 获取 4个 IPC 摄像头
    token = post_auth(username='admin', password='admin').headers['Token']
    # print(token)
    ip = hostIP
    response = get_md_video_in(ip,token)
    return response.json()["VideoIns"]


def create_preview_IPC(ip):
    cr_pr_IPC_data = read_json_file('IPC_AI_USB_D_2.json')

    VideoIns = get_IPC_response(ip)
    item = get_item(VideoIns, "student")
    cr_pr_IPC_data["VideoSpecs"][1]["DeviceId"] = item["DeviceId"]
    item = get_item(VideoIns, "teacher")
    cr_pr_IPC_data["VideoSpecs"][0]["DeviceId"] = item["DeviceId"]

    try:
        response = post_mt_create_update(ip=ip, data=cr_pr_IPC_data)
    except:
        print('Post pull remote Task Failed')
        print(response.json())


    if (response.json()['Code'] == 201):
        print('Create IPC AI 2 (IPC+USB) Frames Success')
        return True
    else:
        print('Create IPC AI 2 (IPC+USB) Frames Fail')
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 remote_pull.py --template=four frame')
    parser.add_argument('-ip', type=str, default='', help='The ip of the far end station')
    args = parser.parse_args()
    IP = args.ip
    create_preview_IPC(IP)
