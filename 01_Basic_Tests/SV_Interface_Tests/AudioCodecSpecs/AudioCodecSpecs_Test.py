import argparse
import json
import sys

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *
from mediadevicelib import get_md_audio_in


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
    MCS = read_json_file("AudioCodecSpec_Test.json")
    AudioIns = get_md_audio_in().json()["AudioIns"]
    for AudioIn in AudioIns:
        if AudioIn["DeviceName"].find("BuiltIn USB Audio") != -1:
            MCS["AudioSpecs"][0]["DeviceId"] = AudioIn["DeviceId"]
        if AudioIn["DeviceName"].find("BuiltIn HDMI Audio") != -1:
            MCS["AudioSpecs"][1]["DeviceId"] = AudioIn["DeviceId"]

    # print(json.dumps(MCS, indent=2))

    # AudioCodecSpec_01
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("AudioCodecSpec_01", response, 201)

    # AudioCodecSpec_02
    MCS["AudioCodecSpecs"][1]["BitRate"] = "20Kbps"
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("AudioCodecSpec_02", response, 201)

    # AudioCodecSpec_03
    MCS["AudioCodecSpecs"][1]["BitRate"] = "-100Kbps"
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("AudioCodecSpec_03", response, 400)

    # AudioCodecSpec_04
    MCS["AudioCodecSpecs"][1]["BitRate"] = "test Kbps"
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("AudioCodecSpec_04", response, 400)

    # AudioCodecSpec_05
    MCS["AudioCodecSpecs"][1]["BitRate"] = "512gbps"
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("AudioCodecSpec_05", response, 400)

    # AudioCodecSpec_06
    MCS["AudioCodecSpecs"][1]["BitRateMode"] = "CBR"
    MCS["AudioCodecSpecs"][1]["BitRate"] = "44Kbps"
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("AudioCodecSpec_06", response, 201)

    # AudioCodecSpec_07
    MCS["AudioCodecSpecs"][1]["BitRateMode"] = "VBR"
    MCS["AudioCodecSpecs"][1]["BitRate"] = "256Kbps"
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("AudioCodecSpec_07", response, 201)


if __name__ == '__main__':
    main()
