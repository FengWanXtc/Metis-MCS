import argparse

import requests
import threading
import time

lock = threading.Lock()  # 创建一把锁
Header = {'Content-type': 'application/json'}
P1_data = {
    "Name": "Agora_Basic",
    "Type": "MCS",
    "Description": "Dynamic Change",
    "Version": "0.3",
    "RtcStreamSpec": {
        "Name": "RtcStream",
        "Protocol": "Agora",
        "Channel": "Agora_Channel",
        "Identity": "Agora_Basic",
        "VideoCodecName": "Computer_h264_Codec",
        "AudioCodecName": "AudioMic_pcm_Codec",
        "LowVideoCodecName": "NULL"
    }
}
P2_data = {
    "Name": "Agora_Basic",
    "Type": "MCS",
    "Description": "Dynamic Change",
    "Version": "0.3",
    "RtcStreamSpec": {
        "Name": "RtcStream",
        "Protocol": "Agora",
        "Channel": "Agora_Channel",
        "Identity": "Agora_Basic",
        "VideoCodecName": "Student_h264_Codec",
        "AudioCodecName": "AudioPC_pcm_Codec",
        "LowVideoCodecName": "NULL"
    }
}


def post_thread_1(ip):
    global RIGHT_NUM
    global ERROR_NUM
    times = 100
    while times > 0:
        try:
            teURL = "http://{}:6689/mediatask/create_update".format(ip)
            r = requests.post(url=teURL, headers=Header, json=P1_data)
            if r.json()['Code'] == 201:
                lock.acquire()  # 上锁
                RIGHT_NUM += 1
                lock.release()
                # print(r.json())
            else:
                lock.acquire()  # 上锁
                ERROR_NUM += 1
                print(r.json())
                lock.release()
        except Exception as e:
            lock.acquire()  # 上锁
            ERROR_NUM += 1
            print(e)
            lock.release()
        times -= 1


def post_thread_2(ip):
    global RIGHT_NUM
    global ERROR_NUM
    times = 100
    while times > 0:
        try:
            teURL = "http://{}:6689/mediatask/create_update".format(ip)
            r = requests.post(url=teURL, headers=Header, json=P2_data)
            if r.json()['Code'] == 201:
                lock.acquire()  # 上锁
                RIGHT_NUM += 1
                lock.release()
                # print(r.json())
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
        times -= 1


def run(ip):
    time1 = time.time()
    t1 = threading.Thread(target=post_thread_1(ip))  # 已经创建好的一个线程
    t2 = threading.Thread(target=post_thread_2(ip))  # 已经创建好的一个线程
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # t3.join()
    # t4.join()
    time2 = time.time()
    # 等待5S是为了让全局变量进行更新
    print("===============测试结果===================")
    print("并发数:", 100)
    print("总耗时(秒):", time2 - time1)
    print("每次请求耗时(秒):", (time2 - time1) / 100)
    print("正确数量:", RIGHT_NUM)
    print("错误数量:", ERROR_NUM)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 Concurrent_SingleMCS.py -ip=10.XXXX -t=100')
    parser.add_argument('-ip', type=str, default='10.12.224.135', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip

    RIGHT_NUM = 0
    ERROR_NUM = 0
    print('测试启动,请等待所有请求发送完成')
    run(IP)
    print("执行结束.")
