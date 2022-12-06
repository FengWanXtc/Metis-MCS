1. 环境要求
至少2台小站
近端：1个摄像头配置教师算法 1个配置学生算法，接上一台laptop（配置ppt识别算法），本地管理添加一路IPC摄像头（配置板书提取算法）
远端：1个摄像头配置教师算法 1个配置学生算法，接上一台laptop（配置ppt识别算法），本地管理添加一路IPC摄像头（配置板书提取算法）
显示器要求：分辨率1920*1080

################################
注：若脚本在小站上直接运行，下面脚本不跟
   -ip 参数默认为当前小站IP地址
################################


2. 脚本执行方式
Case 01 【Metis station Z510_BS&ESWIN_Agora_Media_Dynamic_Change_01】
Steps: 1.python Agora_Basic.py -ip=近端小站IP地址，启基础任务
       2.python Agora_Far.py -ip=远端小站IP地址，启基础任务,查看两台小站音视频是否正常
       3.python Dynamic_Change_01.py  近端动态替换PC IN 音频流，远端不再接收到近端MIC 音频输入
       4.python delete_all_tasks.py -ip=近端（远端）小站IP，停止两端的任务，两端正常结束

Case 02 【Metis station Z510_BS&ESWIN_Agora_Media_Dynamic_Change_02】
Steps: 1.python Agora_Basic.py -ip=近端小站IP地址，启基础任务
       2.python Agora_Far.py -ip=远端小站IP地址，启基础任务,查看两台小站音视频是否正常
       3.python Dynamic_Change_02.py  近端动态替换视频流，远端收到的视频画面发生改变，不影响两端的音频，依然为MIC输入
       4.python delete_all_tasks.py -ip=近端（远端）小站IP，停止两端的任务，两端正常结束

Case 03 【Metis station Z510_BS&ESWIN_Agora_Media_Dynamic_Change_03】
Steps: 1.python Agora_Basic.py -ip=近端小站IP地址，启基础任务
       2.python Agora_Far.py -ip=远端小站IP地址，启基础任务,查看两台小站音视频是否正常
       3.python Dynamic_Change_03.py  -ip=近端小站IP 远端拉取的近端小站视频源和音频源都发生了变更
       4.重复第3步，-ip改为远端小站IP   近端拉取的远端小站视频源和音频源都发生了变更
       5.此时不删除两端任务，进行下一个Case

Case 04 【Metis station Z510_BS&ESWIN_Agora_Media_Dynamic_Change_04】
Steps: 1.python Dynamic_Change_04.py  -ip=近端小站IP 远端拉取的近端小站回显宫格位置发生改变，拉取的视频流畅正常
       2.重复第2步，-ip改为远端小站IP   近端拉取的远端小站回显宫格位置发生改变，拉取的视频流畅正常
       3.此时不删除两端任务，进行下一个Case

Case 05 【Metis station Z510_BS&ESWIN_Agora_Media_Dynamic_Change_05】
Steps: 1.python Dynamic_Change_05.py  -ip=近端小站IP 近端小站回显先移除，5秒后出现，拉取的视频流畅正常
       2.重复第2步，-ip改为远端小站IP   远端小站回显先移除，5秒后出现，拉取的视频流畅正常
       3.python delete_all_tasks.py -ip=近端（远端）小站IP，停止两端的任务，两端正常结束

Case 06 【Metis station Z510_BS&ESWIN_Agora_Media_Dynamic_Change_06】
Steps: 1.python Agora_Basic.py -ip=近端小站IP地址，启基础任务
       2.python Agora_Far.py -ip=远端小站IP地址，启基础任务,查看两台小站音视频是否正常
       3.python Record.py -ip=近端小站IP地址 -vs=Student -as=Mic  选择近端录制学生画面+Mic音频
       4.python Record.py -ip=远端小站IP地址 -vs=Computer -as=PC  选择远端录制PPT画面+PC音频
       5.python Dynamic_Change_02.py  -ip=近端小站IP地址
         近端动态替换视频流，远端收到的视频画面发生改变，不影响两端的音频，依然为MIC输入
         也不影响录制任务继续进行
       6.python delete_all_tasks.py -ip=近端（远端）小站IP，停止两端的任务，两端正常结束,检查两端录制文件是否符合要求


