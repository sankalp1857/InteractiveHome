import os
import datetime

now = datetime.datetime.now()


def alarm(time):
    os.system("alarmclock.sh -t " + time + "&")


def reminder(day, month, year, msg):
    cur_day = now.day
    cur_month = now.month
    cur_year = now.year
    cur_date = datetime.date(cur_year, cur_month, cur_day)
    rem_date = datetime.date(year, month, day)
    delta = rem_date - cur_date
    os.system("alarmclock.sh -d "+str(delta.days)+" -m " + msg + " &")
    os.system("printf \'%s " + msg + "\n\' \"$!\" >> /data/reminder_pid.txt")


def todo(message):
    with open('todo.txt', 'a')as f:
        f.write(message + "\n")


def cancel_reminder(msg):
    with open('reminder_pid.txt') as f:
        lines = f.readlines()
    f.close()
    f = open('/data/reminder_pid.txt', 'w')
    for s in lines:
        if msg not in s:
            f.write(s)
    f.close()
