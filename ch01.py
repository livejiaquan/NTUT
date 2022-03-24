import time
currentTime = time.time()
totalSeconds = int(currentTime)
currentSecond = totalSeconds%60
totalMinutes = totalSeconds//60
currentMinute = totalMinutes%60
totalHors = totalMinutes//60
currentHour = totalHors%24
print("Current time is",currentHour,\
      ":",currentMinute,":",currentSecond,"GMT")

