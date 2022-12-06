import argparse

import requests
import threading
import time
import sys
sys.path.append('../../../libraries')
from mediatasklib import *
from functionlib import *
import json

parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
parser.add_argument('--times', '-t', type=int, default=100, help='The Number of concurrent')
parser.add_argument('--source', '-s', type=str, default="Teacher", help='The source of the camera')
parser.add_argument('--type', '-tp', type=str, default="png", help='The snapshot Type')

args = parser.parse_args()
TIME = args.times
SOURCE = args.source
TYPE = args.type

true = True
false = False
IP = input("Please Input Metis IP: ")
data = {
    "times": TIME,  # 并发量
    # "method": "POST",
    "url": "http://{}:6689/mediatask/create_update".format(IP),
    "header": {'Content-type': 'application/json'},
    "body": {
        "Name": "metis_live_mcs",
        "Type": "MCS",
        "Description": "Pipeline task for metis live",
        "Version": "0.3",
        "VideoSpecs": [
            {
                "Name": "Teacher",
                "DeviceId": "0400-0000",
                "Width": 1920,
                "Height": 1080,
                "FrameRate": 30,
                "Format": "UYVY",
                "Path": "/dev/video0",
                "CameraType": "HDMI"
            },
            {
                "Name": "Student",
                "DeviceId": "0400-0001",
                "Width": 1920,
                "Height": 1080,
                "FrameRate": 30,
                "Format": "UYVY",
                "Path": "/dev/video1",
                "CameraType": "HDMI"
            }
        ],
        "VideoAiSpecs": [
            {
                "Name": "Teacher_Tracking",
                "SourceName": "Teacher",
                "Algorithm": "teacher tracking",
                "ProcessRate": 10,
                "Width": 1920,
                "Height": 1080,
                "FrameRate": 10
            },
            {
                "Name": "Student_Tracking",
                "SourceName": "Student",
                "Algorithm": "student tracking",
                "ProcessRate": 10,
                "Width": 1920,
                "Height": 1080,
                "FrameRate": 10
            }
        ],
        "VideoDirectorSpec": {
            "Name": "Director",
            "Width": 1920,
            "Height": 1080,
            "FrameRate": 30,
            "VideoSourceSet": [
                "Student",
                "Student_Tracking",
                "Teacher",
                "Teacher_Tracking"
            ],
            "FrameSpec": {
                "Template": "single frame",
                "LayoutSpecs": [
                    {
                        "Position": 1,
                        "SelectionSpecs": [
                            {
                                "Priority": 1,
                                "VideoSource": "Student",
                                "PadName": "sink_0",
                                "State": "Stand_N",
                                "Delay": 0,
                                "Timeout": 180,
                                "Hold": 6
                            },
                            {
                                "Priority": 2,
                                "VideoSource": "Student_Tracking",
                                "PadName": "sink_1",
                                "State": "Stand_1",
                                "Delay": 0,
                                "Timeout": 180,
                                "Hold": 6
                            },
                            {
                                "Priority": 4,
                                "VideoSource": "Teacher_Tracking",
                                "PadName": "sink_3",
                                "State": "Many",
                                "Delay": 0,
                                "Timeout": 3600,
                                "Hold": 6
                            },
                            {
                                "Priority": 6,
                                "VideoSource": "Teacher_Tracking",
                                "PadName": "sink_3",
                                "State": "Write",
                                "Delay": 0,
                                "Timeout": 3600,
                                "Hold": 6
                            },
                            {
                                "Priority": 7,
                                "VideoSource": "Teacher_Tracking",
                                "PadName": "sink_3",
                                "State": "Move",
                                "Delay": 0,
                                "Timeout": 3600,
                                "Hold": 6
                            },
                            {
                                "Priority": 8,
                                "VideoSource": "Teacher_Tracking",
                                "PadName": "sink_3",
                                "State": "Stand",
                                "Delay": 0,
                                "Timeout": 3600,
                                "Hold": 6
                            },
                            {
                                "Priority": 9,
                                "VideoSource": "Teacher",
                                "PadName": "sink_2",
                                "State": "Out",
                                "Delay": 0,
                                "Timeout": 3600,
                                "Hold": 6
                            },
                            {
                                "Priority": 10,
                                "VideoSource": "Student",
                                "PadName": "sink_0",
                                "State": "Sit",
                                "Delay": 0,
                                "Timeout": 3600,
                                "Hold": 6
                            },
                            {
                                "Priority": 11,
                                "VideoSource": "Teacher",
                                "PadName": "sink_2",
                                "State": "NoTeacher",
                                "Delay": 0,
                                "Timeout": 3600,
                                "Hold": 6
                            },
                            {
                                "Priority": 12,
                                "VideoSource": "Teacher",
                                "PadName": "sink_2",
                                "State": "Others",
                                "Delay": 0,
                                "Timeout": 3600,
                                "Hold": 6
                            },
                            {
                                "Priority": 1,
                                "VideoSource": "Student",
                                "PadName": "sink_0",
                                "State": "Stand_2",
                                "Delay": 0,
                                "Timeout": 180,
                                "Hold": 6
                            }
                        ]
                    }
                ]
            }
        },
        "RenderSpecs": [
            {
                "Name": "Render",
                "DeviceId": "0800-0000",
                "Background": "NA",
                "CompositionSpec": [
                    {
                        "Geometry": [
                            0,
                            0,
                            1920,
                            1080
                        ],
                        "SourceName": "Director"
                    },
                    {
                        "Geometry": [
                            1280,
                            0,
                            1280,
                            720
                        ],
                        "SourceName": "Teacher"
                    },
                    {
                        "Geometry": [
                            0,
                            720,
                            1280,
                            720
                        ],
                        "SourceName": "Student"
                    }
                ]
            }
        ],
        "VideoCodecSpecs": [
            {
                "Name": "Director_highStream",
                "SourceName": "Director",
                "Codec": "h.264",
                "BitRateMode": "VBR",
                "BitRate": "4mbps",
                "iFrameInterval": 900,
                "idrInterval": 900,
                
                "Profile": "High",
                "VbvSize": 4000000
            }
        ],
        "RecordSpecs": [
            {
                "Name": "Director_Record",
                "VideoCodecName": "Director_highStream",
                "Format": "mp4",
                "Path": "/home/user/Videos/eswin/test_yyyy-mm-dd-hh-mm-ss.mp4",
                "SplitMethod": "NA",
                "SplitUnit": 65535
            }
        ],
        "RtcStreamSpec": {
            "Name": "RtcStream",
            "Protocol": "Agora",
            "Channel": "U6mrx",
            "Identity": "ss",
            "VideoCodecName": "Director_highStream"
        }
        }
    }
