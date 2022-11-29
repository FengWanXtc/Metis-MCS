import sys
import threading

sys.path.append('../../Libraries')
from functionlib import *

# Near_IP = input("Please Input Near-End Metis IP: ")
# Far_IP = input("Please Input Far-End Metis IP: ")
Near_IP = "10.12.224.135"
Far_IP = "10.12.224.140"

scriptlist = [
    # preprocess json
    'preprocess.py -Far_IP={} -Near_IP={}'.format(Far_IP, Near_IP),

    # Far wp pull 2(video&audio)
    'create_update.py -ip={} -mn=Basic_MCS -jf=Far_wppull_norecord'.format(Far_IP),

    # Near wp push 2(video&audio) and pull 6(video&audio)
    'Near_preview_pushpull.py -ip={}'.format(Near_IP),
    # Far wp push 6(video&audio)
    'create_update.py -ip={} -mn=Basic_MCS -jf=Far_wppush'.format(Far_IP),

    # change position
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_change_positition_0'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_change_positition_0_1'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_change_positition_0_2'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_change_positition_0_3'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_change_positition_1'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_change_positition_2'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_change_positition_3'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_change_positition_4'.format(Near_IP),

    # preview and record alone
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_preview_before_record'.format(Near_IP),

    # start record
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_record'.format(Near_IP),

    # record process
    'suspend.py -ip={} -mn=Basic_MCS -jf=Near_record_process_0'.format(Near_IP),
    'suspend.py -ip={} -mn=Basic_MCS -jf=Near_record_process_1'.format(Near_IP),
    'suspend.py -ip={} -mn=Basic_MCS -jf=Near_record_process_2'.format(Near_IP),
    'suspend.py -ip={} -mn=Basic_MCS -jf=Near_record_process_3'.format(Near_IP),

    'resume.py -ip={} -mn=Basic_MCS -jf=Near_record_process_0'.format(Near_IP),
    'resume.py -ip={} -mn=Basic_MCS -jf=Near_record_process_1'.format(Near_IP),
    'resume.py -ip={} -mn=Basic_MCS -jf=Near_record_process_2'.format(Near_IP),
    'resume.py -ip={} -mn=Basic_MCS -jf=Near_record_process_3'.format(Near_IP),

    'remove.py -ip={} -mn=Basic_MCS -jf=Near_record_process_0'.format(Near_IP),
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_record_process_1'.format(Near_IP),
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_record_process_2'.format(Near_IP),
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_record_process_3'.format(Near_IP),

    # clear local push and far pull
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_server_remove'.format(Near_IP),
    'remove.py -ip={} -mn=Basic_MCS -jf=Far_wppull_norecord_remove'.format(Far_IP),

    # compose 2
    'create_update.py -ip={} -mn=Basic_MCS -jf=Far_wppull'.format(Far_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_compose_2'.format(Near_IP),

    # compose 2 picture in picture
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_compose_remove'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_compose_2_in'.format(Near_IP),
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_compose_remove'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_compose_2_in_change_0'.format(Near_IP),
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_compose_remove'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_compose_2_in_change_1'.format(Near_IP),
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_compose_remove'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_compose_2_in_change_2'.format(Near_IP),

    # compose 3
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_compose_remove'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_compose_3'.format(Near_IP),

    # compose 4
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_compose_remove'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_compose_4'.format(Near_IP),

    # compose tcp clear
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_compose_remove_all'.format(Near_IP),
    'remove.py -ip={} -mn=Basic_MCS -jf=Far_wppull_remove'.format(Far_IP),



    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_compose_2_rtmp'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Far_pull_rtmp'.format(Far_IP),
    'remove.py -ip={} -mn=Basic_MCS -jf=Far_pull_rtmp_remove'.format(Far_IP),

    # compose 2 rtmp picture in picture
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_compose_remove_rtmp'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_compose_2_rtmp_in'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Far_pull_rtmp'.format(Far_IP),
    'remove.py -ip={} -mn=Basic_MCS -jf=Far_pull_rtmp_remove'.format(Far_IP),

    # compose 3 rtmp
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_compose_remove_rtmp'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_compose_3_rtmp'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Far_pull_rtmp'.format(Far_IP),
    'remove.py -ip={} -mn=Basic_MCS -jf=Far_pull_rtmp_remove'.format(Far_IP),

    # compose 4 rtmp
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_compose_remove_rtmp'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_compose_4_rtmp'.format(Near_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Far_pull_rtmp'.format(Far_IP),

    # compose clear
    'remove.py -ip={} -mn=Basic_MCS -jf=Far_pull_rtmp_remove'.format(Far_IP),
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_compose_remove_rtmp_all'.format(Near_IP),

    # start transform
    'create_update.py -ip={} -mn=Basic_MCS -jf=Far_wppull_transform'.format(Far_IP),
    'create_update.py -ip={} -mn=Basic_MCS -jf=Near_compose_transform'.format(Near_IP),

    # stop record
    'remove.py -ip={} -mn=Basic_MCS -jf=Far_wppull_record_stop'.format(Far_IP),
    'remove.py -ip={} -mn=Basic_MCS -jf=Near_compose_transform_record_stop'.format(Near_IP)
    ]


def act_basic(ScriptList, sleeptime=5):
    for items in ScriptList:
        os.system('python {}'.format(items))
        time.sleep(sleeptime)


if __name__ == '__main__':
    act_basic(scriptlist, sleeptime=5)
