1. 环境要求
教师端：2个HDMI摄像头
显示器要求：分辨率1920*1080

2. 脚本执行方式可选

方式1：python Act_Story.py
            根据终端提示按回车键执行下一个动作

            场景内容：
            ①创建静态录制窗口（左上角）
            ②创建动态录制窗口（右上角）
            ③开始动态窗口录制动作
            ④删除静态窗口（左上角）
            ⑤再次创建静态窗口（左上角）
            ⑥停止动态窗口录制动作
            ⑦删除所有窗口


方式2：根据喜好执行单功能脚本
            python 脚本名.py
        单功能脚本说明：
        ①static_record.py （参数化构建 -ip 指定小站IP，默认为当前小站）
        ②dynamic_preview.py  （参数化构建 -ip 指定小站IP，默认为当前小站）
        ③delete_all_tasks.py （参数构建，删除所有窗口）
        ④delete_task_by_name.py
           参数化构建 -n 可选值  S3E3_Dynamic  ，S3E3_Static  删除对应的宫格窗口
        ⑤record_start.py（非参数构建，开启动态窗口录制）
        ⑥record_stop.py（非参数构建，停止动态窗口录制）
        

