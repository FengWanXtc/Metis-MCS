import sys

sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["DeviceId", "Volume", "Mute"]
table.align = 'l'
table.align["Volume"] = 'c'


def show_audio_out_cfg():
    token = post_auth(username='admin', password='admin').headers['Token']
    response = get_md_audio_out_cfg(token)

    if response.json()['Code'] == 200:
        print('\n' + 'Get audio out configuration success! ' + response.json()['Message'] + '\n')
    else:
        print('\n' + 'Get audio out configuration Fail! ')
        return False
    try:
        AudioOuts = response.json()['AudioOuts']
        for AudioOut in AudioOuts:
            table.add_row((AudioOut['DeviceId'], AudioOut['Volume'], AudioOut['Mute']))
        print(table, "\n")
        for AudioOut in AudioOuts:
            # 如果有从设备,就再打印一张表
            if "SubDevices" in AudioOut:
                print("DeviceId < {} > Has SubDevices. List As Follow: ".format(AudioOut['DeviceId']))
                Sub_table = PrettyTable()
                Sub_table.field_names = ["Id", "Volume", "Mute"]
                # All left aligned
                Sub_table.align = 'l'
                Sub_table.align['Volume'] = 'c'
                for SubDevice in AudioOut['SubDevices']:
                    Sub_table.add_row((SubDevice['Id'], SubDevice['Volume'], SubDevice['Mute']))
                print(Sub_table)
    except:
        print('None result was found!')
        return False

if __name__ == '__main__':
    show_audio_out_cfg()
