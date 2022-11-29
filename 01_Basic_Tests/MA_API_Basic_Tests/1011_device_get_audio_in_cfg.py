import sys
sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["DeviceId", "Volume", "Mute", "LocalAmplification"]
table.align = 'l'
table.align["Volume"] = 'c'
table.align["LocalAmplification"] = 'c'


def show_audio_in_cfg():
    token = post_auth(username='admin', password='admin').headers['Token']
    response = get_md_audio_in_cfg(token)

    if response.json()['Code'] == 200:
        print('\n' + 'Get audio in configuration success! ' + response.json()['Message'] + '\n')
    else:
        print('\n' + 'Get audio in configuration Fail! ')
        return False
    try:
        AudioIns = response.json()['AudioIns']
        for AudioIn in AudioIns:
            table.add_row((AudioIn['DeviceId'], AudioIn['Volume'], AudioIn['Mute'], AudioIn['LocalAmplification']))
        print(table, "\n")
        for AudioIn in AudioIns:
            # 如果有从设备,就再打印一张表
            if "SubDevices" in AudioIn:
                print("DeviceId < {} > Has SubDevices. List As Follow: ".format(AudioIn['DeviceId']))
                Sub_table = PrettyTable()
                Sub_table.field_names = ["Id", "Volume", "Mute"]
                # All left aligned
                Sub_table.align = 'l'
                Sub_table.align['Volume'] = 'c'
                for SubDevice in AudioIn['SubDevices']:
                    Sub_table.add_row((SubDevice['Id'], SubDevice['Volume'], SubDevice['Mute']))
                print(Sub_table)
    except:
        print('None result was found!')
        return False


if __name__ == '__main__':
    show_audio_in_cfg()
