import os
import sys
import argparse
import time

sys.path.append('../../../libraries')
from mediatasklib import *
from functionlib import *
from authlib import *
from mediadevicelib import *

def get_IPC_response(IP):
    # 传入一个字符型数字，根据数字找内容
    # 利用Video in 获取 4个摄像头
    token = post_auth().headers['Token']
    response = get_md_video_in(ip=IP, token=token)
    return response.json()["VideoIns"]

def create_preview(IP, mcsname , angle):

    cre_data = read_json_file('17.7.6  Dynamically modify Rotation.json')
    cre_data["VideoTransformSpecs"][0]["Rotation"] = angle
    VideoIns = get_IPC_response(IP)
    item = get_item(VideoIns, "teacher")
    if item != False:
        cre_data["VideoSpecs"][0]["DeviceId"] = item["DeviceId"]
    else:
        print("未找到教师摄像头！")
    item = get_item(VideoIns, "student")
    if item != False:
        cre_data["VideoSpecs"][1]["DeviceId"] = item["DeviceId"]
    else:
        print("未找到学生摄像头！")
    cre_data["Name"] = mcsname
    try:
        response = post_mt_create_update(ip=IP, data=cre_data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Create preview Success')
        return True
    else:
        print('Create preview Fail')
        return False


def main(angle,IP):
    parser = argparse.ArgumentParser(
        description='usage: python3 create_one_frame_preview.py --name=Teacher --frame_number=1')
    parser.add_argument('--mcsname', '-t', type=str, default='mcs0.3', help='The name of the mcstask')
    parser.add_argument('-ip', type=str, default='', help='The IP Address')
    parser.add_argument('-angle', type=str, default='90', help='The angle of the Rotation')

    args = parser.parse_args()
    ANGLE = args.angle
    MCSNAME = args.mcsname

    ANGLE = angle

    create_preview(IP, MCSNAME, ANGLE)


if __name__ == '__main__':
    IP = input("Please Input Metis IP: ")
    angle = 90
    main(angle,IP)
    print("5s后切换为180度旋转")
    time.sleep(5)
    os.system('python delete_all_tasks.py')
    time.sleep(2)
    angle = 180
    main(angle,IP)
    print("5s后切换为270度旋转")
    time.sleep(5)
    os.system('python delete_all_tasks.py')
    time.sleep(2)
    angle = 270
    main(angle,IP)
    print("10s后任务删除")
    time.sleep(10)
    os.system('python delete_all_tasks.py')
