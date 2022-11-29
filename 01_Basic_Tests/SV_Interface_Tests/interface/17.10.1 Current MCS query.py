import requests

def get_requests(IP):
    true = True
    false = False
    data = {
        "url": "http://{}:6689/mediatask/inspection".format(IP),
        "header": {'Content-type': 'application/json'},
        "body": {
            "Name": "metis_live_mcs"
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
    IP = input("Please Input Metis IP: ")
    get_requests(IP)