多线程并发下发MCS 场景测试
环境要求：
2台小站都做相同摄像头配置
2个HDMI摄像头，HDMI-0教师算法，HDMI-1学生算法
运行方式
python concurrent_test.py -ip=10.12.xxxxx
参数化构建，启动1宫教师回显，2宫学生摄像头回显，3宫远端拉流，4宫远端拉流
启动3个线程并行下发同样的MCS，通过打印的信息查看是否存在异常

注：由于Python多线程实际是假的多线程实际等价与单线程