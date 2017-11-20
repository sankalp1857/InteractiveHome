import socket
import sys

from action import action
from alarm import reminder, alarm, todo
from classification import classify
from compound import *
from feedback import feedback


def main():
    print("===================================System active===================================")

    found_classes = []

    rooms = ["bedroom", "living_room"]
    states = ["on", "off", "value"]
    appliances = ["light", "fan", "ac"]

    ACTION_KEY = "InteractiveHome"
    HOST = '192.168.43.100'
    PORT = 8888

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket to Host and Port
    try:
        sock.bind((HOST, PORT))
    except socket.error as err:
        print 'Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1]
        sys.exit()

    print 'Socket Bind Success!'

    sock.listen(10)
    print 'Socket is now listening'

    while True:
        print("Listening...")

        conn, addr = sock.accept()
        print 'Connect with ' + addr[0] + ':' + str(addr[1])

        buf = conn.recv(64)
        value = buf.encode("utf-8")

        if ACTION_KEY in value:
            pin = int(value[:2])
            state = int(value[2:5])
            action(pin, state)

        else:
            temp = classify(value)

            if len(
                    found_classes) < 3 and 'reminder' not in found_classes and 'alarm' not in found_classes and 'todo' not in found_classes:
                found_classes += temp
            else:
                found_classes = temp

            r = [x for x in found_classes if x in rooms]
            a = [x for x in found_classes if x in appliances]
            s = [x for x in found_classes if x in states]
            room = r[0] if r else None
            appliance = a[0] if a else None
            state = s[0] if s else None
            is_reminder = True if 'reminder' in found_classes else False
            is_alarm = True if 'alarm' in found_classes else False
            is_todo = True if 'todo' in found_classes else False

            if not is_reminder and not is_alarm and not is_todo:
                if room == rooms[0]:
                    if appliance == appliances[0]:
                        if state == states[0]:
                            action(3, 100)

                        elif state == states[1]:
                            action(3, 0)

                        else:
                            say = "Forgot to tell me on or off."
                            mode = "ask"
                            feedback(mode, say)

                    elif appliance == appliances[1]:
                        if state == states[0]:
                            action(18, 100)

                        elif state == states[1]:
                            action(18, 0)

                        else:
                            say = "turn it off or on"
                            mode = "ask"
                            feedback(mode, say)

                    elif appliance == appliances[2]:
                        if state == states[0]:
                            action(11, 100)

                        elif state == states[1]:
                            action(11, 0)

                        elif state == state[2]:
                            temp = getTemperature(value)
                            action(11, temp)

                        else:
                            say = "Sorry didn't hear you."
                            mode = "ask"
                            feedback(mode, say)

                    else:
                        say = "Which appliance?"
                        mode = "ask"
                        feedback(mode, say)

                elif room == rooms[1]:
                    if appliance == appliances[0]:
                        if state == states[0]:
                            action(16, 100)

                        elif state == states[1]:
                            action(16, 0)

                        else:
                            say = "turn it off or on"
                            mode = "ask"
                            feedback(mode, say)

                    elif appliance == appliances[1]:
                        if state == states[0]:
                            action(4, 1)

                        elif state == states[1]:
                            action(4, 0)

                        else:
                            say = "On or off?"
                            mode = "ask"
                            feedback(mode, say)

                    else:
                        say = "Which appliance"
                        mode = "ask"
                        feedback(mode, say)

                else:
                    say = "What room did you say?"
                    mode = "ask"
                    feedback(mode, say)

            elif is_reminder:
                year, month, day, category = getDate(value)
                msg = getMessage(value, category)
                reminder(day, month, year, msg)
                say = "Reminder set for date " + day + "th " + month + " " + year + ". Event: " + msg + "."
                mode = "repeat"
                feedback(mode, say)

            elif is_alarm:
                time = getAlarmTime(value)
                alarm(time)
                say = "Alarm set for " + time + "hours."
                mode = "repeat"
                feedback(mode, say)

            elif is_todo:
                todo(value)
                say = "Todo set: " + value + "."
                mode = "repeat"
                feedback(mode, say)

            else:
                say = "Oops didn't catch that!"
                mode = "Error"
                feedback(mode, say)


if __name__ == "__main__":
    main()
