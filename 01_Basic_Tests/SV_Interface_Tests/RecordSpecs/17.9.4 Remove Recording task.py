import json
import sys
import time

import requests

sys.path.append('../../../libraries')
from mediatasklib import *
from functionlib import *


def S4E7_Basic():
    # 设置对应的MCS
    IP = input("Please Input Near-End Metis IP: ")
    IP_F = input("Please Input Far-End Metis IP: ")
    data = read_json_file('17.9.4 Remove Recording task.json')
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
    print("分段录制时间为10s,输入回车停止录制")
    input("")
    tempurl = "http://{}:6689/mediatask/remove".format(IP)
    databody = {
        "Name": "Basic_MCS",
        "SpecNames": [
            "Director_Record",
            "remote1_Record",
            "remote2_Record",
            "remote3_Record"
        ]
    }
    response = requests.post(url=tempurl, json=databody)
    print(response.json())



if __name__ == '__main__':
    S4E7_Basic()
