import sys
sys.path.append('../../Libraries')
from authlib import *
from mediadevicelib import *
from prettytable import PrettyTable


Split_Line = "\n\n**********************************************************************************************\n"


def show_strategy():
    token = post_auth(username='admin', password='admin').headers['Token']
    response = get_md_director_strategy(token)
    if response.status_code == 200:
        print('\n' + 'Get director strategy success! \n')
    else:
        print('\n' + 'Get director strategy  Fail! ')
        return False
    try:
        for item in response.json():
            table = PrettyTable()
            table.field_names = ["State", "Priority", "VideoSource", "Delay", "Hold", "Timeout"]
            print("[Scenario] <{}>  Template is <{}>. Strategy As follows: \n".format(item['Scenario'], item['FrameSpec']['Template']))
            SelectionSpecs = item["FrameSpec"]['LayoutSpecs'][0]['SelectionSpecs']
            for SelectionSpec in SelectionSpecs:
                table.add_row([SelectionSpec["State"], SelectionSpec["Priority"], SelectionSpec['VideoSource'], SelectionSpec['Delay'], SelectionSpec['Hold'], SelectionSpec['Timeout']])
            print(table, Split_Line)
    except:
        print('None result was found!')
        return False


if __name__ == '__main__':
    show_strategy()
