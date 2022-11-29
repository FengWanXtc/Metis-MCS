import sys
import argparse
sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *

databody = {
    "DeviceId": "",
    "Background": "/home/user/EST/MCSScripts/background.png"
}


def get_background_DeviceId():
    token = post_auth(username='admin', password='admin').headers['Token']
    response = get_md_video_out_background(token)
    if response.json()['Code'] != 200:
        print('Get video out background in Fail!')
        return False
    DeviceId = response.json()["VideoOuts"][0]["DeviceId"]
    return DeviceId


def create_UI(TYPE):
    TOKEN = post_auth(username='admin', password='admin').headers['Token']
    # get video out DeviceId and set for post request
    databody["DeviceId"] = get_background_DeviceId()
    if TYPE == 'null':
        databody["Background"] = "null"
    elif TYPE == 'png':
        databody["Background"] = "/home/user/EST/MCSScripts/background.png"

    elif TYPE == 'jpg':
        databody["Background"] = "/home/user/EST/MCSScripts/bgjpg.jpg"
    response = post_md_background(TOKEN, databody)

    if response.json()['Code'] == 200:
        print('Create Background Pass!')
    else:
        print('Create Background Fail!')


def main():
    parser = argparse.ArgumentParser(description='usage: python3 create_UI.py --type=null ')
    parser.add_argument('--type', '-t', type=str, default='null', help='whether the background is null')
    args = parser.parse_args()
    TYPE = args.type
    create_UI(TYPE)


if __name__ == '__main__':
    main()
