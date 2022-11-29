import os

import paramiko
import requests


def sshclient_execmd(execmd,IP):
    error='paramiko connect fail , EOFError'
    s = paramiko.SSHClient()  # 创建SSH对象
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接主机
    try:
        s.connect(hostname=IP, port=22, username='user', password='User@1949!')  # 连接服务器
    except:
        print("链接错误")
        return error
    stdin, stdout, stderr = s.exec_command(execmd)  # 执行命令
    # stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
    outputBytes = stdout.read() + stderr.read()
    outputStr = outputBytes.decode("latin1")
    s.close()  # 关闭连接
    return outputStr




if __name__ == '__main__':
    IP = input("Please Input Metis IP: ")
    execmd = 'cat /etc/agent/etc/media-agent/mioscfg.json'
    outputStr = sshclient_execmd(execmd,IP)
    print(outputStr)
