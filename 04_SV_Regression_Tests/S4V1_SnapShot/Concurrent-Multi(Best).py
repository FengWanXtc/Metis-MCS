import requests
import threading
import time

URL = "http://10.12.224.135:6689/mediatask/snapshot"
Header = {'Content-type': 'application/json'}


class myThread(threading.Thread):
    def __init__(self, name, Source, Format='png'):
        threading.Thread.__init__(self)
        self.name = name
        self.tData = {
            # 参数
            "Name": "Basic_MCS",
            "SourceName": Source,
            "Format": Format,
            "Path": "{}_yyyy-mm-dd-hh-mm-ss.png".format(Source)
        }

    def run(self):
        global RIGHT_NUM
        global ERROR_NUM

        print("开始线程：" + self.name)
        # print_time(self.name, self.looptime, 5)
        try:
            r = requests.post(url=URL, headers=Header, json=self.tData)

            if r.json()['Code'] == 200:
                lock.acquire()  # 上锁
                RIGHT_NUM += 1
                lock.release()
                # print(r.json())
            else:
                lock.acquire()
                ERROR_NUM += 1
                lock.release()
                print(r.json())

        except Exception as e:
            lock.acquire()
            ERROR_NUM += 1
            lock.release()
            print(e)

        print("退出线程：" + self.name)


def run_thread():
    SourceList = ["Teacher", "Student", "Blackboard", "Director", "Student_Ai",
                  "Teacher_Ai", "TcpVideoA_pull", "TcpVideoC_pull", "Blackboard_Ai"]
    time1 = time.time()
    for item in SourceList:
        t = myThread("Thread-{}".format(item), item)
        t.start()
        # t.join()
    time2 = time.time()

    # 等待10S是为了让全局变量进行更新
    time.sleep(10)
    print("===============测试结果===================")
    print("URL:", URL)
    print("并发数:", len(SourceList))
    print("总耗时(秒):", time2 - time1)
    print("每次请求耗时(秒):", (time2 - time1) / len(SourceList))
    print("正确数量:", RIGHT_NUM)
    print("错误数量:", ERROR_NUM)


if __name__ == '__main__':
    RIGHT_NUM = 0
    ERROR_NUM = 0
    lock = threading.Lock()  # 创建一把锁
    print('测试启动')

    run_thread()

    print("执行结束.")
