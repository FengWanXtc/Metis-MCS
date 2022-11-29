import json

import requests
import environmentlib

# ***********Get the IP Address*************
# Please run this script in metis station
headers = {'Content-type': 'application/json'}
HOST_IP = environmentlib.check_eth_connect()


# ************MCS 0.3 Update*****************
def post_mt_create_update(ip, token='', data={}):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediatask/create_update".format(ip)
    databody = data
    tempheaders = headers
    # At present ,we don't use token.
    if token != '':
        tempheaders['Token'] = token
    response = requests.post(url=tempurl, headers=tempheaders, json=databody)

    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, data, response.json(), "POST")
    return response


def delete_mt_MCS_Name(ip, MCS_Name, token=''):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediatask/{}".format(ip, MCS_Name)
    databody = {}
    tempheaders = headers
    # At present ,we don't use token.
    if token != '':
        tempheaders['Token'] = token
    response = requests.delete(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "DELETE")
    return response


def get_mt_tasks(ip, token=''):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediatask/tasks".format(ip)
    databody = {}
    tempheaders = headers
    # At present ,we don't use token.
    if token != '':
        tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)

    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")
    return response


def post_mt_inspection(ip, name, token=''):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediatask/inspection".format(ip)
    databody = {"Name": name}
    tempheaders = headers
    if token != '':
        tempheaders['Token'] = token
    response = requests.post(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "POST")
    return response


def post_mt_remove(ip, data, token=''):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediatask/remove".format(ip)
    databody = data
    tempheaders = headers
    if token != '':
        tempheaders['Token'] = token
    response = requests.post(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "POST")
    return response


def post_mt_suspend(ip, data, token=''):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediatask/suspend".format(ip)
    databody = data
    tempheaders = headers
    if token != '':
        tempheaders['Token'] = token
    response = requests.post(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "POST")
    return response


def post_mt_resume(ip, data, token=''):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediatask/resume".format(ip)
    databody = data
    tempheaders = headers
    if token != '':
        tempheaders['Token'] = token
    response = requests.post(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "POST")
    return response
