import sys
import os
import prettytable

sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *
from prettytable import PrettyTable

table = PrettyTable()
# table.field_names = ["DeviceName", "DeviceId", "AliasName", "Algorithms"]
table.field_names = ["DeviceName", "DeviceId", "AliasName", "Default"]
# All left aligned
table.align = 'l'


def show_get_video_out_table():
    token = post_auth(username='admin', password='admin').headers['Token']
    # print(token)
    response = get_md_video_out(token)
    # print(response.json())
    if response.json()['Code'] == 200:
        print('\n' + 'Get Mediadevice video out success! ' + response.json()['Message'] + '\n')
    else:
        print('\n' + 'Get Mediadevice video out Fail! ')
        return False
    try:
        VideoOuts = response.json()['VideoOuts']
        for VideoOut in VideoOuts:
            table.add_row([VideoOut['DeviceName'], VideoOut['DeviceId'], VideoOut['AliasName'], VideoOut["Default"]])

    # print(response.json()['AudioIns'])
    except:
        print('None VideoOuts Device found!')
        return False
    print(table)


if __name__ == '__main__':
    show_get_video_out_table()
