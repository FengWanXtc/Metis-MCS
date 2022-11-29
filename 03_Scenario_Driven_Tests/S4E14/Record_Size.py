import argparse
import json
import sys
import time

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *


def basic():
    # 设置对应的MCS
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('--unit', '-u', type=int, default=10485760, help='The Split Unit (Bytes)')
    parser.add_argument('--recordTime', '-rt', type=int, default=10, help='The Record Time')
    parser.add_argument('--fileName', '-fn', type=str, default="Temp", help='The Record Time')
    args = parser.parse_args()
    IP = args.ip
    UNIT = args.unit
    RECORDTIME = args.recordTime
    FILENAME = args.fileName

    data = read_json_file('Record_Size.json')
    data['RecordSpecs'][0]['SplitUnit'] = UNIT
    data['RecordSpecs'][0]['Path'] = "WP4_SizeSplit_{}_yyyy-mm-dd-hh-mm-ss.mp4".format(str(FILENAME))
    # print(json.dumps(data,indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=data)
        # print(response.url)
        print("Start Recording File, {} Seconds later will destroy Task. Then check record files.".format(str(RECORDTIME)))
        time.sleep(RECORDTIME)
        os.system('python delete_all_tasks.py -ip={}'.format(IP))

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('Record Split By Size Test Pass!')
    else:
        print('Record Split By Size Test Fail!')
        print(response.json())


if __name__ == '__main__':
    basic()
