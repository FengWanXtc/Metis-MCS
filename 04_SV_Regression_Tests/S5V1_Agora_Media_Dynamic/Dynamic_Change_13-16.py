import argparse
import sys

sys.path.append('../../Libraries')
from functionlib import *
from mediatasklib import *


def post_announce(host_ip, mcs_data, announce):
    response = post_mt_create_update(ip=host_ip, data=mcs_data)
    if response.json()['Code'] == 201:
        input(announce)
    else:
        print(response.json())
        raise UserWarning("创建任务失败，请检查环境")


def rtc_dynamic(task_name, host_ip):
    Dynamic_Rtc_MCS = read_json_file('ComposeBasic.json')
    Dynamic_Rtc_MCS['Name'] = task_name
    post_announce(host_ip=host_ip, mcs_data=Dynamic_Rtc_MCS,
                  announce='Compose画中画MCS下发成功，检查效果后按回车进行下一个步骤 :: 动态推送本地画中画+PC音频')

    Dynamic_Rtc_MCS = read_json_file('RtcStreamDynamic.json')
    Dynamic_Rtc_MCS['Name'] = task_name
    Dynamic_Rtc_MCS['RtcStreamSpec']['VideoCodecName'] = 'Compositor_h264_Codec'
    post_announce(host_ip=host_ip, mcs_data=Dynamic_Rtc_MCS,
                  announce="动态推送MCS下发成功，检查效果后按回车进行下一个步骤 :: 动态修改ComposeSpec,画中画改为教师+学生")

    Dynamic_Rtc_MCS = read_json_file('ComposeDynamic_PIP.json')
    Dynamic_Rtc_MCS['Name'] = task_name
    post_announce(host_ip=host_ip, mcs_data=Dynamic_Rtc_MCS,
                  announce="修改画中画MCS下发成功，检查效果后按回车进行下一个步骤 :: 动态修改ComposeSpec,画中画改为导播+PC")

    Dynamic_Rtc_MCS['VideoComposeSpecs'][0]['CompositionSpec'][0]['SourceName'] = 'Director'
    Dynamic_Rtc_MCS['VideoComposeSpecs'][0]['CompositionSpec'][1]['SourceName'] = 'Computer'
    post_announce(host_ip=host_ip, mcs_data=Dynamic_Rtc_MCS,
                  announce="修改画中画MCS下发成功，检查效果后按回车进行下一个步骤 :: 动态修改ComposeSpec,画中画改为二分屏")

    Dynamic_Rtc_MCS['VideoComposeSpecs'][0]['CompositionSpec'][0]['Geometry'] = [0, 270, 960, 540]
    Dynamic_Rtc_MCS['VideoComposeSpecs'][0]['CompositionSpec'][1]['Geometry'] = [960, 270, 960, 540]
    post_announce(host_ip=host_ip, mcs_data=Dynamic_Rtc_MCS,
                  announce="二分屏MCS下发成功，检查效果后按回车进行下一个步骤 :: 动态修改二分屏为老师+PC")

    Dynamic_Rtc_MCS['VideoComposeSpecs'][0]['CompositionSpec'][0]['SourceName'] = 'Teacher'
    post_announce(host_ip=host_ip, mcs_data=Dynamic_Rtc_MCS,
                  announce="二分屏MCS下发成功，检查效果后按回车进行下一个步骤 :: 动态修改为1+3模式")

    Dynamic_Rtc_MCS = read_json_file('ComposeDynamic(1+3).json')
    Dynamic_Rtc_MCS['Name'] = task_name
    post_announce(host_ip=host_ip, mcs_data=Dynamic_Rtc_MCS,
                  announce="Compose(1+3)模式下发成功，检查效果后按回车进行下一个步骤 :: 修改1+3宫格内部位置")

    Dynamic_Rtc_MCS['VideoComposeSpecs'][0]['CompositionSpec'][0]['SourceName'] = 'Teacher'
    Dynamic_Rtc_MCS['VideoComposeSpecs'][0]['CompositionSpec'][1]['SourceName'] = 'Director'
    Dynamic_Rtc_MCS['VideoComposeSpecs'][0]['CompositionSpec'][2]['SourceName'] = 'Computer'
    Dynamic_Rtc_MCS['VideoComposeSpecs'][0]['CompositionSpec'][3]['SourceName'] = 'Student'
    post_announce(host_ip=host_ip, mcs_data=Dynamic_Rtc_MCS,
                  announce="修改Compose内部宫格位置下发成功，检查效果后按回车进行下一个步骤 :: 对Compose路进行Transform并且为第一宫格回显")

    Dynamic_Rtc_MCS = read_json_file('TransformBasic.json')
    Dynamic_Rtc_MCS['Name'] = task_name
    post_announce(host_ip=host_ip, mcs_data=Dynamic_Rtc_MCS,
                  announce="Transform修改分辨率1080P MCS下发成功，检查效果后按回车进行下一个步骤 :: 动态推流TransformSpec")

    Dynamic_Rtc_MCS = read_json_file('RtcStreamDynamic.json')
    Dynamic_Rtc_MCS['Name'] = task_name
    Dynamic_Rtc_MCS['RtcStreamSpec']['VideoCodecName'] = 'VideoTransform_Codec'
    post_announce(host_ip=host_ip, mcs_data=Dynamic_Rtc_MCS,
                  announce="动态推流TransformSpec MCS下发成功，检查效果后按回车进行下一个步骤 :: 动态推流720P分辨率，查看远端效果")

    Dynamic_Rtc_MCS['RtcStreamSpec']['VideoCodecName'] = 'VideoTransform_720_Codec'
    post_announce(host_ip=host_ip, mcs_data=Dynamic_Rtc_MCS,
                  announce="动态推流720P MCS下发成功，检查效果后按回车进行下一个步骤 :: 动态推流480P分辨率，查看远端效果")

    Dynamic_Rtc_MCS['RtcStreamSpec']['VideoCodecName'] = 'VideoTransform_480_Codec'
    post_announce(host_ip=host_ip, mcs_data=Dynamic_Rtc_MCS,
                  announce="动态推流480P MCS下发成功，检查效果后按回车进行下一个步骤 :: 删除两端任务")
def main():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip



    Near_IP = input("请输入近端小站IP地址: ")
    Far_IP = input("请输入远端小站IP地址: ")
    Judge_1 = os.popen('python Agora_Basic.py -ip={}'.format(Near_IP)).read()
    Judge_2 = os.popen('python Agora_Far.py -ip={}'.format(Far_IP)).read()
    if (Judge_1 + Judge_2).find("Fail") == -1:
        input(
            "创建两端任务成功,按回车进行下一个步骤 :: 创建Compose画中画，回显第一宫格切换为画中画")
    else:
        print(Judge_1)
        print(Judge_2)
        raise UserWarning("创建任务失败，请检查环境")

    # 对MCS进行动态修改
    task_name = get_mt_tasks(ip=IP).json()['Names'][0]
    rtc_dynamic(task_name, Near_IP)
    os.system('python delete_all_tasks.py -ip={}'.format(Near_IP))
    os.system('python delete_all_tasks.py -ip={}'.format(Far_IP))


if __name__ == '__main__':
    main()
