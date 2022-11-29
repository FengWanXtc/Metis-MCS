import requests
import json
import os
import io
import time
import environmentlib

# ***********Get the IP Address*************
# Please run this script in metis station

HOST_IP = environmentlib.check_eth_connect()
url = "http://{}:6689/auth".format(HOST_IP)
headers = {'Content-type': 'application/json'}


def read_json_file(filename):
    path = os.path.abspath(os.path.join(os.getcwd(), "json_templates/"))
    # print(path)
    # path = 'json_templates'
    filepath = path + '/' + filename
    file = open(filepath, 'r')
    data = json.load(file)
    return data


# *************For New Version Change********************
def post_internal_mediadevice_camera(DeviceId, token='', data=None):
    # 修改本地管理摄像头
    if data is None:
        data = {}
    tempurl = "http://{}:6689/internal/mediadevice/camera/".format(HOST_IP) + DeviceId
    databody = data
    tempheaders = headers
    if token != '':
        tempheaders['Token'] = token
    response = requests.post(url=tempurl, headers=tempheaders, json=databody)
    return response


def act_story(scriptlist, sleeptime=5):
    # 故事演绎脚本,传入动作列表依次执行动作
    pre_time = time.time()
    for items in scriptlist:
        os.system('python {}'.format(items))
        # print(items)
        time.sleep(sleeptime)
    print('Story Ends.Thanks for Watching')
    now_time = time.time()
    TimeLen = int(now_time - pre_time)
    print('The Story Costs ' + str(TimeLen) + ' Seconds')


# 下面3个函数可以优化成一个哦 *^*

def get_item(VideoIns, Algorithms):
    # 用于记录是否找到对应算法的摄像头，0为找到，1为未找到
    flag = 0
    # 用于保存可能存在的返回值
    tem_item = None
    for item in VideoIns:
        # 找如果有算法，就返回否则返回失败
        if ('Algorithms' in item
                and item["DeviceName"].find("IPC_CAM") != -1
                and item['Algorithms'][0] == "{} tracking".format(Algorithms)):
            tem_item = item
            flag = 1
        if ('Algorithms' in item
                and item["DeviceName"].find("HDMI_CAM") != -1
                and item['Algorithms'][0] == "{} tracking".format(Algorithms)):
            tem_item = item
            flag = 1
        if ('Algorithms' in item
                and item["DeviceName"].find("USB_CAM") != -1
                and item['Algorithms'][0] == "{} tracking".format(Algorithms)):
            tem_item = item
            flag = 1
    if flag == 1:
        return tem_item
    else:
        print("Get Item Function Can not Found Camera with {} Algorithm".format(Algorithms))
        return False


# *************MCS 0.3 Spec New Change********************
def get_Video_DeviceId_by_list(ip, camType, camNum, token=''):
    # 根据摄像头类型和序列号获取DeviceId
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediadevice/list".format(ip)
    tempheaders = headers
    databody = {}
    if token != '':
        tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)

    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")

    if camType == 'HDMI' and camNum != 'IN':
        DeviceName = 'HDMI_CAM_{}'.format(camNum)
    elif camType == 'HDMI':
        DeviceName = 'HDMI_PC_IN'
    elif camType == 'USB':
        DeviceName = 'USB_CAM_P3-{}'.format(camNum)

    VideoIns = response.json()["VideoIns"]
    for items in VideoIns:
        if items["DeviceName"] == DeviceName:
            # 匹配摄像头类型和序号,HDMI,IPC,USB
            return items["DeviceId"]


def get_Video_DeviceId_by_internal_camera(ip, camType, camNum, token=''):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/internal/mediadevice/camera".format(ip)
    tempheaders = headers
    databody = {}
    if token != '':
        tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, json.dumps(databody), response.json(), "GET")

    if camType == 'HDMI' and camNum != '3':
        DeviceName = 'HDMI_CAM_{}'.format(camNum)
    elif camType == 'HDMI' and camNum == '3':
        DeviceName = 'HDMI_PC_IN'
    elif camType == 'USB':
        # 对USB摄像头需要获取其DeviceName的形式2.0USB和3.0USB摄像头有区别
        for item in response.json():
            if item['deviceName'].find("USB") != -1:
                Old_DeviceName = item["deviceName"]
                DeviceName = Old_DeviceName.replace(Old_DeviceName[-1], camNum)
    elif camType == 'IPC':
        DeviceName = 'IPC_CAM_{}'.format(camNum)

    for item in response.json():
        if item["deviceName"] == DeviceName:
            # 匹配摄像头类型和序号,HDMI,IPC,USB
            return item["deviceId"]


def get_DeviceId_by_aiStrategy(ip, camType, aiStrategy, token=''):
    # 根据AI 算法获取摄像头的DeviceId
    # 该函数需要优化，如果获取为空的
    # 根据本地管理配置好相应算法的配置获取摄像头DeviceId

    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/internal/mediadevice/camera".format(ip)
    tempheaders = headers
    databody = {}
    if token != '':
        tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)
    # 内部接口尽量避免打印Log
    for item in response.json():
        if item['deviceName'].find(camType) != -1 and item['aiStrategy'].find(aiStrategy) != -1 and item['isOpen'] is True:
            return item["deviceId"]
            # 脚本在此处就会进行跳出操作，如果没有获取到相应的摄像头DeviceId
            # 就根据 Mediadevice 接口 获取已经配置的摄像头Id

    # 这部分代码是如果上一个步骤没有跳出去的操作
    TempUrl = "http://{}:6689/mediadevice/video/in".format(ip)
    NewResponse = requests.get(url=TempUrl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")

    VideoIns = NewResponse.json()["VideoIns"]
    DeviceIdList = []
    for VideoIn in VideoIns:

        if VideoIn["Algorithms"][0].find(aiStrategy) != -1 and VideoIn["DeviceName"].find("HDMI") != -1:
            return VideoIn["DeviceId"]
            # 优先级适配，高优先级HDMI会在这一步骤跳出
        elif VideoIn["Algorithms"][0].find(aiStrategy) != -1 and VideoIn["DeviceName"].find("IPC") != -1:
            return VideoIn["DeviceId"]

    # MA 给的反馈USB排在HDMI前面
    for VideoIn in VideoIns:
        if VideoIn["Algorithms"][0].find(aiStrategy) != -1 and VideoIn["DeviceName"].find("USB") != -1:
            return VideoIn["DeviceId"]
            # 设置这一步的目的是为了将 USB 优先级放在最后

    # 如果没有一个摄像头配置上相应算法，打印出提示
    print("Warning:: Can't Get Camera DeviceId.Please Check Configuration In Local Manager System!")


if __name__ == '__main__':
    D = get_DeviceId_by_aiStrategy("10.12.224.135", "R", "teacher")
    print(D)
