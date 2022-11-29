import argparse
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
    args = parser.parse_args()
    IP = args.ip

    # 设置MCS 内容
    MCS = read_json_file("AudioComposeSpec_Test.json")
    AudioIns = get_md_audio_in().json()["AudioIns"]
    for AudioIn in AudioIns:
        if AudioIn["DeviceName"].find("BuiltIn USB Audio") != -1:
            MCS["AudioSpecs"][0]["DeviceId"] = AudioIn["DeviceId"]
        if AudioIn["DeviceName"].find("BuiltIn HDMI Audio") != -1:
            MCS["AudioSpecs"][1]["DeviceId"] = AudioIn["DeviceId"]

    AudioOuts = get_md_audio_out().json()["AudioOuts"]
    for AudioOut in AudioOuts:
        if AudioOut["DeviceName"].find("BuiltIn USB Audio") != -1:
            MCS["PlaySpecs"][0]["DeviceId"] = AudioOut["DeviceId"]
    # print(json.dumps(MCS, indent=2))

    # AudioComposeSpec_01
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("AudioComposeSpec_01", response, 201)
    time.sleep(5)
    # AudioComposeSpec_02
    MCS["PlaySpecs"][0]["Sources"][0]["Volume"] = 20
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("AudioComposeSpec_02", response, 201)
    # AudioComposeSpec_03
    time.sleep(5)
    MCS["PlaySpecs"][0]["Sources"][0]["Volume"] = 0
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("AudioComposeSpec_03", response, 201)


if __name__ == '__main__':
    main()
