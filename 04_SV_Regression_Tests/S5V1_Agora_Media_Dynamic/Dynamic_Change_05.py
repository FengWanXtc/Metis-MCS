import argparse
import sys

sys.path.append('../../Libraries')
from functionlib import *
from mediatasklib import *


def mcs_task(host_ip):
    mcs_data = read_json_file('Dynamic_Change_05.json')
    # print(json.dumps(mcs_data, indent=2))
    task_name = get_mt_tasks(ip=host_ip).json()['Names'][0]
    mcs_data['Name'] = task_name

    # Remove Render Part
    print("Remove Render And Sleep 5 seconds")
    remove_data = {"Name": task_name, "SpecNames": ["Render_test"]}
    res = post_mt_remove(ip=host_ip, data=remove_data)
    time.sleep(5)
    # Re Create Render
    response = post_mt_create_update(ip=host_ip, data=mcs_data)
    if response.json()['Code'] == 201:
        print('Dynamic Change 05 MCS *{}* Post to Remove And Recover Render Success'.format(task_name))
        return True
    else:
        print('Dynamic Change 05 MCS *{}* Post to Remove And Recover Render Fail'.format(task_name))
        print(response.json())
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python3 delete_all_tasks --ip=10.12.224.135')
    parser.add_argument('-ip', type=str, default='', help='The IP address of the METIS')
    args = parser.parse_args()
    IP = args.ip
    mcs_task(IP)
