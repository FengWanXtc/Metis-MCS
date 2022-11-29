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

def create_preview(IP, mcsname ,Geometry):

    cre_data = read_json_file('17.7.7  Update the Crop parameter for Operation in VideoTransformSpecs.json')
    cre_data["VideoTransformSpecs"][0]["Geometry"] = Geometry
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


def main(Geometry,IP):
    parser = argparse.ArgumentParser(
        description='usage: python3 create_one_frame_preview.py --name=Teacher --frame_number=1')
    parser.add_argument('--mcsname', '-t', type=str, default='mcs0.3', help='The name of the mcstask')
    parser.add_argument('-ip', type=str, default='', help='The IP Address')

    args = parser.parse_args()
    MCSNAME = args.mcsname



    create_preview(IP, MCSNAME,Geometry)


if __name__ == '__main__':
    IP = input("Please Input Metis IP: ")
    Geometry = []
    main(Geometry,IP)
    time.sleep(5)
    os.system('python delete_all_tasks.py')
    time.sleep(2)
    Geometry = [0, 0, 480, 270]
    main(Geometry,IP)
    time.sleep(5)
    os.system('python delete_all_tasks.py')
    time.sleep(2)
    Geometry = [0, 0, 960, 540]
    main(Geometry,IP)
    time.sleep(5)
    os.system('python delete_all_tasks.py')
    time.sleep(2)
    Geometry = [0, 0, 1440, 810]
    main(Geometry)
    print("10s后任务删除")
    time.sleep(10)
    os.system('python delete_all_tasks.py')
