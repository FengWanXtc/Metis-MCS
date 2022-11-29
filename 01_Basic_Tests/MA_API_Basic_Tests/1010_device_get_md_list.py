import sys
sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *
from prettytable import PrettyTable

SplitLine = "\n\n******************************************* Split Line **********************************************\n"


def show_list():
    token = post_auth(username='admin', password='admin').headers['Token']
    response = get_md_list(token, "10.12.224.140")
    if response.json()['Code'] == 200:
        print('\n' + 'Get Device List success!' + response.json()['Message'] + '\n')
    else:
        print('\n' + 'Get  Device List Volume Fail!')
        return False
    # 获取list里的4个列表

    AudioIns = response.json()['AudioIns']
    AudioOuts = response.json()['AudioOuts']
    VideoOuts = response.json()['VideoOuts']
    VideoIns = response.json()['VideoIns']

    # 对AudioIns进行处理，同理对其他内容进行处理
    if AudioIns is not None:
        AudioInsTable = PrettyTable()
        AudioInsTable.field_names = ["DeviceName", "DeviceId", "AliasName", "Default"]
        AudioInsTable.align = 'l'
        for AudioIn in AudioIns:
            AudioInsTable.add_row((AudioIn['DeviceName'], AudioIn['DeviceId'], AudioIn['AliasName'], AudioIn['Default']))
        # print(response.json()['AudioIns'])
        # 先打印总表
        print("Audio In Devices As Follow.")
        print(AudioInsTable, "\n")
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
                print(Sub_table, SplitLine)

    # 对AudioOuts进行处理，同理对其他内容进行处理
    if AudioOuts is not None:
        AudioOutsTable = PrettyTable()
        AudioOutsTable.field_names = ["DeviceName", "DeviceId", "AliasName", "Default"]
        AudioOutsTable.align = 'l'
        for AudioOut in AudioOuts:
            AudioOutsTable.add_row((AudioOut['DeviceName'], AudioOut['DeviceId'], AudioOut['AliasName'], AudioOut['Default']))
        print("Audio Out Devices As Follow.")
        print(AudioOutsTable, "\n")
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
                print(Sub_table, SplitLine)

        # 对VideoIns进行处理，同理对其他内容进行处理
        if VideoIns is not None:
            VideoInsTable = PrettyTable()
            VideoInsTable.field_names = ["DeviceName", "DeviceId", "AliasName", "Default", "Algorithms"]
            VideoInsTable.align = 'l'
            for VideoIn in VideoIns:
                if "Algorithms" in VideoIn:
                    VideoInsTable.add_row([VideoIn['DeviceName'], VideoIn['DeviceId'], VideoIn['AliasName'], VideoIn["Default"], VideoIn['Algorithms']])
                else:
                    VideoInsTable.add_row([VideoIn['DeviceName'], VideoIn['DeviceId'], VideoIn["Default"], VideoIn['AliasName'], "None"])
            print("Video In Devices As Follow.")
            print(VideoInsTable, SplitLine)

        # 对VideoOuts进行处理，同理对其他内容进行处理
        if VideoOuts is not None:
            VideoOutsTable = PrettyTable()
            VideoOutsTable.field_names = ["DeviceName", "DeviceId", "AliasName", "Default"]
            VideoOutsTable.align = 'l'
            for VideoOut in VideoOuts:
                VideoOutsTable.add_row(
                    [VideoOut['DeviceName'], VideoOut['DeviceId'], VideoOut['AliasName'], VideoOut["Default"]])
            print("Video Out Devices As Follow.")
            print(VideoOutsTable)


if __name__ == '__main__':
    show_list()
