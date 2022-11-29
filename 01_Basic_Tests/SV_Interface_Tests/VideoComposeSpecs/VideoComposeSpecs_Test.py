import argparse
import sys
import time

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


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
    MCS = read_json_file("VideoComposeSpec_Test.json")
    # 填充对应的设备算法
    Teacher_DeviceId = get_DeviceId_by_aiStrategy(ip='', camType='HDMI', aiStrategy='teacher')
    MCS['VideoSpecs'][0]['DeviceId'] = Teacher_DeviceId
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip='', camType='IPC', aiStrategy='student')
    MCS['VideoSpecs'][1]['DeviceId'] = Student_DeviceId

    # print(json.dumps(MCS, indent=2))

    # AudioCodecSpec_01
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("VideoComposeSpec_01", response, 201)
    time.sleep(5)
    # AudioCodecSpec_02
    # 先remove移除原来的compose
    remove_data = {"Name": "VideoComposeSpecTest", "SpecNames": ["Compositor"]}
    response = post_mt_remove(ip=IP, data=remove_data)
    if response.json()["Code"] != 200:
        print("Test Case:: AudioCodecSpec_02 Fail!")
        print(response.json())
        return False
    # 重新创建新的Compose
    MCS = read_json_file("VideoComposeSpec_Test_02.json")
    response = post_mt_create_update(data=MCS, ip=IP)
    check_result("VideoComposeSpec_02", response, 201)


if __name__ == '__main__':
    main()
