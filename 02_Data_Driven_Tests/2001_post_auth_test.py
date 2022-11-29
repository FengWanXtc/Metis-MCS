import sys
import os
import requests
import prettytable
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Scence description", "UserName", "Password", "Actual Code", "Actual Message", "Expect Result"]
table.align = "c"

expectResult_200 = {"Code": 200,"Message": "No error found!"}

expectResult_400 = {"Code": 400,"Message": "Bad parameter!"}

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


def show_post_auth_table():
    # 1
    response = post_auth(username="admin", password="admin")
    table.add_row(["正常用户名和密码", "admin", "admin", response.json()["Code"], response.json()["Message"], expectResult_200])

    # 2
    response = post_auth(username="", password="admin")
    table.add_row(["UserName为空", "", "admin", response.json()["Code"], response.json()["Message"], expectResult_400])

    # 3
    response = post_auth(username=111, password="admin")
    table.add_row(
        ["UserName为整型", "111(Int)", "admin", response.json()["Code"], response.json()["Message"], expectResult_400])

    # 4
    databody = {"Password": "admin"}
    response = post_auth_by_body(databody)
    table.add_row(
        ["删除UserName字段", "////////", "admin", response.json()["Code"], response.json()["Message"], expectResult_400])

    # 5
    response = post_auth(username="", password="admin")
    table.add_row(["Password为空", "admin", "", response.json()["Code"], response.json()["Message"], expectResult_400])

    # 6
    response = post_auth(username="admin", password=222)
    table.add_row(
        ["Password为整型", "admin", "222(Int)", response.json()["Code"], response.json()["Message"], expectResult_400])

    # 7
    databody = {'UserName': "admin"}
    response = post_auth_by_body(databody)
    table.add_row(
        ["删除Password字段", "admin", "////////", response.json()["Code"], response.json()["Message"], expectResult_400])

    # 8
    response = post_auth(username="user", password="user")
    table.add_row(
        ["用户名和密码不为admin", "user", "user", response.json()["Code"], response.json()["Message"], expectResult_400])

    # 9
    # 修改用户名
    token = post_auth(username='admin', password='admin').headers['Token']
    post_auth_modify("eswin_xtc", "xtc", token)
    # 再次用原来的 admin 登录
    response = post_auth(username="admin", password="admin")
    table.add_row(
        ["修改账户后使用旧账户", "admin", "admin", response.json()["Code"], response.json()["Message"], expectResult_400])
    # 用新的用户名登录
    response = post_auth(username="eswin_xtc", password="xtc")
    table.add_row(
        ["使用新的用户名密码", "eswin_xtc", "xtc", response.json()["Code"], response.json()["Message"], expectResult_200])

    # 10 恢复原来的用户名和密码
    token = post_auth(username='eswin_xtc', password='xtc').headers['Token']
    post_auth_modify("admin", "admin", token)

    print(table)


if __name__ == '__main__':
    show_post_auth_table()
