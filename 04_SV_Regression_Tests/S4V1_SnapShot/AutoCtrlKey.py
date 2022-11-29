import pyautogui
import time

time.sleep(5)
print("Start Auto Control Keyboard")
begin_time = time.time()    # 开始时间
anchor_time = time.time()   # 锚点时间
while True:
    # 加等待时间是为了减少循环的次数0
    time.sleep(500)
    end_time = time.time()
    # 每隔10分钟切换一次PPT
    if end_time - anchor_time > 600:
        print(":: 按了方向下键盘")
        pyautogui.press("down")
        time.sleep(60)
        print(":: 按了方向上键盘")
        pyautogui.press("up")
        # 每隔多久 刷新一次锚点和当前时间
        anchor_time = time.time()
        end_time = time.time()

    # 超过 7天 就停止脚本
    if end_time - begin_time > 604800:
        print("Auto Control Keyboard Ends")
        break


