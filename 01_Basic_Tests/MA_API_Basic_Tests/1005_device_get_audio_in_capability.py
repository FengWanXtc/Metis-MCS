import sys
import os
import prettytable

sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *
from prettytable import PrettyTable

table = PrettyTable()
# table.field_names = ["DeviceName", "DeviceId", "AliasName", "Algorithms"]
table.field_names = ["DeviceId", "ChannelsRange", "SampleRateRange", "Formats", "Layouts", "Codecs"]
# All left aligned
# table.align = 'l'


def show_get_audio_in_cap_table():
    token = post_auth(username='admin', password='admin').headers['Token']
    # print(token)
    response = get_md_audio_in_capability(token)
    # print(response.json())
    if (response.json()['Code'] == 200):
        print('\n' + 'Get Mediadevice audio in capability success! ' + response.json()['Message'] + '\n')
    else:
        print('\n' + 'Get Mediadevice audio in capability Fail! ')
        return False
    try:
        AudioIns = response.json()['AudioIns']
        for Item in AudioIns:
            Formats = Item["Formats"]
            for F_item in Formats:
                if F_item == Formats[0]:
                    table.add_row([Item['DeviceId'], Item['ChannelsRange'], Item['SampleRateRange'],
                                   F_item, Item["Layouts"], response.json()["Codecs"]])

                else:
                    table.add_row(["", "", "", F_item, "", "", ""])

            table.add_row(["CurrentConfig", Item["CurrentConfig"]["Channels"], Item["CurrentConfig"]["SampleRate"],
                           Item["CurrentConfig"]["Format"], Item["CurrentConfig"]["Layout"], ""])

    except:
        print('None audio in capability was found!')
        return False
    print(table)


if __name__ == '__main__':
    show_get_audio_in_cap_table()
