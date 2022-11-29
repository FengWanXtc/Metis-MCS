10XX开头均为mediadevice 基础的API测试脚本
运行方式均为 python 10XX .py

1001 - 1011（非参数化构建） ：
运行后会以表格形式形象化返回的内容

1012（交互式脚本，非参数化）:
该脚本会改变麦克风的音量，可以先去DemoAPP 开一个互动房间，然后运行该脚本，根据输入的音量大小调整音量，输入q退出

1013（非参数化）：
该脚本会播放音乐并且不停的进行post修改扬声器音量，音量由大变小再由小变大

1014：（参数化构建）  -i=False ，缺省值为False ，会出现一个画面， 如果为True 则是 返回原本桌面
运行方式： python  1014XXX.py -i=False

1100：设定本地管理摄像头的脚本，有需要可以测试
    python 1100_XXX.py -d=0 -a=AliasNameXXXXXXX -ai=teacher
        -d指定摄像头，可选0,1,2,3..... 分别对应CAM_1 CAM_2 CAM_3 ,USB_CAM_1.....
        -a指定摄像头别名
        -ai 指定摄像头算法，可选值 teacher,student,ppt,blackboard
