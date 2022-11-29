import argparse

import requests
import threading
import time
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
    "url": "http://{}:6689/mediadevice/audio/in/configuration".format(IP),
    "header": {'Content-type': 'application/json'},
    "body": {
       "DeviceId" : "0103-0200",
       "Mute": true
    }
}
data2 = {
    "times": TIME,  # 并发量
    # "method": "POST",
    "url": "http://{}:6689/mediadevice/audio/in/configuration".format(IP),
    "header": {'Content-type': 'application/json'},
    "body": {
       "DeviceId" : "0103-0200",
       "Mute": false
    }
}
deviceid = requests.get("http://{}:6689/mediadevice/audio/in/configuration".format(IP), headers={'Content-type': 'application/json'}, json='')
data['body']['DeviceId'] = deviceid.json()["AudioIns"][0]["DeviceId"]
data2['body']['DeviceId'] = deviceid.json()["AudioIns"][0]["DeviceId"]
def get_requests(d,d2):
    global RIGHT_NUM
    global ERROR_NUM
    try:
        r = requests.post(d["url"], headers=d["header"], json=d['body'])
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

def run1():

    Threads = []
    time1 = time.time()
    for i in range(data["times"]):
        t = threading.Thread(target=get_requests(data,data2))
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