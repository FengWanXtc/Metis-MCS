import sys
import argparse

sys.path.append('../../Libraries')
from functionlib import *
from mediatasklib import *


def push_record(argc_ip, mcsname, specName):
    # 封装的读取json文件的函数,保存为一个字典对象data
    data = {"Name": mcsname, "SpecNames": specName}

    # ***print可以用于查看MCS是怎么样的***
    # print(json.dumps(data, indent=2))

    try:
        response = post_mt_suspend(ip=argc_ip, data=data)
    except:
        print('Suspend MCS ({}) SpecName {} Failed'.format(mcsname, specName))
        print(response.status_code)
        return False

    if response.json()['Code'] == 200:
        print('Suspend MCS ({}) SpecName ({}) Success'.format(mcsname, specName))
        return True
    else:
        print('Suspend MCS ({}) SpecName ({}) Fail'.format(mcsname, specName))
        print(response.json())
        return False


def main():
    parser = argparse.ArgumentParser(
        description='usage: python3 XXXX.py -mn=XXXX -sn=XXXX -ip=XXXX')
    # 指定哪个HDMI口
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    parser.add_argument('--mcsname', '-mn', type=str, default='Basic_MCS', help='The name of MCS,default is MCSV3')
    parser.add_argument('--specname', '-sn', type=str, default='',
                        help='SpecNames, split by "," ')
    args = parser.parse_args()
    IP = args.ip
    MCSNAME = args.mcsname
    SPECNAME = args.specname.split(',')
    push_record(IP, MCSNAME, SPECNAME)


if __name__ == '__main__':
    main()
