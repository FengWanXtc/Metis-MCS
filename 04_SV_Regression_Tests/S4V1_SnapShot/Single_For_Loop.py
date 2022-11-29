import os
import time

if __name__ == '__main__':
    TestList = {"Teacher": "NULL", "Teacher_Ai": "NULL", "Computer": "NULL", "Blackboard": "NULL",
                "Student": "NULL", "Student_Ai": "NULL", "Computer_Ai": "NULL", "Blackboard_Ai": "NULL",
                "Director": "NULL", "TcpVideoA_pull": "NULL", "TcpVideoB_pull": "NULL", "TcpVideoC_pull": "NULL"
                }
    for item in TestList.items():
        print(item.keys())
    print(TestList)
    # f = os.popen(r"python Concurrent-Single.py -s={}".format(key), "r")
    # outputStr = f.buffer.read().decode("utf-8")
    # if outputStr.find()
    # time.sleep(3)
