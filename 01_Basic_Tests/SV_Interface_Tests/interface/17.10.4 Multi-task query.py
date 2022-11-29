import requests


def get_requests(IP):
    data = {
        "url": "http://{}:6689/mediatask/create_update".format(IP),
        "header": {'Content-type': 'application/json'},
        "body": {
            "Name": "metis_live_mcs",
            "Type": "MCS",
            "Description": "Pipeline task for metis live",
            "Version": "0.3",
            "RenderSpecs": [
                {
                    "Name": "Render",
                    "DeviceId": "0800-0000",
                    "CompositionSpec": [
                        {
                            "Geometry": [
                                960,
                                540,
                                1920,
                                1080
                            ],
                            "SourceName": "Student"
                        }
                    ]
                }
            ]
        }
    }
    r = requests.post(data["url"], headers=data["header"], json=data['body'])
    print(r.json())
    true = True
    false = False
    data = {
        "url": "http://{}:6689/mediatask/tasks".format(IP),
        "header": {'Content-type': 'application/json'},
        "body": {}
    }
    try:
        r = requests.get(data["url"], headers=data["header"], json=data['body'])
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