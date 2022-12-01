import argparse
import sys

sys.path.append('../../Libraries')
from environmentlib import *
from functionlib import *
from mediatasklib import *


def mcs_task(host_ip):
    mcs_data = read_json_file('Dynamic_Change_02.json')
    print(json.dumps(mcs_data, indent=2))

    response = post_mt_create_update(ip=host_ip, data=mcs_data)
    if response.json()['Code'] == 201:
        print('Dynamic Change 02 MCS Post Success')
        return True
    else:
        print('Dynamic Change 02 MCS Post Fail')
        print(response.json())
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip
    mcs_task(IP)
