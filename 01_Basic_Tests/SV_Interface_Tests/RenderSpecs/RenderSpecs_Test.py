import argparse
import json
import sys
import time

sys.path.append('../../../Libraries')
from mediadevicelib import *
from mediatasklib import *
from functionlib import *


def change_background(TYPE, IP):
    databody = {
        "DeviceId": "0800-0000",
        "Background": ""
    }
    if TYPE == 'null':
        databody["Background"] = "null"
    elif TYPE == 'png':
        databody["Background"] = "/home/user/EST/MCSScripts/background.png"
    elif TYPE == 'jpg':
        databody["Background"] = "/home/user/EST/MCSScripts/bgjpg.jpg"
    response = post_md_background(data=databody, ip=IP)

    if response.json()['Code'] != 200:
        print('Set Background Fail! Status Code As Follows!')
        print(response.status_code)
        return False
    return True


def Render_test_01(IP):
    MCS = read_json_file("RenderSpec_Test.json")
    VideoIns = get_md_video_in(ip=IP).json()["VideoIns"]
    # 赋值IPC 设备ID 给 MCS
    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find("IPC") != -1:
            MCS["VideoSpecs"][3]["DeviceId"] = VideoIn["DeviceId"]

    try:
        response = post_mt_create_update(ip=IP, data=MCS)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('Test Case :: Render_01 Pass!')
    else:
        print('Test Case :: Render_01 Fail!')
        print(response.json())


def Render_test_02(IP):
    MCS = read_json_file("RenderSpec_Test.json")
    VideoIns = get_md_video_in(ip=IP).json()["VideoIns"]
    # 赋值IPC 设备ID 给 MCS
    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find("IPC") != -1:
            MCS["VideoSpecs"][3]["DeviceId"] = VideoIn["DeviceId"]
    # 修改回显为一宫格
    MCS["RenderSpecs"][0]["CompositionSpec"] = [{"Geometry": [0, 0, 960, 540], "SourceName": "Teacher"}]

    try:
        response = post_mt_create_update(ip=IP, data=MCS)
    except:
        print('Test Case :: Render_02 Fail!')
        print(response)

    if response.json()['Code'] != 201:
        print(response.json())
        print('Test Case :: Render_02 Fail!')
    time.sleep(3)
    # 下面是修改Background
    StatusFlag_A = change_background("png", IP)
    time.sleep(3)
    StatusFlag_B = change_background("jpg", IP)

    if StatusFlag_A and StatusFlag_B:
        print('Test Case :: Render_02 Pass!')
    else:
        print('Test Case :: Render_02 Fail!')
    time.sleep(3)
    change_background("null", IP)


def Render_test_03(IP):
    MCS = read_json_file("RenderSpec_Test.json")
    VideoIns = get_md_video_in(ip=IP).json()["VideoIns"]
    # 赋值IPC 设备ID 给 MCS
    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find("IPC") != -1:
            MCS["VideoSpecs"][3]["DeviceId"] = VideoIn["DeviceId"]
    MCS["RenderSpecs"][0]["CompositionSpec"] = [{"Geometry": [0, 0, 1920, 1080], "SourceName": "Teacher"}]

    try:
        response = post_mt_create_update(ip=IP, data=MCS)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('Test Case :: Render_03 Pass!')
    else:
        print('Test Case :: Render_03 Fail!')
        print(response.json())


def Render_test_04(IP):
    MCS = read_json_file("RenderSpec_Test.json")
    VideoIns = get_md_video_in(ip=IP).json()["VideoIns"]
    # 赋值IPC 设备ID 给 MCS
    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find("IPC") != -1:
            MCS["VideoSpecs"][3]["DeviceId"] = VideoIn["DeviceId"]
    MCS["RenderSpecs"][0]["CompositionSpec"][1]["Geometry"] = [960, 0, 480, 270]
    MCS["RenderSpecs"][0]["CompositionSpec"][2]["Geometry"] = [0, 600, 480, 270]
    MCS["RenderSpecs"][0]["CompositionSpec"][3]["Geometry"] = [1000, 700, 480, 270]
    try:
        response = post_mt_create_update(ip=IP, data=MCS)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('Test Case :: Render_04 Pass!')
    else:
        print('Test Case :: Render_04 Fail!')
        print(response.json())


