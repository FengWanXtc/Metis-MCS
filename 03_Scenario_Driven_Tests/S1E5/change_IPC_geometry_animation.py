import sys
sys.path.append('../../Libraries')
from functionlib import *


def main():
    data = read_json_file('change_IPC_geometry_animation.json')['Geometry_animation']
    for item in data:
        str_item = ''
        for list_item in item:
            str_item += str(list_item) + ','
        geometry = str_item[:-1]
        if os.system("python change_IPC_geometry.py -g={}".format(geometry)):
            print("Change Geometry Animation Fail.")


if __name__ == '__main__':
    main()
