import argparse
import sys
sys.path.append('../../Libraries')
from functionlib import *
from mediatasklib import *


def read_json_file(filename):
    # path = os.path.abspath(os.path.join(os.getcwd(), "../json_templates/"))
    path = 'json_gen'
    filepath = path + '/' + filename
    file = open(filepath, 'r')
    data = json.load(file)
    return data

def S1E2_test():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip
    S1E2_data = read_json_file('Near_preview_pushpull.json')
    # 根据算法获取DeviceId
    # print(json.dumps(S1E2_data, indent=2))
    Teacher_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType='HDMI', aiStrategy='teacher')
    S1E2_data['VideoSpecs'][0]['DeviceId'] = Teacher_DeviceId
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType='IPC', aiStrategy='student')
    S1E2_data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    blackboard_DeviceId = get_DeviceId_by_aiStrategy(ip=IP, camType='IPC', aiStrategy='blackboard')
    S1E2_data['VideoSpecs'][3]['DeviceId'] = blackboard_DeviceId

    # print(json.dumps(S1E2_data, indent=2))

    try:
        response = post_mt_create_update(ip=IP, data=S1E2_data)
    except:
        print('Post Create Task Failed')
        print(response.status_code)
        return False

    if (response.json()['Code'] == 201):
        print('Create Update (Near_preview_pushpull) Success')
        return True
    else:
        print('Create Update (Near_preview_pushpull) Fail')
        print(response.json())
        return False


if __name__ == '__main__':
    S1E2_test()
