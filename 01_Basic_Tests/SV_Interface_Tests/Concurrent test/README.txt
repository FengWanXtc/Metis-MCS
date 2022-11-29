1. 环境要求
2台小站
教师端：1个HDMI摄像头配置教师算法 1个IPC配置学生算法，接上一台laptop（配置ppt识别算法），本地管理添加一路IPC摄像头（配置板书提取算法）
学生端：1个HDMI摄像头配置教师算法 1个IPC配置学生算法
显示器要求：分辨率1920*1080

2. 脚本执行方式
默认都是并发100次
按顺序执行脚本即可
auth接口部分
python 01.post auth.py 并发请求auth接口
python 02.authmodify.py 并发请求auth/modify接口，使用相同的body
python 03.post auth modify.py 使用包含不同的body post /auth/modify 接口
python 04.post auth modify post auth.py 使用同一body post /auth/modify 接口后再使用该body post /auth接口
mediadevice接口部分
python 05.GET mediadevice audio in.py 多次并发GET mediadevice/audio/in接口过程中不断插拔audio in设备
python 06.GET mediadevice audio out.py 多次并发GET mediadevice/audio/out接口过程中不断插拔audio out设备
python 07.GET mediadevice video in.py 多次并发GET mediadevice/video/in接口过程中不断插拔video in设备
python 08.GET mediadevice video out.py 多次并发GET mediadevice/video/in接口过程中不断插拔video out设备
python 09.GET mediadevice list.py 多次并发GET mediadevice/list接口过程中不断插拔设备
python 10.GET mediadevice audio in capability.py 多次并发GET mediadevice/audio/in/capability接口过程中不断插拔audio in设备
python 11.GET mediadevice audio out capability.py 多次并发GET mediadevice/audio/out/capability接口过程中不断插拔audio out设备
python 12.GET mediadevice video in capability.py 多次并发GET mediadevice/video/in/capability接口过程中不断插拔video in设备
python 13.GET mediadevice video out capability.py 多次并发GET mediadevice/vidoe/out/capability接口过程中不断插拔video out设备
python 14.GET mediadevice video out background.py 多次并发GET mediadevice/video/out/background接口
python 15.GET mediadevice audio in configuration.py 多次并发GET mediadevice/audio/in/configuration接口
python 16.GET mediadevice audio out configuration.py 多次并发GET mediadevice/audio/out/configuration接口
python 17.POST mediadevice audio in configuration.py 同一body多次并发POST mediadevice/audio/in/configuration接口
python 18.POST mediadevice audio in configuration Mute.py 设置body Mute参数分别为true或false，多次并发POST mediadevice/audio/in/configuration接口
python 19.POST mediadevice audio in configuration.py 设置body Volume参数分别为不同的值，多次并发POST mediadevice/audio/in/configuration接口
python 20.POST mediadevice audio in configuration.py 设置body LocalAmplification参数分别为true或false，多次并发POST mediadevice/audio/in/configuration接口
python 21.POST mediadevice audio in configuration.py 设置body 音频子列表参数分别为不同的值，多次并发POST mediadevice/audio/in/configuration接口
python 22.POST mediadevice audio out configuration.py 同一body多次并发POST mediadevice/audio/out/configuration接口
python 23.POST mediadevice audio out configuration.py 设置body Mute参数分别为true或false，多次并发POST mediadevice/audio/out/configuration接口
python 24.POST mediadevice audio out configuration.py 设置body Value参数分别为不同的值，多次并发POST mediadevice/audio/out/configuration接口
python 25.POST mediadevice audio out configuration.py 设置body 音频子列表参数分别为不同的值，多次并发POST mediadevice/audio/out/configuration接口
python 26.POST mediadevice video out background.py 同一body多次并发POST mediadevice/video/out/background接口
python 27.POST mediadevice video out background.py 设置body Background参数分别为不同的值，多次并发POST mediadevice/video/out/background接口
mediatask接口部分
这部分运行完之后可以用delete all tasks删除任务,执行多个脚本间可以不删任务
python 28.POST mediatask create_update.py 多次并发POST mediatask/create_update只包含回显的task
python 29.POST mediatask create_update.py 多次并发POST mediatask/create_update包含回显和录制的task
python 30.POST mediatask create_update.py 多次并发POST mediatask/create_update包含回显、录制和互动的task 使用WP接口推流
python 31.POST mediatask remove.py 多次并发POST mediatask/remove接口
python 32.POST mediatask suspend.py 多次并发POST mediatask/suspend接口
python 33.POST mediatask resume.py 多次并发POST mediatask/resume接口
python 34.POST mediatask inspection.py 多次并发POST mediatask/inspection接口
python 35.POST mediatask keyframe.py 多次并发POST mediatask/keyframe接口 测试完后请删除任务
python 36.POST mediatask snapshot.py 多次并发POST mediatask/snapshot接口  请先关闭两个小站的防火墙
python 37.POST mediatask merge.py 多次并发POST mediatask/merge接口
python 38.DELETE  mediatask{MCS_Name}.py 多次并发DELETE  mediatask/{MCS_Name}接口
python 39.GET mediatask tasks.py 多次并发GET mediatask/tasks接口
python 40.GET mediatask{MCS_Name}{Spec_Name}.py 多次并发GET mediatask/{MCS_Name}/{Spec_Name}接口
多接口混合并发
python 41.POST mediatask create_update RenderSpecs.py.py 下发POST mediatask/create_update启动回显后并发下发回显宫格变化RenderSpecs（包含位置变化和分辨率的变化）
python 42.POST mediatask create_update  mediadevice audio in configuration.py 下发POST mediatask/create_update启动回显后并发下发回显宫格变化RenderSpecs和音量输入设置POST mediadevice/audio/in/configuration
python 43.POST mediatask create_update  mediadevice audio out configuration.py 3.下发POST mediatask/create_update启动回显后并发下发回显宫格变化RenderSpecs和音量输出设置POST mediadevice/audio/out/configuration
python 44.POST mediatask create_update  mediatask remove.py 下发POST mediatask/create_update启动回显后并发下发回显宫格变化RenderSpecs和录制的启动结束POST mediatask/create_update和POST mediatask/remove
python 45.POST mediatask create_update  mediatask suspend resume.py 下发POST mediatask/create_update启动回显后并发下发回显宫格变化RenderSpecs和录制的暂停和恢复POST mediatask/suspend和POST mediatask/resume
python 46.POST mediatask create_update  mediatask snapshot.py 下发POST mediatask/create_update启动回显后并发下发回显宫格变化RenderSpecs和截图POST mediatask/snapshot
python 47.POST mediatask create_update  mediatask keyframe.py 下发POST mediatask/create_update启动回显后并发下发回显宫格变化RenderSpecs和关键帧生成POST mediatask/keyframe
python 48.POST mediatask create_update  mediatask inspection.py 下发POST mediatask/create_update启动回显后并发下发回显宫格变化RenderSpecs和任务查询POST mediatask/inspection
python 49.POST mediatask create_update  mediatask {MCS_Name} {Spec_Name}.py 下发POST mediatask/create_update启动回显后并发下发回显宫格变化RenderSpecs和具体spec查询GET mediatask/{MCS_Name}/{Spec_Name}
python 50.POST mediatask create_update  mediatask Rtcstreamspec.py 下发POST mediatask/create_update启动回显后并发下发回显宫格变化RenderSpecs和加入退出互动（回显、互动使用不同的MCS下发更新）
python 51.POST mediatask RtcStreamSpec  mediatask audio in configuration.py 下发POST mediatask/create_update启动回显后并发下发加入退出互动和音量输入设置POST mediadevice/audio/in/configuration
python 52.POST mediatask RtcStreamSpec  mediatask audio out configuration.py 下发POST mediatask/create_update启动回显后并发下发加入退出互动和音量输出设置POST mediadevice/audio/out/configuration
python 53.POST mediatask RtcStreamSpec  mediatask create_update remove.py 下发POST mediatask/create_update启动回显后并发下发加入退出互动和录制的启动结束POST mediatask/create_update和POST mediatask/remove
python 54.POST mediatask RtcStreamSpec  mediatask suspend resume.py 下发POST mediatask/create_update启动回显后并发下发加入退出互动和录制的暂停和恢复POST mediatask/suspend和POST mediatask/resume
python 55.POST mediatask RtcStreamSpec  mediatask snapshot.py 下发POST mediatask/create_update启动回显后并发下发加入退出互动和截图POST mediatask/snapshot
python 56.POST mediatask RtcStreamSpec  mediatask keyframe.py 下发POST mediatask/create_update启动回显后并发下发加入退出互动和关键帧生成POST mediatask/keyframe
python 57.POST mediatask RtcStreamSpec  mediatask inspection.py 下发POST mediatask/create_update启动回显后并发下发加入退出互动和任务查询POST mediatask/inspection
python 58.POST mediatask RtcStreamSpec  mediatask {MCS_Name} {Spec_Name}.py 下发POST mediatask/create_update启动回显后并发下发加入退出互动和具体spec查询GET mediatask/{MCS_Name}/{Spec_Name}
python 59.POST mediatask RtcStreamSpec  mediatask audio in configuration.py 下发POST mediatask/create_update启动回显后并发下启动停止录制和音量输入设置POST mediadevice/audio/in/configuration
python 60.POST mediatask RtcStreamSpec  mediatask audio out configuration.py 下发POST mediatask/create_update启动回显后并发下启动停止录制和音量输出设置POST mediadevice/audio/out/configuration
python 61.POST mediatask RtcStreamSpec  mediatask snapshot.py 下发POST mediatask/create_update启动回显后并发下启动停止录制和截图POST mediatask/snapshot
python 62.POST mediatask RtcStreamSpec  mediatask keyframe.py 下发POST mediatask/create_update启动回显后并发下启动停止录制和关键帧生成POST mediatask/keyframe
python 63.POST mediatask RtcStreamSpec  mediatask inspection.py 下发POST mediatask/create_update启动回显后并发下启动停止录制和任务查询POST mediatask/inspection
python 64.POST mediatask RtcStreamSpec  mediatask {MCS_Name} {Spec_Name}.py 下发POST mediatask/create_update启动回显后并发下启动停止录制和具体spec查询GET mediatask/{MCS_Name}/{Spec_Name}