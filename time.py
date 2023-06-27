import time

def focus_timer(duration):
    print("专注时钟已启动，倒计时 {} 分钟".format(duration))
    duration_sec = duration * 60
    time.sleep(duration_sec)
    print("专注时钟结束，恭喜你完成任务！")

if __name__ == "__main__":
    duration = int(input("请输入专注时长（分钟）："))
    focus_timer(duration)
