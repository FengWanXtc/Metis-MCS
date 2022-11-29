import json
import sys
import time

sys.path.append('../../../libraries')
from mediatasklib import *
from functionlib import *


def S4E7_Basic():
    # 设置对应的MCS
    IP = input("Please Input Near-End Metis IP: ")
    IP_F = input("Please Input Far-End Metis IP: ")
    data = read_json_file('17.9.2 Dynamic Change time.json')
    # CAM1、CAM2、CAM_IN 的 DeviceId基本已定,需修改的是IPC
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType='IPC', aiStrategy='student')
    data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    data["CodecStreamSpecs"][0]["URI"] = "rtsp://{}:8554/metis/ch1".format(IP_F)
    data["CodecStreamSpecs"][1]["URI"] = "rtsp://{}:8554/metis/ch2".format(IP_F)
    data["CodecStreamSpecs"][2]["URI"] = "rtsp://{}:8554/metis/ch3".format(IP_F)
    # print(data)
    # print(json.dumps(S4E3_data, indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.url)
    except:
        print('Post Create Task Failed.')
        print(response)

    print("当前分段录制时间为2700s，为确保生成录制文件有效正在录制30s请稍等")
    time.sleep(30)
    print("动态修改分段录制时间为30s")
    data["RecordSpecs"][0]["SplitUnit"] = 30
    data["RecordSpecs"][1]["SplitUnit"] = 30
    data["RecordSpecs"][2]["SplitUnit"] = 30
    data["RecordSpecs"][3]["SplitUnit"] = 30
    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.url)
    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201 or response.json()['Code'] == 202:
        print('Test Pass!')
    else:
        print('Test Fail!')
        print(response.json())


if __name__ == '__main__':
    S4E7_Basic()
