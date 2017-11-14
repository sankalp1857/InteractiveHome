import os
def alarm():
    hours=12
    min=3
    time=str(hours)+":"+str(min)
    os.system("./alarmclock.sh -t"+time)
alarm()