def Render_test_05(IP):
    MCS = read_json_file("RenderSpec_Test_02.json")
    VideoIns = get_md_video_in(ip=IP).json()["VideoIns"]
    # 赋值IPC 设备ID 给 MCS
    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find("IPC") != -1:
            MCS["VideoSpecs"][3]["DeviceId"] = VideoIn["DeviceId"]
    try:
        response = post_mt_create_update(ip=IP, data=MCS)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('Test Case :: Render_05 Pass!')
    else:
        print('Test Case :: Render_05 Fail!')
        print(response.json())


def Render_test_06(IP):
    MCS = read_json_file("RenderSpec_Test.json")
    VideoIns = get_md_video_in(ip=IP).json()["VideoIns"]
    # 赋值IPC 设备ID 给 MCS
    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find("IPC") != -1:
            MCS["VideoSpecs"][3]["DeviceId"] = VideoIn["DeviceId"]
    MCS["RenderSpecs"][0]["CompositionSpec"][0]["SourceName"] = "Computer"
    MCS["RenderSpecs"][0]["CompositionSpec"][2]["SourceName"] = "Teacher"
    try:
        response = post_mt_create_update(ip=IP, data=MCS)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('Test Case :: Render_06 Pass!')
    else:
        print('Test Case :: Render_06 Fail!')
        print(response.json())


def Render_test_07(IP):
    MCS = read_json_file("RenderSpec_Test.json")
    VideoIns = get_md_video_in(ip=IP).json()["VideoIns"]
    # 赋值IPC 设备ID 给 MCS
    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find("IPC") != -1:
            MCS["VideoSpecs"][3]["DeviceId"] = VideoIn["DeviceId"]
    MCS["RenderSpecs"][0]["CompositionSpec"][0] = {"Geometry": [0, 0, 960, 540],
                                                   "Picture": "/home/user/EST/MCSScripts/background.png"}
    MCS["RenderSpecs"][0]["CompositionSpec"][3] = {"Geometry": [960, 540, 960, 540],
                                                   "Picture": "/home/user/EST/MCSScripts/bgjpg.jpg"}
    try:
        response = post_mt_create_update(ip=IP, data=MCS)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('Test Case :: Render_07 Pass!')
    else:
        print('Test Case :: Render_07 Fail!')
        print(response.json())


def Render_test_08(IP):
    MCS = read_json_file("RenderSpec_Test.json")
    VideoIns = get_md_video_in(ip=IP).json()["VideoIns"]
    # 赋值IPC 设备ID 给 MCS
    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find("IPC") != -1:
            MCS["VideoSpecs"][3]["DeviceId"] = VideoIn["DeviceId"]
    MCS["RenderSpecs"][0]["CompositionSpec"][1]["FlipMethod"] = "Vertical"
    # print(json.dumps(MCS,indent=2))
    try:
        response = post_mt_create_update(ip=IP, data=MCS)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('Test Case :: Render_08 Pass!')
    else:
        print('Test Case :: Render_08 Fail!')
        print(response.json())


def main():
    parser = argparse.ArgumentParser(description='usage: python3 Render --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('--interval', '-i', type=int, default=5, help='The Interval of time')
    args = parser.parse_args()
    Interval = args.interval
    IP = args.ip

    Render_test_01(IP)
    time.sleep(Interval)
    Render_test_02(IP)
    time.sleep(Interval)
    Render_test_03(IP)
    time.sleep(Interval)
    Render_test_04(IP)
    time.sleep(Interval)
    Render_test_05(IP)
    time.sleep(Interval)
    Render_test_06(IP)
    time.sleep(Interval)
    Render_test_07(IP)
    time.sleep(Interval)
    Render_test_08(IP)


if __name__ == '__main__':
    main()
