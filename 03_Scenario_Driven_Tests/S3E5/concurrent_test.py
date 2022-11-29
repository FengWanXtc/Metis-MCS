import argparse
import sys
import threading
sys.path.append('../../Libraries')
from environmentlib import *
from functionlib import *


def read_json_file(filename):
    # path = os.path.abspath(os.path.join(os.getcwd(), "../json_templates/"))
    path = 'json_templates'
    filepath = path + '/' + filename
    file = open(filepath, 'r')
    jsonData = json.load(file)
    return jsonData


def post_task(ip):
    if ip == '':
        ip = Global_NearEnd
    tempurl = "http://{}:6689/mediatask/create_update".format(ip)
    tempHeader = {'Content-type': 'application/json'}
    response = requests.post(url=tempurl, headers=tempHeader, json=post_data)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, post_data, response.json(), "POST")
    return response


def concurrent_test(threadName, looptime, ip):
    while looptime:
        # print(threadName, data['VideoSpecs'][0])
        response = post_task(ip)

        print("{}:: The present Count is {}, Codec::".format(threadName, looptime), response.json())
        # time.sleep(0.5)
        looptime -= 1


class myThread(threading.Thread):
    def __init__(self, threadID, name, looptime, ip):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.looptime = looptime
        self.ip = ip

    def run(self):
        print("开始线程：" + self.name)
        # print_time(self.name, self.looptime, 5)
        concurrent_test(self.name, self.looptime, self.ip)
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
    print("结束")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip
    post_data = read_json_file('4F-4.1D-4.2T-4.3S-4.4RA.json')
    Teacher_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=Global_TeacherCamType, aiStrategy='teacher')
    post_data['VideoSpecs'][0]['DeviceId'] = Teacher_DeviceId
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType=Global_StudentCamType, aiStrategy='student')
    post_data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId

    # 创建新线程
    thread1 = myThread(1, "Thread-1", 50, IP)
    thread2 = myThread(2, "Thread-2", 50, IP)
    # thread3 = myThread(3, "Thread-3", 50, IP)
    # 开启新线程
    thread1.start()
    # thread3.start()
    thread2.start()

    # thread3.join()
    thread2.join()
    thread1.join()

    print("退出主线程")
