import time

minutes = int(input("enter the number of minutes to focus:"))
secondes = minutes * 60

while seconds:
  mins,secs = divmod(seconds,60)
  timer = '{:02d}:{:02d}'.format(mins,secs)
  print(timer,end="\r")
  time.sleep(1)
  seconds -= 1

print("time's up!")
