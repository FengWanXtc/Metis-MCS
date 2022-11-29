import requests
import threading
import time

URL = "http://10.12.224.135:6689/mediatask/snapshot"
Header = {'Content-type': 'application/json'}


def post_thread_1():
    data = {
        # 参数
        "Name": "Basic_MCS",
        "SourceName": "Teacher_Ai",
        "Format": "png",
        "Path": "Teacher_Ai_yyyy-mm-dd-hh-mm-ss.png"
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


def post_thread_2():
    data = {
        # 参数
        "Name": "Basic_MCS",
        "SourceName": "Director",
        "Format": "png",
        "Path": "Director_yyyy-mm-dd-hh-mm-ss.png"
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
    t3 = threading.Thread(target=post_thread_3)  # 已经创建好的一个线程
    t4 = threading.Thread(target=post_thread_4)  # 已经创建好的一个线程
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    time2 = time.time()
    # 等待5S是为了让全局变量进行更新
    time.sleep(5)
    print("===============测试结果===================")
    print("URL:", URL)
    print("并发数:", 4)
    print("总耗时(秒):", time2 - time1)
    print("每次请求耗时(秒):", (time2 - time1) / 4)
    print("正确数量:", RIGHT_NUM)
    print("错误数量:", ERROR_NUM)


if __name__ == '__main__':
    RIGHT_NUM = 0
    ERROR_NUM = 0
    print('测试启动')

    run1()

    print("执行结束.")
