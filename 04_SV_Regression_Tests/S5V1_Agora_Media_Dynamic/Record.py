import argparse
import sys

sys.path.append('../../Libraries')
from functionlib import *
from mediatasklib import *

VS = ['Student', 'Teacher', 'Director', 'Computer']
AS = ['Mic', 'PC']


def mcs_task(host_ip, video_src, audio_src):
    mcs_data = read_json_file('Record.json')
    task_name = get_mt_tasks(ip=host_ip).json()['Names'][0]
    mcs_data['Name'] = task_name

    if video_src not in VS or audio_src not in AS:
        raise ValueError("Please Use Right VideoSource And AudioSource!")

    mcs_data['RecordSpecs'][0]['VideoCodecName'] = "{}_h264_Codec".format(video_src)
    mcs_data['RecordSpecs'][0]['AudioCodecName'] = "Audio{}_aac_Codec".format(audio_src)
    mcs_data['RecordSpecs'][0]['Path'] = "Record_{vid}_{aud}_yyyy-mm-dd-hh-mm-ss.mp4".format(vid=video_src,
                                                                                             aud=audio_src)

    response = post_mt_create_update(ip=host_ip, data=mcs_data)
    if response.json()['Code'] == 201:
        print('Record VideoSrc:{vid} Audio:{aud} Success'.format(vid=video_src, aud=audio_src))
        return True
    else:
        print('Record VideoSrc:{vid} Audio:{aud} Success Fail'.format(vid=video_src, aud=audio_src))
        print(response.json())
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-vs', '--videoSrc', type=str, default='Student',
                        help='Record Video Source:Teacher,Student,etc')
    parser.add_argument('-as', '--audioSrc', type=str, default='Mic', help='Record Audio Source:Mic,PC')
    args = parser.parse_args()
    IP = args.ip
    VIDEOSRC = args.videoSrc
    AUDIOSRC = args.audioSrc

    mcs_task(IP, VIDEOSRC, AUDIOSRC)
