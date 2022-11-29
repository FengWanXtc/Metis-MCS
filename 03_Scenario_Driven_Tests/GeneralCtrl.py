import argparse
import sys
sys.path.append('../Libraries')
import environmentlib
# 此脚本为功能配置脚本，目前支持 logfile功能
# 后续可以扩展其余新功能


def main():
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-logfile', type=str, default="OFF", help='LogFile Name')
    args = parser.parse_args()
    LOGFILE = args.logfile

    if LOGFILE == "OFF":
        # 如果是OFF，则关闭Logfile功能
        environmentlib.modify_cfg("IsLogFile", False)
    else:
        # 此步骤是设置LogFile
        environmentlib.modify_cfg("IsLogFile", True)
        environmentlib.modify_cfg("FileName", LOGFILE)


if __name__ == '__main__':
    main()
