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
    data = read_json_file('17.9.6  Dynamically modify size.json')
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

    time.sleep(10)
    print("需要观察录制生成的问题是否1m大小生成")

    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.json())
    except:
        print('Post Create Task Failed.')
        print(response)
    time.sleep(10)
    print("动态修改分段录制大小为-100,需要观察录制生成的问题是否还是以1M生成/或不分段")
    data["RecordSpecs"][0]["SplitUnit"] = -100
    data["RecordSpecs"][1]["SplitUnit"] = -100
    data["RecordSpecs"][2]["SplitUnit"] = "***"
    data["RecordSpecs"][3]["SplitUnit"] = "***"
    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.json())
    except:
        print('Post Create Task Failed.')
        print(response)

if __name__ == '__main__':
    S4E7_Basic()
