import requests
import environmentlib

# ***********Get the IP Address*************
# Please run this script in metis station

HEADERS = {'Content-type': 'application/json'}
HOST_IP = environmentlib.check_eth_connect()

url = "http://{}:6689/mediadevice".format(HOST_IP)


# *******************************************************************************
# *                                  MCS 0.3                                    *
# *******************************************************************************
def post_md_audio_in_config(ip, databody, token=''):
    if ip == '':
        ip = HOST_IP
    temp_url = "http://{}:6689/mediadevice/audio/in/configuration".format(ip)
    temp_headers = HEADERS
    if token != '':
        temp_headers['Token'] = token
    response = requests.post(url=temp_url, headers=temp_headers, json=databody)
    return response


def get_md_audio_in(token='', ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    temp_url = 'http://{}:6689/mediadevice/audio/in'.format(ip)
    temp_headers = HEADERS

    if token != '':
        temp_headers['Token'] = token
    response = requests.get(url=temp_url, headers=temp_headers, json={})

    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, {}, response.json(), "GET")
    # 生成file文件
    return response


def get_md_audio_out(token='', ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    tempurl = 'http://{}:6689/mediadevice/audio/out'.format(ip)
    databody = {}
    tempheaders = HEADERS
    if token != '':
        tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)

    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")
    return response


def get_md_video_in(token='', ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediadevice/video/in".format(ip)
    databody = {}
    tempheaders = HEADERS
    if token != '':
        tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")

    return response


def get_md_video_out(token='', ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediadevice/video/out".format(ip)
    databody = {}
    tempheaders = HEADERS
    if token != '':
        tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")
    return response


def get_md_audio_in_capability(token='', ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    tempurl = 'http://{}:6689/mediadevice/audio/in/capability'.format(ip)
    databody = {}
    tempheaders = HEADERS
    if token != '':
        tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")
    return response


def get_md_audio_out_capability(token='', ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    tempurl = 'http://{}:6689/mediadevice/audio/out/capability'.format(ip)
    databody = {}
    tempheaders = HEADERS
    if token != '':
        tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")
    return response


def get_md_video_in_capability(token='', ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    tempurl = 'http://{}:6689/mediadevice/video/in/capability'.format(ip)
    databody = {}
    tempheaders = HEADERS
    if token != '':
        tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")
    return response


def get_md_video_out_capability(token='', ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    tempurl = 'http://{}:6689/mediadevice/video/out/capability'.format(ip)
    databody = {}
    tempheaders = HEADERS
    tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")
    return response


def get_md_video_out_background(token='', ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    tempurl = 'http://{}:6689/mediadevice/video/out/background'.format(ip)
    databody = {}
    tempheaders = HEADERS
    tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")
    return response


def get_md_list(token='', ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediadevice/list".format(ip)
    databody = {}
    tempheaders = HEADERS
    if token != '':
        tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")
    return response


def get_md_audio_in_cfg(token='', ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediadevice/audio/in/configuration".format(ip)
    databody = {}
    tempheaders = HEADERS
    if token != '':
        tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")
    return response


def get_md_audio_out_cfg(token='', ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediadevice/audio/out/configuration".format(ip)
    databody = {}
    tempheaders = HEADERS
    if token != '':
        tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")
    return response


def get_md_director_strategy(token='', ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediadevice/director-strategy".format(ip)
    databody = {}
    tempheaders = HEADERS
    if token != '':
        tempheaders['Token'] = token
    response = requests.get(url=tempurl, headers=tempheaders, json=databody)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, databody, response.json(), "GET")
    return response


def post_md_background(data, token="", ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    tempurl = "http://{}:6689/mediadevice/video/out/background".format(ip)
    tempheaders = HEADERS
    if token != '':
        tempheaders['Token'] = token
    response = requests.post(url=tempurl, headers=tempheaders, json=data)
    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, data, response.json(), "POST")
    return response


def mediadevice_request(data: dict, api: str, function: str, token='', ip=HOST_IP):
    if ip == '':
        ip = HOST_IP
    temp_url = "http://{IP}:6689/mediadevice/{API}".format(IP=ip, API=api)
    temp_headers = HEADERS
    if token != '':
        temp_headers['Token'] = token

    if function == 'POST':
        response = requests.post(url=temp_url, headers=temp_headers, json=data)
    elif function == 'GET':
        response = requests.get(url=temp_url, headers=temp_headers, json=data)
    else:
        raise ValueError("请求类型错误!请使用POST或者GET")

    if environmentlib.Whether_Log_File is not False:
        environmentlib.log_file(response.url, data, response.json(), "POST")
    return response


if __name__ == '__main__':
    res = mediadevice_request({}, "video/out/background", "GET")
    print(res.json())
