import sys
import os
import prettytable
sys.path.append('../../libraries')
from authlib import *
from mediadevicelib import *
from prettytable import PrettyTable



def show_audio_in_table():
    table = PrettyTable()
    table.field_names = ["DeviceName", "DeviceId", "AliasName"]
    #All left aligned
    table.align = 'l'
    token = post_auth(username='admin',password='admin').headers['Token']
    #print(token)
    response = get_md_audio_in(token)
    if(response.json()['Code'] == 200):
        print('\n' + 'Get Mediadevice audio in success!' + response.json()['Message'] + '\n')
    else:
        print('\n' + 'Get Mediadevice audio in Fail!')
        return False
    try:    
        devicedict = response.json()['AudioIns']
        dictlen = len(devicedict)
        for i in range(0,dictlen):
            table.add_row([devicedict[i]['DeviceName'], devicedict[i]['DeviceId'], devicedict[i]["AliasName"]])
    #print(response.json()['AudioIns'])
    except:
        print('None AudioIns Device found!')
        return False
    print(table)
    
if __name__ == '__main__':
    Anno = "\n***********************************************************\n"
    input(Anno + "Please Insert Two Microphone and then Press Enter Key.")
    show_audio_in_table()
    input(Anno + "Please Unplug ALL Microphones and then Press Enter Key.")
    show_audio_in_table()
    input(Anno + "Please Insert One Microphones and then Press Enter Key.")
    show_audio_in_table()