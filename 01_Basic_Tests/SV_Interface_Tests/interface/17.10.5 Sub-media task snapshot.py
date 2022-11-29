import os

import requests


def get_requests(IP):
    true = True
    false = False
    data = {
        "url": "http://{}:6689/mediatask/snapshot".format(IP),
        "header": {'Content-type': 'application/json'},
        "body": {
            "Name": "metis_live_mcs",
            "SourceName": "Remote_pull",
            "Format": "png",
            "Path": "R_yyyy-mm-dd-hh-mm-ss.png"
        }
    }
    try:
        r = requests.post(data["url"], headers=data["header"], json=data['body'])
        if r.json()['Code'] == 200:
            print(r.json())
            print("接口测试正常！")
        else:
            print(r.json())
    except Exception as e:
        print(e)




if __name__ == '__main__':
    print("先删除所有任务！")
    os.system('python delete_all_tasks.py')
    print("启动近端preview！")
    os.system('python create_preview.py')
    print("启动远端preview！")
    os.system('python create_remote.py')
    IP = input("Please Input Metis IP: ")
    get_requests(IP)
