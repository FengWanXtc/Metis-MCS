import argparse
import sys

sys.path.append('../../Libraries')
from functionlib import *
from mediatasklib import *


def rtc_dynamic(task_name, host_ip):
    Dynamic_Rtc_MCS = read_json_file('RtcStreamDynamic.json')
    Dynamic_Rtc_MCS['Name'] = task_name
    Dynamic_Rtc_MCS["RtcStreamSpec"]["VideoCodecName"] = "Director_h265_Codec"
    response = post_mt_create_update(ip=host_ip, data=Dynamic_Rtc_MCS)
    if response.json()['Code'] == 201:
        input("动态修改MCS下发成功，检查效果后按回车进行下一个步骤 :: 删除两端任务，结束该Case测试")
    else:
        print(response.json())
        raise UserWarning("创建任务失败，请检查环境")


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
            "创建两端任务成功,按回车进行下一个步骤 :: 近端动态变换RtcStreamSpec推流端视频，由H264 4mbps VBR 导播路改为推送H265 1mbps CBR PC路")
    else:
        print(Judge_1)
        print(Judge_2)
        raise UserWarning("创建任务失败，请检查环境")

    task_name = get_mt_tasks(ip=IP).json()['Names'][0]
    # 对MCS进行动态修改
    rtc_dynamic(task_name, Near_IP)
    os.system('python delete_all_tasks.py -ip={}'.format(Near_IP))
    os.system('python delete_all_tasks.py -ip={}'.format(Far_IP))


if __name__ == '__main__':
    main()
