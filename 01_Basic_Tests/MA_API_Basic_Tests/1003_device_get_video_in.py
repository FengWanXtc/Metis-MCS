import sys
import os
import prettytable

sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["DeviceName", "DeviceId", "AliasName", "Default", "Algorithms"]
table.align = 'l'


def show_video_in():
    token = post_auth(username='admin', password='admin').headers['Token']
    # print(token)
    response = get_md_video_in(token)
    # print(response.json())
    if response.json()['Code'] == 200:
        print('\n' + 'Get Mediadevice video in success! ' + response.json()['Message'] + '\n')
    else:
        print('\n' + 'Get Mediadevice video in Fail! ')
        return False
    try:
        VideoIns = response.json()['VideoIns']
        for item in VideoIns:
            if "Algorithms" in item:
                table.add_row([item['DeviceName'], item['DeviceId'], item['AliasName'], item["Default"], item['Algorithms']])
            else:
                table.add_row([item['DeviceName'], item['DeviceId'], item["Default"], item['AliasName'], "None"])
    except:
        print('None VideoIns Device found!')
        return False
    print(table)


if __name__ == '__main__':
    show_video_in()
