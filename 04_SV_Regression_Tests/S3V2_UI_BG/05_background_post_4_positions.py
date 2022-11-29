import sys
sys.path.append('../../Libraries')
from functionlib import *
from mediatasklib import *


def main():
    data = read_json_file('05_background_post_4_positions.json')
    # print(json.dumps(data))
    response = post_mt_create_update(ip="", data=data)
    if response.json()['Code'] == 201:
        print('Step 1: Post 4 Frames Task Success')
    else:
        print('Step 1: Post 4 Frames Task Fail')
        print(response.json())
        return False

    time.sleep(2)

    # 动态替换背景
    data["RenderSpecs"][0]["Background"] = "null"
    response = post_mt_create_update(ip="", data=data)
    if response.json()['Code'] == 201:
        print('Step 2: Post UI Background Success')
    else:
        print('Step 2: Post UI Background Fail')
        print(response.json())
        return False


if __name__ == '__main__':
    main()
