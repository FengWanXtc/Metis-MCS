import argparse
import copy
import json
import sys
import time

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *
from mediadevicelib import *


# 构造MCS 各个Spec过程,因为现在命名规范起来,所以可以定死DeviceId

def check_result(caseName, response, judgement):
    if response.json()["Code"] == judgement:
        print("Test Case:: {} Pass!".format(caseName))
    else:
        print("Test Case:: {} Fail!".format(caseName))
        print(json.dumps(response.json()))


def main():
    parser = argparse.ArgumentParser(description='usage: python XXX.py --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('--interval', '-i', type=int, default=5, help='The Interval of time')

    args = parser.parse_args()
    IP = args.ip
    Interval = args.interval

    # 设置MCS 内容
    # 获取输入设备的DeviceId
    MCS = read_json_file("PlaySpecs_Test.json")
    AudioIns = get_md_audio_in().json()["AudioIns"]
    MICDeviceId = "0103-0200"  # 默认值
    PCDeviceId = "0100-0101"
    for AudioIn in AudioIns:
        if AudioIn["DeviceName"].find("BuiltIn USB Audio") != -1:
            MICDeviceId = AudioIn["DeviceId"]
            MCS["AudioSpecs"][0]["DeviceId"] = AudioIn["DeviceId"]
        if AudioIn["DeviceName"].find("BuiltIn HDMI Audio") != -1:
            PCDeviceId = AudioIn["DeviceId"]
            MCS["AudioSpecs"][1]["DeviceId"] = AudioIn["DeviceId"]
    # 获取输出设备的DeviceId
    AudioOuts = get_md_audio_out().json()["AudioOuts"]
    for AudioOut in AudioOuts:
        if AudioOut["DeviceName"].find("BuiltIn USB Audio") != -1:
            MCS["PlaySpecs"][0]["DeviceId"] = AudioOut["DeviceId"]
    # print(json.dumps(MCS, indent=2))

    MCS_Copy = copy.deepcopy(MCS)

    # PlaySpecs_01
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("PlaySpecs_01", response, 201)
    time.sleep(Interval)

    # PlaySpecs_02
    MCS["PlaySpecs"][0]["Sources"][0]["SourceName"] = "PC"
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("PlaySpecs_02", response, 201)
    time.sleep(Interval)

    # PlaySpecs_03
    MCS["PlaySpecs"][0]["Sources"][0]["SourceName"] = "MIC"
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("PlaySpecs_03", response, 201)
    time.sleep(Interval)

    # PlaySpecs_04
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("PlaySpecs_04", response, 201)
    time.sleep(Interval)

    # PlaySpecs_05
    MCS["PlaySpecs"][0]["Sources"].append({"SourceName": "PC", "Volume": 60})
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("PlaySpecs_05", response, 201)
    time.sleep(Interval)

    # PlaySpecs_06
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("PlaySpecs_06", response, 201)
    time.sleep(Interval)

    # PlaySpecs_07
    MCS["PlaySpecs"][0]["Sources"][1]["Volume"] = 100
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("PlaySpecs_07", response, 201)
    time.sleep(Interval)

    # PlaySpecs_08
    AudioMCS = {"DeviceId": MICDeviceId, "Volume": 0}
    response = post_md_audio_in_config(ip=IP, databody=AudioMCS)
    check_result("PlaySpecs_08_Part1", response, 200)
    time.sleep(Interval)

    AudioMCS = {"DeviceId": MICDeviceId, "Volume": 70}
    response = post_md_audio_in_config(ip=IP, databody=AudioMCS)
    check_result("PlaySpecs_08_Part2", response, 200)

    # PlaySpecs_09
    MCS_Copy["AudioCodecSpecs"][0]["SourceName"] = "Wrong Source"
    response = post_mt_create_update(ip=IP, data=MCS_Copy)
    check_result("PlaySpecs_09", response, 201)
    time.sleep(Interval)

    AudioMCS = {"DeviceId": MICDeviceId, "Volume": 1000}
    response = post_md_audio_in_config(ip=IP, databody=AudioMCS)
    check_result("PlaySpecs_10_Part1", response, 200)

    AudioMCS = {"DeviceId": PCDeviceId, "Volume": -100}
    response = post_md_audio_in_config(ip=IP, databody=AudioMCS)
    check_result("PlaySpecs_10_Part2", response, 200)


if __name__ == '__main__':
    main()
