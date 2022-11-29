import sys
import os
sys.path.append('../../Libraries')
from functionlib import *


def main():
    data = read_json_file('change_geometry_animation.json')['change_geometry_animation']
    for item in data:
        # print("python change_geometry.py -n={} -g={}".format(item[0], item[1]))
        if os.system("python change_geometry.py -n={} -g={}".format(item[0], item[1])):
            print("Change Geometry Animation Fail.")


if __name__ == '__main__':
    main()
