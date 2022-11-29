import sys
import os
import prettytable

sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *
from prettytable import PrettyTable

table = PrettyTable()
# table.field_names = ["DeviceName", "DeviceId", "AliasName", "Algorithms"]
table.field_names = ["DeviceId", "Background"]
# All left aligned
table.align = 'l'


def show_get_video_out_background_table():
    token = post_auth(username='admin', password='admin').headers['Token']
    # print(token)
    response = get_md_video_out_background(token)
    # print(response.json())
    if (response.json()['Code'] == 200):
        print('\n' + 'Get video out background success! ' + response.json()['Message'] + '\n')
    else:
        print('\n' + 'Get video out background in Fail! ')
        return False
    try:
        devicedict = response.json()['VideoOuts']
        dictlen = len(devicedict)
        for i in range(0, dictlen):
            table.add_row([devicedict[i]['DeviceId'], devicedict[i]['Background']])
    except:
        print('None result was found!')
        return False
    print(table)


if __name__ == '__main__':
    show_get_video_out_background_table()
