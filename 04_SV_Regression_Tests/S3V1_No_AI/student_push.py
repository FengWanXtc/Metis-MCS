import sys
import argparse
sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def student_push(IP):
    data = read_json_file('student_push.json')

    # 获取DeviceId , 一般0是教师摄像头

    try:
        response = post_mt_create_update(ip=IP, data=data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Create Student Push Success')
        return True
    else:
        print('Create Student Push Fail')
        return False

def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 teacher_record_preview.py --device=0')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip
    student_push(IP)


if __name__ == '__main__':
    main()

