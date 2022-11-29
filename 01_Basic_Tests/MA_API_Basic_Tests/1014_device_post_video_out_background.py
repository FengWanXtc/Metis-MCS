import requests
import json
import os
import sys
import argparse

sys.path.append('../../Libraries')
from authlib import *
from mediatasklib import *
from functionlib import *
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


def create_UI(bg):
    TOKEN = post_auth(username='admin', password='admin').headers['Token']
    # get video out DeviceId and set for post request
    databody["DeviceId"] = get_background_DeviceId()
    if bg == "null":
        databody["Background"] = "null"
    elif bg == "":
        databody["Background"] = ""
    elif bg == "jpg":
        databody["Background"] = "/usr/share/backgrounds/buka_wallpaper_4k.jpg"
    elif bg == "png":
        databody["Background"] = "/usr/share/backgrounds/NVIDIA_Login_Logo.png"

    response = post_md_background(TOKEN, databody)

    if response.json()['Code'] == 200:
        print('Crete Background Pass!')
    else:
        print('Crete Background Fail!')


def main():
    parser = argparse.ArgumentParser(description='usage: python3 1014_.......py -bg=jpg ')
    parser.add_argument('-bg', type=str, default="null", help='The type of the background.')
    args = parser.parse_args()
    BG = args.bg
    create_UI(BG)


if __name__ == '__main__':
    main()
