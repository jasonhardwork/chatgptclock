import time

def focus_timer(duration):
    print("专注时间开始！")
    time.sleep(duration * 60)  # 将分钟转换为秒并等待指定的专注时间
    print("专注时间结束！")

# 设置专注时间（以分钟为单位）
focus_duration = 100000000

# 启动专注时钟
focus_timer(focus_duration)
