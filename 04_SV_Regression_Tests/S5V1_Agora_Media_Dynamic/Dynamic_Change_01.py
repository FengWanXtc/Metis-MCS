import argparse
import sys

sys.path.append('../../Libraries')
from environmentlib import *
from functionlib import *
from mediatasklib import *
from mediadevicelib import *

AS = ["Mic", "PC"]


def mcs_task(host_ip, audio_src):
    mcs_data = read_json_file('Dynamic_Change_01.json')

    task_name = get_mt_tasks(ip=host_ip).json()['Names'][0]
    mcs_data['Name'] = task_name

    if audio_src in AS and audio_src != "NULL":
        mcs_data['RtcStreamSpec']["AudioCodecName"] = "Audio{}_pcm_Codec".format(audio_src)
    else:
        mcs_data['RtcStreamSpec']["AudioCodecName"] = "{}".format(audio_src)

    print(json.dumps(mcs_data, indent=2))
    try:
        response = post_mt_create_update(ip=host_ip, data=mcs_data)
    except:
        print('Post Create Task Failed')
        print(response.status_code)
        return False

    if response.json()['Code'] == 201:
        print('Dynamic Change 01 MCS Success')
        return True
    else:
        print('Dynamic Change 01 MCS Fail')
        print(response.json())
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-as', '--audioSrc', type=str, default='Mic', help='Record Audio Source:Mic,PC')
    args = parser.parse_args()
    IP = args.ip
    AUDIOSRC = args.audioSrc
    mcs_task(IP, AUDIOSRC)
