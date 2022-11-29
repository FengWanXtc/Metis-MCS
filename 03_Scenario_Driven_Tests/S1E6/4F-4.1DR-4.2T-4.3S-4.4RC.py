import sys
sys.path.append('../../Libraries')
from environmentlib import *
from mediatasklib import *
from functionlib import *

TeacherCamType = Global_TeacherCamType
StudentCamType = Global_StudentCamType


def basic():
    data = read_json_file('4F-4.1DR-4.2T-4.3S-4.4RC.json')
    # 根据算法获取DeviceId
    # print(json.dumps(S1E2_data, indent=2))
    Teacher_DeviceId = get_DeviceId_by_aiStrategy(ip='', camType=TeacherCamType, aiStrategy='teacher')
    data['VideoSpecs'][0]['DeviceId'] = Teacher_DeviceId
    Student_DeviceId = get_DeviceId_by_aiStrategy(ip='', camType=StudentCamType, aiStrategy='student')
    data['VideoSpecs'][1]['DeviceId'] = Student_DeviceId
    # print(json.dumps(data, indent=2))

    try:
        response = post_mt_create_update(ip='', data=data)
    except:
        print('Post Create Task Failed')
        print(response.status_code)
        return False

    if (response.json()['Code'] == 201):
        print('S1E2 Test Success')
        return True
    else:
        print('S1E2 Test Fail')
        print(response.json())
        return False


if __name__ == '__main__':
    basic()
