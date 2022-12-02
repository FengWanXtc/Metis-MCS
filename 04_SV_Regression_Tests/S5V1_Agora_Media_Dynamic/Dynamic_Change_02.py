import argparse
import sys

sys.path.append('../../Libraries')
from environmentlib import *
from functionlib import *
from mediatasklib import *

VS = ['Student', 'Teacher', 'Director', 'Computer']


def mcs_task(host_ip, video_src):
    mcs_data = read_json_file('Dynamic_Change_02.json')
    task_name = get_mt_tasks(ip=host_ip).json()['Names'][0]
    mcs_data['Name'] = task_name

    if video_src in VS and video_src != "NULL":
        mcs_data['RtcStreamSpec']["VideoCodecName"] = "{}_h264_Codec".format(video_src)
    else:
        mcs_data['RtcStreamSpec']["VideoCodecName"] = "{}".format(video_src)

    print(json.dumps(mcs_data, indent=2))

    response = post_mt_create_update(ip=host_ip, data=mcs_data)
    if response.json()['Code'] == 201:
        print('Dynamic Change 02 MCS Post Success')
        return True
    else:
        print('Dynamic Change 02 MCS Post Fail')
        print(response.json())
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-vs', '--videoSrc', type=str, default='Student',
                        help='Record Video Source:Teacher,Student,etc')
    args = parser.parse_args()
    IP = args.ip
    VS = args.videoSrc
    mcs_task(IP, VS)
