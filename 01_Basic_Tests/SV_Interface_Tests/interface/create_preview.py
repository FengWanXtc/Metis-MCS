import sys
import argparse

sys.path.append('../../../libraries')
from mediatasklib import *
from functionlib import *
from authlib import *
from mediadevicelib import *

def get_IPC_response(IP):
    # 传入一个字符型数字，根据数字找内容
    # 利用Video in 获取 4个 IPC 摄像头
    token = post_auth().headers['Token']
    response = get_md_video_in(ip=IP, token=token)
    # print(response.json())
    return response.json()["VideoIns"]

def create_preview(IP):
    cre_data = read_json_file('create_preview.json')
    VideoIns = get_IPC_response(IP)
    item = get_item(VideoIns, "teacher")
    # print(VideoIns)
    if item != False:
        cre_data["VideoSpecs"][0]["DeviceId"] = item["DeviceId"]
    else:
        print("未找到教师摄像头！")
    item = get_item(VideoIns, "student")
    if item !=False:
        cre_data["VideoSpecs"][1]["DeviceId"] = item["DeviceId"]
    else:
        print("未找到学生摄像头！")
    cre_data["CodecStreamSpecs"][0]["URI"] = "wp://{}:6671".format(IP)
    cre_data["CodecStreamSpecs"][1]["URI"] = "wp://{}:6672".format(IP)
    try:
        response = post_mt_create_update(ip=IP, data=cre_data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Create one frame preview Success')
        return True
    else:
        print('Create one frame preview Fail')
        return False


def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 create_one_frame_preview.py --name=Teacher --frame_number=1')
    parser.add_argument('-ip', type=str, default='', help='The IP Address')
    args = parser.parse_args()
    IP = args.ip
    IP = input("Please Input Metis IP: ")

    create_preview(IP)


if __name__ == '__main__':
    main()
