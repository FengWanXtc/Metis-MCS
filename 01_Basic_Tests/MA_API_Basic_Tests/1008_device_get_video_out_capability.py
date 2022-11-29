import sys
import os
import prettytable
sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *
from prettytable import PrettyTable
from functionlib import *

table = PrettyTable()
table.field_names = ["DeviceId", "Width", "Height"]
table.align = 'l'  # 设置对齐


def show_video_out_capability_table():
    token = post_auth(username='admin',password='admin').headers['Token']
    response = get_md_video_out_capability(token)
    if response.json()['Code'] == 200:
        print('\n' + 'Get Mediadevice video out capability success!' + response.json()['Message'] + '\n')
    else:
        print('\n' + 'Get Mediadevice video out capability Fail!')
        return False

    VideoOuts = response.json()["VideoOuts"]
    for item in VideoOuts:
        table.add_row([item["DeviceId"], item["Width"], item["Height"]])
    print(table)


if __name__ == '__main__':
    show_video_out_capability_table()
