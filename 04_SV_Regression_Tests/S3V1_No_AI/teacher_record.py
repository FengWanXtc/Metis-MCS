import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def teacher_record(IP):
    tea_re_data = read_json_file('teacher_record.json')

    # 获取DeviceId , 一般0是教师摄像头

    try:
        response = post_mt_create_update(ip=IP, data=tea_re_data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Create Teacher Record Success')
        return True
    else:
        print('Create Teacher Record Fail')
        return False

def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 teacher_record_preview.py --device=0')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip
    teacher_record(IP)


if __name__ == '__main__':
    main()

