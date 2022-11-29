import sys
import os
import requests
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Scene description", "NewName", "NewPassword", "Code", "Message"]
table.align = "l"

if sys.platform.startswith("win"):
    HOST_IP = '10.12.224.135'
else:
    ip_get_cmd = "ifconfig eth0 | grep 'inet ' | awk '{print $2}'"
    HOST_IP = os.popen(ip_get_cmd).read().strip()

url = "http://{}:6689/auth".format(HOST_IP)


def post_auth(username, password):
    tempurl = url
    databody = {'UserName': username, 'Password': password}

    headers = {'Content-type': 'application/json'}
    response = requests.post(url=tempurl, headers=headers, json=databody)
    return response


def post_auth_by_body(body):
    tempurl = url
    databody = body
    headers = {'Content-type': 'application/json'}
    response = requests.post(url=tempurl, headers=headers, json=databody)
    return response


def post_auth_modify(newname, newpassword, token):
    tempurl = url + '/modify'
    databody = {'NewName': newname, 'NewPassword': newpassword}
    headers = {'Content-type': 'application/json', 'Token': token}
    response = requests.post(tempurl, headers=headers, json=databody)
    return response


def show_post_auth_modify_table():
    userName = 'admin'
    passWord = 'admin'
    # 1
    response = post_auth(username=userName, password=passWord)
    token = response.json()["Token"]
    table.add_row(["修改新用户名", "eswin_xtc", "xtc", response.json()["Code"], response.json()["Message"]])
    # 修改新用户名和密码
    userName, passWord = "eswin_xtc", "xtc"
    post_auth_modify(userName, passWord, token)
    # 2
    response = post_auth(username=userName, password=passWord)
    token = response.json()["Token"]

    print(table)


if __name__ == '__main__':
    show_post_auth_modify_table()
