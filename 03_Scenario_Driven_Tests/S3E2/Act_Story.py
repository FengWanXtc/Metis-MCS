import sys
sys.path.append('../../Libraries')
from functionlib import *

    
def act():
    print("********Start Create four remote frames********")
    os.system('python create_frames_1by1.py')
    IP = input('Please input a Host IP to Push Stream: \n')
    os.system('python remote_push.py -ip={}'.format(IP))


if __name__ == '__main__':
    act()