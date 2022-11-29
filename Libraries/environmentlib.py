import io
import json
import sys
import os
import datetime


#####################################################################
#                   全局变量管理功能部分(目前未使能)                      #
#####################################################################
def _init():
    """初始化操作"""
    global GLOBALS_DICT
    # 用Key-Value的形式存储和获取变量
    GLOBALS_DICT = {}


def _set(name, value):
    """设置"""
    try:
        GLOBALS_DICT[name] = value
        return True
    except KeyError:
        return False


def _get(name):
    """取值"""
    try:
        return GLOBALS_DICT[name]
    except KeyError:
        return "Not Found"


def check_eth_connect():
    """
    设置对应IP，如果是linux系统，而且脚本放在小站上,可以自动获取IP地址
    但如果是放在开发机上，就不能调用这个函数获取IP地址，需要手动修改HOST_IP的值
    :return:
    """
    ip_get_cmd = "ifconfig eth0 | grep 'inet ' | awk '{print $2}'"
    if sys.platform.startswith("win"):
        # 如果是Windows系统，需要手动设置修改下面IP地址
        HOST_IP = '10.12.224.135'
    else:
        while True:
            HOST_IP = os.popen(ip_get_cmd).read().strip()
            if HOST_IP is None or HOST_IP == "":
                continue
            else:
                # print(HOST_IP)
                break
    return HOST_IP


#####################################################################
#                         初始化配置模块部分                           #
#####################################################################
"""
目前不采用复杂的手段,简单的4个变量控制全局
_init()
# 设置对应摄像头类型
_set("Global_TeacherCamType", "IPC")
_set("Global_StudentCamType", "IPC")
_set("Global_BlackBoardCamType", "IPC")
_set("Global_PPTCamType", "HDMI")
# 设置请求的IP地址
_set("Global_HostIP", check_eth_connect())
"""

MCS_Cfg = json.load(open("{}/MCSConfiguration.json".format(os.path.dirname(os.path.abspath(__file__))), 'r'))
# 加载配置文件

Global_TeacherCamType = MCS_Cfg["CameraType"]['Global_TeacherCamType']
Global_StudentCamType = MCS_Cfg["CameraType"]['Global_StudentCamType']
Global_BlackBoardCamType = MCS_Cfg["CameraType"]['Global_BlackBoardCamType']
Global_PPTCamType = MCS_Cfg["CameraType"]['Global_PPTCamType']
Global_GeneralCamType = MCS_Cfg["CameraType"]['Global_GeneralCamType']
Global_GeneralCamType_other = MCS_Cfg["CameraType"]['Global_GeneralCamType_other']

# 为自动化服务
Global_NearEnd = '10.12.224.135'
Global_FarEnd = '10.12.224.140'

PLATFORM = sys.platform                  # 操作系统

Whether_Log_File = MCS_Cfg['IsLogFile']

#####################################################################
#                         Log File 模块部分                          #
#####################################################################


def write_log(content, FileName):
    """
    向文件写入内容
    :param content:
    :param FileName:
    :return:
    """
    MainPath = '/home/user/Metis-MCS/MCS_Log'  # Linux Log存放路径
    Log_Path = "MCS_Log"  # Windows
    if PLATFORM.startswith("linux"):
        if not os.path.isdir(MainPath):  # 如果当前路径不存在Log目录，则生成一个
            print('Create MCS Log File Folder...')
            print("MCS Log File Path : {}".format(MainPath))
            if os.system('mkdir {}'.format(MainPath)):
                print('Make out dir failed.')

        with open('{}/{}'.format(MainPath, FileName), 'a+', encoding="utf-8") as Log:
            Log.write('***********{}************\n'.format(content))

    elif PLATFORM.startswith("win"):
        if not os.path.isdir(Log_Path):  # 如果当前路径不存在Log目录，则生成一个
            print('Create MCS Log File Folder...')
            print("MCS Log File Path : {}".format(os.path.abspath(os.path.join(os.getcwd(), Log_Path))))
            if os.system('mkdir {}'.format(Log_Path)):
                print('Make out dir failed.')
        with open('{}/{}'.format(Log_Path, FileName), 'a+', encoding="utf-8") as Log:
            Log.write('{}\n'.format(content))


def log_file(api, mcs, res, retype):
    # print(type(Time))
    # 对于Windows系统，是脚本同级目录下生成Log文件
    # 对于Linux系统，在指定路径下生成Log文件
    # 需要生成的Log信息包含 时间、调用的接口、MCS内容、返回的响应体、接口类型GET之类
    Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    MCS_Cfg_Temp = json.load(open("{}/MCSConfiguration.json".format(os.path.dirname(os.path.abspath(__file__))), 'r'))
    FileName = MCS_Cfg_Temp['FileName']
    splitLine = "----------"
    write_log("\n" + splitLine*5 + "\n" + "* Time Line: " + Time, FileName)
    write_log("* API: " + retype + " " + api, FileName)
    write_log("* Using MCS As Follow: \n" + json.dumps(mcs, indent=2), FileName)
    write_log("* Response As Follow: \n" + json.dumps(res), FileName)


def modify_cfg(key, value):
    # 修改配置文件使用
    MCS_Cfg[key] = value
    with io.open("{}/MCSConfiguration.json".format(os.path.dirname(os.path.abspath(__file__))), 'w') as jsonfile:
        json.dump(MCS_Cfg, jsonfile, indent=4)
