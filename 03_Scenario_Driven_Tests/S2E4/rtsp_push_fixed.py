import sys
import argparse
sys.path.append('../../libraries')
from mediatasklib import *
from functionlib import *
from mediadevicelib import *


def rtsp_push(IP):
    rtsp_push_data = read_json_file('rtsp_push_fixed.json')
    VideoIns = get_md_video_in(ip=IP).json()['VideoIns']
    #print(json.dumps(rtsp_push_data, indent=2))
    print(json.dumps(VideoIns, indent=2))
    # 找到第一个HDMI摄像头获取DeviceId
    for VideoIn in VideoIns:
        if VideoIn['DeviceName'].find('HDMI') != -1:
            rtsp_push_data['VideoSpecs'][0]['DeviceId'] = VideoIn['DeviceId']
            break

    if IP == '':
        # IP 为空说明是在当前小站
        rtsp_push_data['ServerSpecs'][0]['URI'] = 'rtsp://127.0.0.1:8554/metis/ch1'
    else:
        # IP 不为空需要指定推流小站
        rtsp_push_data['ServerSpecs'][0]['URI'] = 'rtsp://{}:8554/metis/ch1'.format(IP)

    print(json.dumps(rtsp_push_data, indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=rtsp_push_data)
    except:
        print('Post Create Task Failed')
        print(response.status_code)
        return False

    if (response.json()['Code'] == 201):
        print('RTSP Push Task Success! Please Use Vlc to check Video Streams')
        return True
    else:
        print('RTSP Push Task Fail')
        print(response.json())
        return False


def main():
    parser = argparse.ArgumentParser(description='usage: python3 rtsp_push.py  -ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The ip of Metis Station to push rtsp stream')
    args = parser.parse_args()
    IP = args.ip  # 指定推流小站的IP
    rtsp_push(IP)


if __name__ == '__main__':
    main()