data2 = {
    "times": TIME,  # 并发量
    # "method": "POST",
    "url": "http://{}:6689/mediatask/remove".format(IP),
    "header": {'Content-type': 'application/json'},
    "body": {
        "Name": "metis_live_mcs",
        "SpecNames": [
            "RtcStream"
        ]
    }
}
data3 = {
    "times": TIME,  # 并发量
    # "method": "POST",
    "url": "http://{}:6689/mediatask/create_update".format(IP),
    "header": {'Content-type': 'application/json'},
    "body": {
        "Name": "metis_live_mcs",
        "Type": "MCS",
        "Description": "Pipeline task for metis live",
        "Version": "0.3",
        "VideoCodecSpecs": [
            {
                "Name": "Director_highStream",
                "SourceName": "Director",
                "Codec": "h.264",
                "BitRateMode": "VBR",
                "BitRate": "4mbps",
                "iFrameInterval": 900,
                "idrInterval": 900,
                
                "Profile": "High",
                "VbvSize": 4000000
            }
        ],
        "RecordSpecs": [
            {
                "Name": "Director_Record",
                "VideoCodecName": "Director_highStream",
                "Format": "mp4",
                "Path": "/home/user/Videos/eswin/test_yyyy-mm-dd-hh-mm-ss.mp4",
                "SplitMethod": "NA",
                "SplitUnit": 65535
            }
        ]
    }
}
data4 = {
    "times": TIME,  # 并发量
    # "method": "POST",
    "url": "http://{}:6689/mediatask/remove".format(IP),
    "header": {'Content-type': 'application/json'},
    "body": {
        "Name": "metis_live_mcs",
        "SpecNames": [
            "Director_Record"
        ]
}
}
Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType='IPC', aiStrategy='student')
data['body']['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
def get_requests(d,d2,d3,d4):

    global RIGHT_NUM
    global ERROR_NUM
    try:
        r = requests.post(d["url"], headers=d["header"], json=d['body'])
        # print(r.status_code)
        if r.json()['Code'] == 201:
            lock.acquire()  # 上锁
            RIGHT_NUM += 1
            lock.release()
            print(r.json())
        # print("RIGHT_NUM:",RIGHT_NUM)
        else:
            lock.acquire()  # 上锁
            ERROR_NUM += 1
            lock.release()
            print(r.json())
    except Exception as e:
        lock.acquire()  # 上锁
        ERROR_NUM += 1
        lock.release()
        print(e)
    try:
        r = requests.post(d2["url"], headers=d2["header"], json=d2['body'])
        # print(r.status_code)
        if r.json()['Code'] == 200:
            lock.acquire()  # 上锁
            RIGHT_NUM += 1
            lock.release()
            print(r.json())
        # print("RIGHT_NUM:",RIGHT_NUM)
        else:
            lock.acquire()  # 上锁
            ERROR_NUM += 1
            lock.release()
            print(r.json())
    except Exception as e:
        lock.acquire()  # 上锁
        ERROR_NUM += 1
        lock.release()
        print(e)
    try:
        r = requests.post(d3["url"], headers=d3["header"], json=d3['body'])
        # print(r.status_code)
        if r.json()['Code'] == 201:
            lock.acquire()  # 上锁
            RIGHT_NUM += 1
            lock.release()
            print(r.json())
        # print("RIGHT_NUM:",RIGHT_NUM)
        else:
            lock.acquire()  # 上锁
            ERROR_NUM += 1
            lock.release()
            print(r.json())
    except Exception as e:
        lock.acquire()  # 上锁
        ERROR_NUM += 1
        lock.release()
        print(e)
    try:
        r = requests.post(d4["url"], headers=d4["header"], json=d4['body'])
        # print(r.status_code)
        if r.json()['Code'] == 200:
            lock.acquire()  # 上锁
            RIGHT_NUM += 1
            lock.release()
            print(r.json())
        # print("RIGHT_NUM:",RIGHT_NUM)
        else:
            lock.acquire()  # 上锁
            ERROR_NUM += 1
            lock.release()
            print(r.json())
    except Exception as e:
        lock.acquire()  # 上锁
        ERROR_NUM += 1
        lock.release()
        print(e)

def run1():

    Threads = []

    for i in range(data["times"]):
        t = threading.Thread(target=get_requests(data,data2,data3,data4))
        t.setDaemon(True)
        Threads.append(t)

    time1 = time.time()
    for t in Threads:
        # print(t)
        t.start()

    # for t in Threads:
    # t.join()

    time2 = time.time()
    time.sleep(5)
    print("===============测试结果===================")
    print("URL:", data["url"])
    print("body:", data['body'])
    print("并发数:", data["times"])
    print("总耗时(秒):", time2 - time1)
    print("每次请求耗时(秒):", (time2 - time1) / data["times"])
    print("正确数量:", RIGHT_NUM)
    print("错误数量:", ERROR_NUM)


if __name__ == '__main__':
    RIGHT_NUM = 0
    ERROR_NUM = 0
    lock = threading.Lock()  # 创建一把锁
    print("测试启动")
    run1()
    print("执行结束.")