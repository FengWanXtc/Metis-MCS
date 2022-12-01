import argparse
import sys

sys.path.append('../../Libraries')
from environmentlib import *
from functionlib import *
from mediatasklib import *
from mediadevicelib import *


def mcs_task(Host, TCam, SCam):
    mcs_data = read_json_file('Dynamic_Change_01.json')
    print(json.dumps(mcs_data, indent=2))

    try:
        response = post_mt_create_update(ip=Host, data=mcs_data)
    except:
        print('Post Create Task Failed')
        print(response.status_code)
        return False

    if response.json()['Code'] == 201:
        print('Dynamic Change 01 MCS Success')
        return True
    else:
        print('Dynamic Change 01 MCS Fail')
        print(response.json())
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-TCam', type=str, default=Global_TeacherCamType, help='The Teacher Cam Type')
    parser.add_argument('-SCam', type=str, default=Global_StudentCamType, help='The Student Cam Type')
    args = parser.parse_args()
    IP = args.ip
    SCAM = args.SCam
    TCAM = args.TCam

    mcs_task(IP, TCAM, SCAM)
