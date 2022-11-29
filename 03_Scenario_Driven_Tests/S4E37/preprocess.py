import sys
import threading
import random
import argparse
import json
import os
sys.path.append('../../Libraries')
from functionlib import *
from mediatasklib import *

cameras = ["Director", "Teacher", "Teacher_Ai", "Student", "Student_Ai", "Blackboard", "Blackboard_Ai", "Computer", "Computer_Ai"]
true_cam = ["Teacher", "Student", "Blackboard", "Computer"]
random_ = random.sample(cameras, 7) #0 __push__, 1 __preview__ , 2 __record__ , 3 __otherpreview1__ , 4 __otherpreview2__, 5, __otherpreview3__, 6 __otherpreview4__
regu_str = ["__push__", "__preview__", "__record__", "__otherpreview1__", "__otherpreview2__", "__otherpreview3__", "__otherpreview4__"]
compose = random.sample(true_cam, 1)

def process(random_, Far_IP, Near_IP):
    jsonfiles = os.listdir("./json_templates")
    for jsonfile in jsonfiles:
        with open("json_templates/" + jsonfile, 'r') as f:
            jsoncontent = f.readlines()
            jsoncontent_str = "".join(jsoncontent)
            for i in range(7):
                jsoncontent_str = jsoncontent_str.replace(regu_str[i], random_[i])
        jsoncontent_str = jsoncontent_str.replace("__Far_IP__", Far_IP)
        jsoncontent_str = jsoncontent_str.replace("__Near_IP__", Near_IP)
        jsoncontent_str = jsoncontent_str.replace("__compose__", compose[0])
        with open("json_gen/" + jsonfile, 'w') as f:
            f.write(jsoncontent_str)
            

def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 create_one_frame_preview.py -n=teacher -ct=HDMI -cn=0 -g=0,0,960,540')
    parser.add_argument('-Far_IP', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('-Near_IP', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    Far_IP = args.Far_IP
    Near_IP = args.Near_IP

    process(random_, Far_IP, Near_IP)


if __name__ == '__main__':
    main()