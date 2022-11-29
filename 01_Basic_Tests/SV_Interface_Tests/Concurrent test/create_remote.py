import argparse
import json
import sys

sys.path.append('../../../libraries')
from mediatasklib import *
from functionlib import *


def main(IP,TARGET):
    # 设置对应的MCS

    data = read_json_file('create_remote.json')
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType='IPC', aiStrategy='student')
    data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    data["ServerSpecs"][0]["URI"] = "wp://{}:6671".format(TARGET)
    data["ServerSpecs"][1]["URI"] = "wp://{}:6672".format(TARGET)
    data["ServerSpecs"][2]["URI"] = "wp://{}:6675".format(TARGET)
    data["ServerSpecs"][3]["URI"] = "wp://{}:6676".format(TARGET)
    data["ServerSpecs"][4]["URI"] = "wp://{}:6677".format(TARGET)
    data["ServerSpecs"][5]["URI"] = "wp://{}:6678".format(TARGET)
    # CAM1、CAM2、CAM_IN 的 DeviceId基本已定,需修改的是IPC
    # print(json.dumps(data,indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response.status_code)
    # print(response.status_code)

    if response.json()['Code'] == 201:
        print('Director Push Test Pass!')
    else:
        print('Director Push Test Fail!')
        print(response.json())


if __name__ == '__main__':
    main()
