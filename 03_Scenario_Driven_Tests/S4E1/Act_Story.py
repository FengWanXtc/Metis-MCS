import argparse
import sys

sys.path.append('../../Libraries')
from environmentlib import *
from functionlib import *


def act_basic(ScriptList, sleeptime=5):
    # 先依次执行前面操作
    for items in ScriptList:
        os.system('python {}'.format(items))
        # print(items)
        # input("Press  Enter  Key  to  do Next")
        time.sleep(sleeptime)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-Nip', type=str, default=Global_NearEnd, help='The Near_End IP address of the METIS')
    parser.add_argument('-Fip', type=str, default=Global_FarEnd, help='The Far_End IP address of the METIS')
    parser.add_argument('-TCam', type=str, default=Global_TeacherCamType, help='The Teacher Cam Type')
    parser.add_argument('-SCam', type=str, default=Global_StudentCamType, help='The Student Cam Type')
    parser.add_argument('-BCam', type=str, default=Global_BlackBoardCamType, help='The Blackboard Cam Type')
    args = parser.parse_args()
    NIP = args.Nip
    FIP = args.Fip
    SCAM = args.SCam
    TCAM = args.TCam

    scriptlist = [
        'Basic.py -ip={NearIp} -TCam={TCAM} -SCam={SCAM}'.format(NearIp=NIP, TCAM=TCAM, SCAM=SCAM),
        'Far_Push.py -ip={FarIp} -TCam={TCAM} -SCam={SCAM}'.format(FarIp=FIP, TCAM=TCAM, SCAM=SCAM),
        'remove.py -mn=Basic_MCS -sn=Rtc_Spec -ip={}'.format(NIP),
        'create_update.py -mn=Basic_MCS -jf=Transform -ip={}'.format(NIP),
        'delete_all_tasks.py -ip={}'.format(NIP),
        'delete_all_tasks.py -ip={}'.format(FIP)
    ]
    act_basic(scriptlist, sleeptime=10)
