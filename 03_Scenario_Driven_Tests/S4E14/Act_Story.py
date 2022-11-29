import os
import sys

sys.path.append('../../Libraries')
from functionlib import *

scriptlist = [
    'Record_Time.py -u=120 -rt=610 -fn=2Min',
    'Record_Size.py -u=15728640 -rt=1210 -fn=15MB',
    'Record_Time.py -u=300 -rt=1810 -fn=5Min',
    'Record_Size.py -u=104857600 -rt=3610 -fn=100MB',
    'Record_Time.py -u=2700 -rt=10810 -fn=45Min',
    'Record_Size.py -u=524288000 -rt=14410 -fn=500MB',
]
scL = [
    'Record_Size.py -u=5242880 -rt=605 -fn=5MB  -ip=10.12.224.135',
    'Record_Size.py -u=10485760 -rt=605 -fn=10MB  -ip=10.12.224.135',
    'Record_Size.py -u=15728640 -rt=905 -fn=15MB  -ip=10.12.224.135',
    'Record_Size.py -u=20971520 -rt=1205 -fn=20MB  -ip=10.12.224.135',
    'Record_Size.py -u=104857600 -rt=1805 -fn=100MB -ip=10.12.224.135',
]

# 'Record_Size.py -u=15728640 -rt=1210 -fn=15MB  -ip=10.12.224.47'
#    'Record_Size.py -u=104857600 -rt=3610 -fn=100MB -ip=10.12.224.47',
#    'Record_Size.py -u=524288000 -rt=14410 -fn=500MB -ip=10.12.224.47'
# 分段2分钟录制10分钟（10秒Buffer）
# 分段15MB录制20分钟（10秒Buffer）
# 分段5分钟录制30分钟（10秒Buffer）
# 分段100MB录制60分钟（10秒Buffer）
# 分段45分钟录制180分钟（10秒Buffer）
# 分段500MB录制240分钟（10秒Buffer）
def act_wqf():
    for i in range(1, 51):
        os.system('python Record_Size.py -u=60000000 -rt=33 -fn=30Sec -ip=10.12.224.60')

    print("Ends!!!!!!!")


def act_basic(ScriptList, sleeptime=60):
    # 先依次执行前面操作
    for items in ScriptList:
        os.system('python {} -ip=10.12.224.43' .format(items))
        # print(items)
        time.sleep(sleeptime)


if __name__ == '__main__':
    # act_basic(scriptlist, sleeptime=60)
    # act_wqf()
    act_basic(scL, sleeptime=60)
