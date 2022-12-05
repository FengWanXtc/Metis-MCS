import sys
import argparse

sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *
from mediadevicelib import *

GeneralCamType = Global_GeneralCamType


def create_remote():
    parser = argparse.ArgumentParser(
        description='usage: python3 student_create_remote.py -ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The ip of the host pc which push camera stream')
    parser.add_argument('-logfile', type=str, default=None, help='LogFile Name')
    args = parser.parse_args()
    IP = args.ip
    LOGFILE = args.logfile

    if LOGFILE is not None:
        # 此步骤是设置LogFile
        environmentlib.Whether_Log_File = True
        environmentlib.modify_cfg("FileName", LOGFILE)
    cre_rem_data = read_json_file('student_create_remote.json')
    VideoIns = get_md_video_in(ip=IP).json()['VideoIns']

    for VideoIn in VideoIns:
        if VideoIn["DeviceName"].find(GeneralCamType) != -1:
            Student_DeviceId = VideoIn['DeviceId']
            break

    cre_rem_data['VideoSpecs'][0]['DeviceId'] = Student_DeviceId
    # print(json.dumps(cre_rem_data, indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=cre_rem_data)
    except:
        print('Post Create Task Failed.')
        print(response.json())

    if response.json()['Code'] == 201:
        print('S1E1 Student Test Pass!')
    else:
        print('S1E1 Student Test Fail!')
        print(json.dumps(cre_rem_data, indent=2))
        print(response.json())
        return response.json()


if __name__ == '__main__':
    create_remote()
