import argparse
import sys
sys.path.append('../../Libraries')
from mediadevicelib import *


def change_audio(IP, volume: str):
    data = {
        "DeviceId": "0103-0200",
        "Volume": int(volume)
    }
    response = post_md_audio_in_config(IP, data)
    if response.json()['Code'] == 200:
        print("Change Audio In Volume Pass!")
    else:
        print("Change Audio In Volume Fail!")
        print(response.json())


def main():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('--volume', '-v', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip
    VOLUME = args.volume
    change_audio(IP, VOLUME)


if __name__ == '__main__':
    main()

