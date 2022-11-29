import sys
import os
import prettytable

sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *
from prettytable import PrettyTable
from functionlib import *

code_table = PrettyTable()
detail_table = PrettyTable()

code_table.field_names = ["Codecs"]
detail_table.field_names = ["DeviceId", "FormatSet", "[ Format", "ResolutionSet", "[ Width", "Height", "FrameRate ] ]"]
# All left aligned
detail_table.vertical_char = "|"  # 控制竖边框


def show_get_video_in_cap_table():
    token = post_auth(username='admin', password='admin').headers['Token']
    # print(token)
    response = get_md_video_in_capability(token)

    # print(response.json())
    if response.json()['Code'] == 200:
        print('\n' + 'Get Mediadevice video in capability success! ' + response.json()['Message'] + '\n')
    else:
        print('\n' + 'Get Mediadevice video in capability Fail! ')
        return False

    code_table.add_row([response.json()["Codecs"]])
    # 先打印Codecs
    # 随后打印详细内容

    VideoIns = response.json()["VideoIns"]
    for item in VideoIns:
        FormatItem = item["FormatSet"]  # 存在多种FormatSet，所以需要多段遍历
        for format_item in FormatItem:
            ResolutionItem = format_item["ResolutionSet"]
            for resolution_item in ResolutionItem:
                if resolution_item == ResolutionItem[0] and format_item == FormatItem[0]:  # 自底向上减少判断
                    detail_table.add_row(
                        [item['DeviceId'], "", format_item["Format"], "",
                         resolution_item["Width"], resolution_item["Height"], resolution_item["FrameRate"]])
                    # 如果是VideoIns第一个则打印全部内容，否则不打印Device，Format
                elif resolution_item == ResolutionItem[0] and format_item != FormatItem[0]:
                    detail_table.add_row(["", "", format_item["Format"], "",  resolution_item["Width"],
                                          resolution_item["Height"], resolution_item["FrameRate"]])
                    # 如果是Format第一个则做相应处理
                else:
                    detail_table.add_row(["", "", "", "", resolution_item["Width"],
                                          resolution_item["Height"], resolution_item["FrameRate"]])
                    # 如果都不是做其他处理

        # detail_table.add_row([item['DeviceId'], ])
    print(code_table)
    print(detail_table)

if __name__ == '__main__':
    show_get_video_in_cap_table()

