import argparse
import requests
import threading
import time

parser = argparse.ArgumentParser(description='usage: python3 Concurrent_SingleMCS.py -ip=10.XXXX -t=100')
parser.add_argument('--times', '-t', type=int, default=100, help='The Number of concurrent')
parser.add_argument('-ip', type=str, default='10.12.224.135', help='The IP address of the METIS')

args = parser.parse_args()
TIME = args.times
IP = args.ip

data = {
    "times": TIME,  # 并发量
    "method": "POST",
    "url": "http://{}:6689/mediatask/create_update".format(IP),
    "header": {'Content-type': 'application/json'},
    "body": {
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
            "AudioCodecName": "AudioPC_pcm_Codec",
            "LowVideoCodecName": "NULL"
        }
    }
}


def get_requests():
    global RIGHT_NUM
    global ERROR_NUM
    global Flag
    try:
        # print("Start Time:" + str(time.time()))
        r = requests.post(data["url"], headers=data["header"], json=data['body'])
        # print(r.status_code)
        if r.json()['Code'] == 201 or r.json()['Code'] == 202:
            lock.acquire()  # 上锁
            RIGHT_NUM += 1
            lock.release()
            # print(r.json())
        # print("RIGHT_NUM:",RIGHT_NUM)
        else:
            lock.acquire()  # 上锁
            ERROR_NUM += 1
            Flag = False
            lock.release()
            print(r.json())
    except Exception as e:
        lock.acquire()  # 上锁
        ERROR_NUM += 1
        Flag = False
        lock.release()
        print(e)


def run():
    Threads = []
    time1 = time.time()
    for i in range(data["times"]):
        t = threading.Thread(target=get_requests)
        t.setDaemon(True)
        Threads.append(t)

    for t in Threads:
        # print(t)
        t.start()

    time2 = time.time()

    for t in Threads:
        t.join()


    # time.sleep(10)
    print("===============测试结果===================")
    print("URL:", data["url"])
    print("并发数:", data["times"])
    print("总耗时(秒):", time2 - time1)
    print("每次请求耗时(秒):", (time2 - time1) / data["times"])
    print("正确数量:", RIGHT_NUM)
    print("错误数量:", ERROR_NUM)


if __name__ == '__main__':
    RIGHT_NUM = 0
    ERROR_NUM = 0
    Flag = True
    lock = threading.Lock()  # 创建一把锁
    print("测试启动,请等待所有请求发送完成")
    run()
    print("执行结束.")
    if Flag:
        print("Concurrent Post Same MCS to Dynamic Change RtcStreamSpec Test Pass")
    else:
        print("Concurrent Post Same MCS to Dynamic Change RtcStreamSpec Test Fail")
