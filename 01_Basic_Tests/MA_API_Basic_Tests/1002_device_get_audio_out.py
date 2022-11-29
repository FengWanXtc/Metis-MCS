import sys

sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["DeviceName", "DeviceId", "AliasName", "Default"]
# All left aligned
table.align = 'l'


def show_audio_out_table():
    token = post_auth(username='admin', password='admin').headers['Token']
    # print(token)
    response = get_md_audio_out(token)
    if response.json()['Code'] == 200:
        print('\n' + 'Get Mediadevice audio out success! ' + response.json()['Message'] + '\n')
    else:
        print('\n' + 'Get Mediadevice audio out Fail! ')
        return False
    AudioOuts = response.json()['AudioOuts']
    for AudioOut in AudioOuts:
        table.add_row((AudioOut['DeviceName'], AudioOut['DeviceId'], AudioOut['AliasName'], AudioOut['Default']))
    print(table, "\n")

    for AudioOut in AudioOuts:
        # 如果有从设备,就再打印一张表
        if "SubDevices" in AudioOut:
            print("< {} > Has SubDevices. List As Follow: ".format(AudioOut['DeviceName']))
            Sub_table = PrettyTable()
            Sub_table.field_names = ["Id", "Name", "Alias"]
            # All left aligned
            Sub_table.align = 'l'
            for SubDevice in AudioOut['SubDevices']:
                Sub_table.add_row((SubDevice['Id'], SubDevice['Name'], SubDevice['Alias']))
            print(Sub_table)


if __name__ == '__main__':
    show_audio_out_table()
