import argparse
import json
import sys
import time

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def check_result(caseName, response, judgement):
    if response.json()["Code"] == judgement:
        print("Test Case:: {} Pass!".format(caseName))
    else:
        print("Test Case:: {} Fail!".format(caseName))
        print(json.dumps(response.json()))


def VideoCodecSpecTest():
    # 设置对应的MCS
    parser = argparse.ArgumentParser(description='usage: python XXX.py --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('--interval', '-i', type=int, default=5, help='The Interval of time')

    args = parser.parse_args()
    IP = args.ip
    Interval = args.interval

    data = read_json_file('VideoCodecSpec_Test.json')
    # CAM1、CAM2、CAM_IN 的 DeviceId基本已定,需修改的是IPC
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType='IPC', aiStrategy='student')
    data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    Blackboard_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType='IPC', aiStrategy='blackboard')
    data['VideoSpecs'][3]['DeviceId'] = Blackboard_DeviceId

    response = post_mt_create_update(ip=IP, data=data)
    check_result("VideoCodecSpec_01", response, 201)

    time.sleep(1)
    data["VideoCodecSpecs"][1]["BitRate"] = "2mbps"
    response = post_mt_create_update(ip=IP, data=data)
    check_result("VideoCodecSpec_02", response, 201)

    time.sleep(1)
    data["VideoCodecSpecs"][1]["BitRate"] = "-50mbps"
    response = post_mt_create_update(ip=IP, data=data)
    check_result("VideoCodecSpec_03", response, 400)

    time.sleep(1)
    data["VideoCodecSpecs"][1]["BitRate"] = " test BPS"
    response = post_mt_create_update(ip=IP, data=data)
    check_result("VideoCodecSpec_04", response, 400)

    time.sleep(1)
    data["VideoCodecSpecs"][1]["BitRate"] = "512gbps"
    response = post_mt_create_update(ip=IP, data=data)
    check_result("VideoCodecSpec_05", response, 400)

    time.sleep(2)
    data["VideoCodecSpecs"][1]["BitRate"] = "2mbps"
    data["VideoCodecSpecs"][1]["BitRateMode"] = "CBR"
    response = post_mt_create_update(ip=IP, data=data)
    check_result("VideoCodecSpec_06", response, 201)

    time.sleep(2)
    data["VideoCodecSpecs"][1]["iFrameInterval"] = 25
    response = post_mt_create_update(ip=IP, data=data)
    check_result("VideoCodecSpec_07", response, 201)

    time.sleep(2)
    data["VideoCodecSpecs"][1]["idrInterval"] = 60
    response = post_mt_create_update(ip=IP, data=data)
    check_result("VideoCodecSpec_08", response, 201)
    time.sleep(2)
    data["VideoCodecSpecs"][1]["QpRange"] = [51, 51]
    response = post_mt_create_update(ip=IP, data=data)
    check_result("VideoCodecSpec_09", response, 201)


if __name__ == '__main__':
    VideoCodecSpecTest()
