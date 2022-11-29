import sys
import os
import prettytable

sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["DeviceName", "DeviceId", "AliasName", "Default"]

# All left aligned
table.align = 'l'


def show_audio_in_table():
    token = post_auth(username='admin', password='admin').headers['Token']
    # print(token)
    response = get_md_audio_in(token)
    if response.json()['Code'] == 200:
        print('\n' + 'Get Mediadevice audio in success! ' + response.json()['Message'] + '\n')
    else:
        print('\n' + 'Get Mediadevice audio in Fail! ')
        return False
    try:
        AudioIns = response.json()['AudioIns']
        for AudioIn in AudioIns:
            table.add_row((AudioIn['DeviceName'], AudioIn['DeviceId'], AudioIn['AliasName'], AudioIn['Default']))
        # print(response.json()['AudioIns'])
        # 先打印总表
        print(table, "\n")

        for AudioIn in AudioIns:
            # 如果有从设备,就再打印一张表
            if "SubDevices" in AudioIn:
                print("< {} > Has SubDevices. List As Follow: ".format(AudioIn['DeviceName']))
                Sub_table = PrettyTable()
                Sub_table.field_names = ["Id", "Name", "Alias"]
                # All left aligned
                Sub_table.align = 'l'
                for SubDevice in AudioIn['SubDevices']:
                    Sub_table.add_row((SubDevice['Id'], SubDevice['Name'], SubDevice['Alias']))
                print(Sub_table)
    except:
        print('None AudioIns Device found!')
        return False


if __name__ == '__main__':
    show_audio_in_table()
