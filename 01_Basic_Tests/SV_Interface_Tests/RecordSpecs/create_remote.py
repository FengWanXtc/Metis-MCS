import sys

sys.path.append('../../../libraries')
from mediatasklib import *
from functionlib import *


def main():
    IP = input("Please Input Far-End Metis IP: ")
    # 设置对应的MCS
    data = read_json_file('create_remote.json')
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType='IPC', aiStrategy='student')
    data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    data["ServerSpecs"][0]["URI"] = "rtsp://{}:8554/metis/ch1".format(IP)
    data["ServerSpecs"][1]["URI"] = "rtsp://{}:8554/metis/ch2".format(IP)
    data["ServerSpecs"][2]["URI"] = "rtsp://{}:8554/metis/ch3".format(IP)
    # CAM1、CAM2、CAM_IN 的 DeviceId基本已定,需修改的是IPC17.9.1 RecordSpecs Dynamic task configuration.py
    # print(json.dumps(data,indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('Director Push Test Pass!')
    else:
        print('Director Push Test Fail!')
        print(response.json())


if __name__ == '__main__':
    main()
