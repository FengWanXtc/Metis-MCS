import sys

sys.path.append('../../Libraries')
from functionlib import *

Near_IP = input("Please Input Near-End Metis IP: ")
Far_IP = input("Please Input Far-End Metis IP: ")
Anno = "************************************"

scriptlist = ['4F-4.1DR-4.2S-4.3T-4.4RT.py -ip={}'.format(Near_IP),
              'Director_push.py -t={} -ip={}'.format(Near_IP, Far_IP),
              'suspend.py -mn=Basic_MCS -ip={} -sn=Director_Record,Teacher_Record,Student_Record,ComputerAi_Record'.format(
                  Near_IP),
              'resume.py -mn=Basic_MCS -ip={} -sn=Director_Record,Teacher_Record,Student_Record,ComputerAi_Record'.format(
                  Near_IP),
              'remove.py -mn=Basic_MCS -ip={} -sn=Director_Record,Teacher_Record,Student_Record,ComputerAi_Record'.format(
                  Near_IP)
              ]

if __name__ == '__main__':
    # 烂代码^ ^
    os.system('python {}'.format(scriptlist[0]))
    time.sleep(5)
    os.system('python {}'.format(scriptlist[1]))
    time.sleep(5)
    start_time = time.time()
    count = 0

    while True:
        end_time = time.time()
        if end_time - start_time > 300:
            print(Anno + "\nLoop Task Ends. Loop For *{}* Times. Remove Four Record Spec.\n".format(str(count)) + Anno)
            os.system('python delete_all_tasks.py -ip={}'.format(Near_IP))
            os.system('python delete_all_tasks.py -ip={}'.format(Far_IP))
            break
        else:
            print(":: The Present Loop Time is {} .".format(str(count)))
            os.system('python {}'.format(scriptlist[2]))
            # 等待30秒后继续录制
            time.sleep(30)
            os.system(
                'python {}'.format(scriptlist[3]))
            # 录制60秒后继续暂停
            time.sleep(60)
            count += 1
