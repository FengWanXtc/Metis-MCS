import argparse
import os
import sys
import time

sys.path.append('../../Libraries')
from mediatasklib import *
from functionlib import *
from environmentlib import *

def Record(IP):
    databody = read_json_file('AI_6_record_TS.json')
    try:
        response = post_mt_create_update(ip=IP, data=databody)
        # print(response.url)

    except:
        print('Post Create Task Failed.')
        print(response)

    if response.json()['Code'] == 201:
        print('AI_6 Record(T+S) Test Pass!')
    else:
        print('AI_6 Record(T+S) Test Fail!')
        print(response.json())


def main():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip
    os.system("python AI_3_audio.py -ip={}".format(IP))
    time.sleep(5)
    print("Create Record Task")
    Record(IP)


if __name__ == '__main__':
    main()
