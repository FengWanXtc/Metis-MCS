import json

import requests
import threading
import time

from functionlib import read_json_file

URL = "http://10.12.224.51:6689/mediatask/snapshot"
Header = {'Content-type': 'application/json'}


def post_thread_1():
    p1_data = read_json_file('snap.json')

    global RIGHT_NUM
    global ERROR_NUM
    times = 1
    while times > 0:
        try:
            teURL = "http://10.12.224.51:6689/mediatask/snapshot"
            r = requests.post(url=teURL, headers=Header, json=p1_data)
            if r.json()['Code'] == 200:
                RIGHT_NUM += 1
                print(r.json())
            else:
                ERROR_NUM += 1
                print(r.json())
        except Exception as e:
            ERROR_NUM += 1
            print(e)
        times -= 1


def post_thread_2():
    data = read_json_file('Compose.json')
    # print(json.dumps(data, indent=2))
    global RIGHT_NUM
    global ERROR_NUM
    times = 1
    while times > 0:
        try:
            teURL = "http://10.12.224.51:6689/mediatask/create_update"
            r = requests.post(url=teURL, headers=Header, json=data)
            if r.json()['Code'] == 201:
                RIGHT_NUM += 1
                print(r.json())
            else:
                ERROR_NUM += 1
                print(r.json())
        except Exception as e:
            ERROR_NUM += 1
            print(e)
        times -= 1


def post_thread_3():
    data = {
        # 参数
        "Name": "Basic_MCS",
        "SourceName": "Student",
        "Format": "png",
        "Path": "Student_yyyy-mm-dd-hh-mm-ss.png"
    }
    global RIGHT_NUM
    global ERROR_NUM
    try:
        r = requests.post(url=URL, headers=Header, json=data)
        if r.json()['Code'] == 200:
            RIGHT_NUM += 1
            print(r.json())
        else:
            ERROR_NUM += 1
            print(r.json())
    except Exception as e:
        ERROR_NUM += 1
        print(e)


def post_thread_4():
    data = {
        # 参数
        "Name": "Basic_MCS",
        "SourceName": "Student",
        "Format": "png",
        "Path": "Student_yyyy-mm-dd-hh-mm-ss.png"
    }
    global RIGHT_NUM
    global ERROR_NUM
    try:
        r = requests.post(url=URL, headers=Header, json=data)
        if r.json()['Code'] == 200:
            RIGHT_NUM += 1
            print(r.json())
        else:
            ERROR_NUM += 1
            print(r.json())
    except Exception as e:
        ERROR_NUM += 1
        print(e)


def run1():
    time1 = time.time()
    t1 = threading.Thread(target=post_thread_1)  # 已经创建好的一个线程
    t2 = threading.Thread(target=post_thread_2)  # 已经创建好的一个线程
    t1.start()
    t2.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    time2 = time.time()
    # 等待5S是为了让全局变量进行更新
    time.sleep(10)
    print("===============测试结果===================")
    print("并发数:", 1)
    print("总耗时(秒):", time2 - time1)
    print("每次请求耗时(秒):", (time2 - time1) / 1)
    print("正确数量:", RIGHT_NUM)
    print("错误数量:", ERROR_NUM)


if __name__ == '__main__':
    RIGHT_NUM = 0
    ERROR_NUM = 0
    print('测试启动')

    run1()

    print("执行结束.")
