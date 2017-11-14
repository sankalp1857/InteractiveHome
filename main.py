import speech_recognition as sr

from action import action
from alarm import reminder, alarm, todo
from classification import classify
from compound import *
from feedback import feedback


def main():
    print("===================================System active===================================")

    found_classes = []

    while True:
        print("Listening...")
        r = sr.Recognizer()
        m = sr.Microphone()

        with m as source:
            r.adjust_for_ambient_noise(source)

        with m as source:
            audio = r.listen(source)

        try:
            value = r.recognize_google(audio)
            temp = classify(value)
            if len(found_classes) < 3 and 'reminder' not in found_classes and 'alarm' not in found_classes and 'todo' not in found_classes:
                found_classes += temp
            else:
                found_classes = temp

            rooms = ["bedroom", "living_room"]
            states = ["on", "off", "value"]
            appliances = ["light", "fan", "ac"]

            r = [x for x in found_classes if x in rooms]
            a = [x for x in found_classes if x in appliances]
            s = [x for x in found_classes if x in states]
            room = r[0] if r else None
            appliance = a[0] if a else None
            state = s[0] if s else None
            is_reminder = True if 'reminder' in found_classes else False
            is_alarm = True if 'alarm' in found_classes else False
            is_todo = True if 'todo' in found_classes else False

            if room or appliance or state:
                if room == rooms[0]:
                    if appliance == appliances[0]:
                        if state == states[0]:
                            action(3, 100)

                        elif state == states[1]:
                            action(0, 0)

                        else:
                            say = "Forgot to tell me on or off."
                            mode = "ask"
                            feedback(mode, say)

                    elif appliance == appliances[1]:
                        if state == states[0]:
                            action(1, 1)

                        elif state == states[1]:
                            action(1, 0)

                        else:
                            say = "turn it off or on"
                            mode = "ask"
                            feedback(mode, say)

                    elif appliance == appliances[2]:
                        if state == states[0]:
                            action(2, 1)

                        elif state == states[1]:
                            action(2, 0)

                        elif state == state[2]:
                            action(2, 0.96)

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
                            action(3, 0)

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
                            say = "Sorry didn't hear you."
                            mode = "ask"
                            feedback(mode, say)

                    elif appliance == appliances[2]:
                        if state == states[0]:
                            action(5, 1)

                        elif state == states[1]:
                            action(5, 0)

                        elif state == state[2]:
                            action(5, 0.48)

                        else:
                            say = "Did you forget to tell me on or off."
                            mode = "ask"
                            feedback(mode, say)

                    else:
                        say = "Which appliance"
                        mode = "ask"
                        feedback(mode, say)

                else:
                    say = "What's the room you say?"
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

        except sr.UnknownValueError:
            say = "Oops didn't catch that!"
            mode = "Error"
            feedback(mode, say)

        except sr.RequestError:
            say = "Internet seems to be down."
            mode = "Error"
            feedback(mode, say)


if __name__ == "__main__":
    main()
