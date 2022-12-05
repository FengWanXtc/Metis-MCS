import argparse
import sys
sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *

TeacherCamType = Global_TeacherCamType
StudentCamType = Global_StudentCamType


def S1E2_test():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-TCam', type=str, default=TeacherCamType, help='The Teacher Cam Type')
    parser.add_argument('-SCam', type=str, default=StudentCamType, help='The Student Cam Type')
    parser.add_argument('-rtsp', type=str, default="rtsp://10.12.224.57/ch2", help='IPC camera as CodecStream Source.')
    parser.add_argument('-logfile', type=str, default=None, help='LogFile Name')

    args = parser.parse_args()
    IP = args.ip
    SCAM = args.SCam
    TCAM = args.TCam
    RTSP = args.rtsp
    LOGFILE = args.logfile

    if LOGFILE is not None:
        # 此步骤是设置LogFile
        environmentlib.Whether_Log_File = True
        environmentlib.modify_cfg("FileName", LOGFILE)

    S1E2_data = read_json_file('4F-4.1DR-4.2T-4.3S-4.4RC.json')
    # print(json.dumps(S1E2_data, indent=2))
    Teacher_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=TCAM, aiStrategy='teacher')
    S1E2_data['VideoSpecs'][0]['DeviceId'] = Teacher_DeviceId
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=SCAM, aiStrategy='student')
    S1E2_data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    S1E2_data['CodecStreamSpecs'][0]['URI'] = RTSP

    try:
        response = post_mt_create_update(ip=IP, data=S1E2_data)
    except:
        print('Post Create Task Failed')
        print(response.status_code)
        return False

    if response.json()['Code'] == 201:
        print('S1E2 Test Success')
        return True
    else:
        print('S1E2 Test Fail')
        print(response.json())
        print(json.dumps(S1E2_data, indent=2))
        return response.json()


if __name__ == '__main__':
    S1E2_test()
