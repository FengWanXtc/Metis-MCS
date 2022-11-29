import sys
import os
import prettytable
sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *
from prettytable import PrettyTable


def show_audio_out_table():
    table = PrettyTable()
    table.field_names = ["DeviceName", "DeviceId", "AliasName"]
    #All left aligned
    table.align = 'l'
    token = post_auth(username='admin',password='admin').headers['Token']
    #print(token)
    response = get_md_audio_out(token)
    if(response.json()['Code'] == 200):
        print('\n' + 'Get Mediadevice audio out success!' + response.json()['Message'] + '\n')
    else:
        print('\n' + 'Get Mediadevice audio out Fail!')
        return False
    devicedict = response.json()['AudioOuts']
    #print(response.json()['AudioIns'])
    dictlen = len(devicedict)
    for i in range(0,dictlen):
        table.add_row([devicedict[i]['DeviceName'],devicedict[i]['DeviceId'], devicedict[i]["AliasName"]])
    print(table)
    
if __name__ == '__main__':
    Anno = "\n***********************************************************\n"
    input(Anno + "Please Insert Speaker and then Press Enter Key.")
    show_audio_out_table()
    input(Anno + "Please Unplug Speaker and then Press Enter Key.")
    show_audio_out_table()