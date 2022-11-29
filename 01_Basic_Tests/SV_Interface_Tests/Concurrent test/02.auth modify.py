import argparse

import requests
import threading
import time

parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
parser.add_argument('--times', '-t', type=int, default=100, help='The Number of concurrent')
parser.add_argument('--source', '-s', type=str, default="Teacher", help='The source of the camera')
parser.add_argument('--type', '-tp', type=str, default="png", help='The snapshot Type')

args = parser.parse_args()
TIME = args.times
SOURCE = args.source
TYPE = args.type

IP = input("Please Input Metis IP: ")
data = {
    "times": TIME,  # 并发量
    # "method": "POST",
    "url": "http://{}:6689/auth/modify".format(IP),
    "header": {'Content-type': 'application/json'},
    "body": {
        "NewName": "admin",
        "NewPassword": "admin"
    }
}


def get_requests():
    global RIGHT_NUM
    global ERROR_NUM
    try:
        r = requests.post(data["url"], headers=data["header"], json=data['body'])
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
        t = threading.Thread(target=get_requests)
        t.setDaemon(True)
        Threads.append(t)
    time1 = time.time()
    for t in Threads:
        # print(t)
        t.start()

    # for t in Threads:
    # t.join()

    time2 = time.time()
    time.sleep(10)
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