Case 07 【Metis station Z510_BS&ESWIN_Agora_Media_Dynamic_Change_07】
Steps: 1.python Agora_Basic.py -ip=近端小站IP地址，启基础任务
       2.python Agora_Far.py -ip=远端小站IP地址，启基础任务,查看两台小站音视频是否正常
       3.python Record.py -ip=近端小站IP地址 -vs=Student -as=Mic  选择近端录制学生画面+Mic音频
       4.python Record.py -ip=远端小站IP地址 -vs=Computer -as=PC  选择远端录制PPT画面+PC音频
       5.python Dynamic_Change_02.py  -ip=近端小站IP地址  -vs=NULL   不推送近端视频源，查看远端拉取的是否为黑屏
       6.python Dynamic_Change_02.py  -ip=近端小站IP地址  -vs=其他字符串，如st，1a  等等 ，MA应当返回错误码
       7.python delete_all_tasks.py -ip=近端（远端）小站IP，停止两端的任务，两端正常结束,检查两端录制文件是否符合要求

Case 08 【Metis station Z510_BS&ESWIN_Agora_Media_Dynamic_Change_08】
Steps: 1.python Agora_Basic.py -ip=近端小站IP地址，启基础任务
       2.python Agora_Far.py -ip=远端小站IP地址，启基础任务,查看两台小站音视频是否正常
       3.python Record.py -ip=近端小站IP地址 -vs=Student -as=Mic  选择近端录制学生画面+Mic音频
       4.python Record.py -ip=远端小站IP地址 -vs=Computer -as=PC  选择远端录制PPT画面+PC音频
       5.python Dynamic_Change_01.py  -ip=近端小站IP地址  -vs=NULL   不推送近端音频源，对着MIC说话，远端不接收声音
       6.python Dynamic_Change_01.py  -ip=近端小站IP地址  -vs=其他字符串，如st，1a  等等 ，MA应当返回错误码
       7.此时不删除两端任务，进行下一个Case

Case 09 【Metis station Z510_BS&ESWIN_Agora_Media_Dynamic_Change_09】
Steps: 1.python Dynamic_Change_04.py  -ip=近端小站IP 远端拉取的近端小站回显宫格位置发生改变，拉取的视频流畅正常
       2.重复第2步，-ip改为远端小站IP   近端拉取的远端小站回显宫格位置发生改变，拉取的视频流畅正常
       3.此时不删除两端任务，进行下一个Case

Case 10 【Metis station Z510_BS&ESWIN_Agora_Media_Dynamic_Change_10】
Steps: 1.python Dynamic_Change_05.py  -ip=近端小站IP 近端小站回显先移除，5秒后出现，拉取的视频流畅正常
       2.重复第2步，-ip改为远端小站IP   远端小站回显先移除，5秒后出现，拉取的视频流畅正常
       3.python delete_all_tasks.py -ip=近端（远端）小站IP，停止两端的任务，两端正常结束，查看录制的视频，视频正常流畅

Case 11 【Metis station Z510_BS&ESWIN_Agora_Media_Dynamic_Change_11】
Steps: 1.python Dynamic_Change_11.py  根据提示依次输入两端小站IP地址
       2.依照提示内容按回车执行下一个步骤
       3.场景内容为:（1）创建近端和远端任务
                  （2）动态修改推流视频编码格式，RtcStreamSpec 由H264改为H265 导播路推流
                  （3）动态修改推流音频编码，由pcm Mic 改为opus Mic
                  （4）删除两端任务

Case 12 【Metis station Z510_BS&ESWIN_Agora_Media_Dynamic_Change_12】
Steps: 1.python Dynamic_Change_11.py  根据提示依次输入两端小站IP地址
       2.依照提示内容按回车执行下一个步骤
       3.场景内容为:（1）创建近端和远端任务
                  （2）动态修改推流视频编码格式，AudioCodecSpec 由H264改为H265 ，不改变RtcStreamSpec
                  （3）动态修改推流音频编码，由pcm Mic 改为opus Mic
                  （4）删除两端任务