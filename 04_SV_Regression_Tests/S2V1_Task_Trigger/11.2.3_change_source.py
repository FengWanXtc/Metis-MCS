import sys
import argparse

sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *

TeacherCamType = Global_TeacherCamType
StudentCamType = Global_StudentCamType


def main():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip

    MCS_data = read_json_file('11.2.3_change_source.json')
    # print(json.dumps(S1E2_data, indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=MCS_data)
    except RuntimeError:
        print('Post Create Task Failed')
        print(response.status_code)
        return False

    if response.json()['Code'] == 201:
        print('S2V1 Case 3:Change Source Test Success')
        return True
    else:
        print('S2V1 Case 3:Change Source Test Fail')
        print(response.json())
        return False


if __name__ == '__main__':
    main()
