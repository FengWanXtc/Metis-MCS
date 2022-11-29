import requests
import argparse
import json

# ***********Get the IP Address*************
# ip_get_cmd = "ifconfig eth0 | grep 'inet ' | awk '{print $2}'"
# HOST_IP = os.popen(ip_get_cmd).read().strip()
HOST_IP = "10.12.224.135"
headers = {'Content-type': 'application/json'}

# 模板
camera_data = '''
{
        "aliasName": "Tea2",
        "isOpen": true,
        "rtspUrl": "",
        "aiStrategy": "",
        "codec": "H264",
        "format": "UYVY",
        "resolutionWidth": 1920,
        "resolutionHeight": 1080,
        "framerate": 30
}
'''
# 转化成json格式
camera_data_json = json.loads(camera_data)


# 获取DeviceId
def get_DeviceId_by_devicePath(deviceNum):
    tempurl = "http://{}:6689/internal/mediadevice/getDeviceInfo".format(HOST_IP)
    tempheaders = headers
    databody = {}
    devicePath = "/dev/video" + deviceNum
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)
    reslist = response.json()['cameras']
    listlen = len(reslist)
    for i in range(0, listlen):
        if (reslist[i]['devicePath'] == devicePath):
            DeviceId = reslist[i]['uuid']
            return DeviceId


# 下发修改本地管理摄像头
def post_camera(deviceid, token='', data={}):
    tempurl = "http://{}:6689/internal/mediadevice/camera/".format(HOST_IP) + deviceid
    databody = data
    tempheaders = headers
    if (token != ''):
        tempheaders['Token'] = token
    response = requests.post(url=tempurl, headers=tempheaders, json=databody)
    return response


def set_camera(aliasName, deviceNum, aiStrategy):
    # 获取DeviceId
    DeviceId = get_DeviceId_by_devicePath(deviceNum)

    # 需要修改的body
    post_data = camera_data_json
    post_data["aliasName"] = aliasName
    post_data["rtspUrl"] = "/dev/device" + deviceNum
    post_data["aiStrategy"] = aiStrategy + " tracking"

    response = post_camera(deviceid=DeviceId, data=post_data)

    # 结果判定
    if (response.json()["Code"] == 200):
        print("Set camera Success")
    else:
        print("Set Camera Fail")
        print(response.json())


def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 set_camera.py -a=Teacher(self-define) -d=0(1,2,3...) -ai=teacher(student,blackboard,ppt).')
    parser.add_argument('--aliasName', '-a', type=str, default='Teacher',
                        help='The aliasName of the camera,default is Teacher.')
    parser.add_argument('--deviceNum', '-d', type=str, default='0', help='The device of the camera,default is 0.')
    parser.add_argument('--aiStrategy', '-ai', type=str, default='teacher',
                        help='The ai strategy of the camera,default is teacher.')
    args = parser.parse_args()

    ALIASNAME = args.aliasName
    DEVICENUM = args.deviceNum
    AISTRATEGY = args.aiStrategy
    set_camera(ALIASNAME, DEVICENUM, AISTRATEGY)


if __name__ == '__main__':
    main()
