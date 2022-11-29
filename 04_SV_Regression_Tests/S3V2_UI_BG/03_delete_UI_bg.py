import sys
import paramiko

sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *

databody = {
    "DeviceId": "",
    "Background": "/home/user/EST/MCSScripts/background.png"
}

hostname = input("Please input a Metis IP to test: ")

# Careful the host Metis-station
port = 22
login = 'user'
password = 'User@1949!'
outputStr = ''


def sshctrl():
    execmd = 'cd ~/EST/MCSScripts && rm -rf background.png'
    s = paramiko.SSHClient()  # 创建SSH对象
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接主机
    s.connect(hostname=hostname, port=port, username=login, password=password)  # 连接服务器
    stdin, stdout, stderr = s.exec_command(execmd)  # 执行命令

    outputBytes = stdout.read() + stderr.read()
    outputStr = outputBytes.decode("utf-8")
    print(outputStr)


def get_background_DeviceId():
    token = post_auth(username='admin', password='admin').headers['Token']
    response = get_md_video_out_background(token)
    if response.json()['Code'] != 200:
        print('Get video out background in Fail!')
        return False
    DeviceId = response.json()["VideoOuts"][0]["DeviceId"]
    return DeviceId


def create_UI():
    TOKEN = post_auth(username='admin', password='admin').headers['Token']
    databody["DeviceId"] = get_background_DeviceId()
    databody["Background"] = "/home/user/EST/MCSScripts/background.png"
    response = post_md_background(TOKEN, databody)

    if response.json()['Code'] == 200:
        print('create Background Pass!')
    else:
        print('create Background Fail!')


def delete_create_UI():
    TOKEN = post_auth(username='admin', password='admin').headers['Token']
    # get video out DeviceId and set for post request
    databody["DeviceId"] = get_background_DeviceId()
    databody["Background"] = "/home/user/EST/MCSScripts/background.png"
    response = post_md_background(TOKEN, databody)

    if response.json()['Code'] == 400:
        print('background picture not exist!')
    else:
        print('delete Background Success!')


def main():
    create_UI()  # 创建背景图片
    sshctrl()  # 删除背景图片
    delete_create_UI()  # 再次下发删除的图片，变为桌面


if __name__ == '__main__':
    main()
