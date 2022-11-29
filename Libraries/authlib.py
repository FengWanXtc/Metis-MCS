import requests
import environmentlib


# ***********Get the IP Address*************
# Please run this script in metis station
HOST_IP = environmentlib.check_eth_connect()
url = "http://{}:6689/auth".format(HOST_IP)


def post_auth(username='admin', password='admin'):
    tempurl = url
    databody = {'UserName': username, 'Password': password}

    headers = {'Content-type': 'application/json'}
    response = requests.post(url=tempurl, headers=headers, json=databody)
    return response


def post_auth_modify(newname, newpassword, token):
    tempurl = url + '/modify'
    databody = {'NewName': newname, 'NewPassword': newpassword}
    headers = {'Content-type': 'application/json', 'Token': token}
    response = requests.post(tempurl, headers=headers, json=databody)
    return response


# For example by using above API
def get_token():
    token = post_auth('admin', 'admin').headers['Token']
    return token
