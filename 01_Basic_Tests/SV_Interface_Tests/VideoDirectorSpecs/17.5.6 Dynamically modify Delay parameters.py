import sys
import argparse

sys.path.append('../../../libraries')
from mediatasklib import *
from functionlib import *


def create_preview(IP, mcsname ):
    IP = input("Please Input Metis IP: ")
    cre_data = read_json_file('17.5.6 Dynamically modify Delay parameters.json')
    cre_data["Name"] = mcsname
    try:
        response = post_mt_create_update(ip=IP, data=cre_data)
    except:
        print('Post Create Task Failed')
        print(response.json())

    if (response.json()['Code'] == 201):
        print('Create preview Success')
        return True
    else:
        print('Create preview Fail')
        return False


def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 create_one_frame_preview.py --name=Teacher --frame_number=1')
    parser.add_argument('--mcsname', '-t', type=str, default='mcs0.3', help='The name of the mcstask')
    parser.add_argument('-ip', type=str, default='', help='The IP Address')

    args = parser.parse_args()
    IP = args.ip
    MCSNAME = args.mcsname

    create_preview(IP, MCSNAME)


if __name__ == '__main__':
    main()
