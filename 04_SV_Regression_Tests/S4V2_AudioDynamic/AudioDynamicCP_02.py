import argparse
import sys
sys.path.append('../../Libraries')
from environmentlib import *
from functionlib import *
from mediatasklib import *
from mediadevicelib import *


def mcs_task(Host):
    mcs_data = read_json_file('AudioDynamicCP_02.json')
    AudioIns = get_md_audio_in(ip=Host).json()['AudioIns']

    try:
        response = post_mt_create_update(ip=Host, data=mcs_data)
    except:
        print('Post Create Task Failed')
        print(response.status_code)
        return False

    if response.json()['Code'] == 201:
        print('AudioDynamicCP 01 Test Success')
        return True
    else:
        print('AudioDynamicCP 01 Test Fail')
        print(response.json())
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip
    mcs_task(IP)
