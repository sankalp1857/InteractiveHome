from classification import classify
from feedback import feedback
from action import  action
from speech import recognise


def main():
    found_classes = []
    while True:
        text = recognise()
        temp = classify(text)

        if len(found_classes) < 3:
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

        if room == rooms[0]:
            if appliance == appliances[0]:
                if state == states[0]:
                    action(0, 1)
                elif state == states[1]:
                    action(0, 0)
                else:
                    say = "STATE"
                    mode = "ask"
                    feedback(mode, say)
            elif appliance == appliances[1]:
                if state == states[0]:
                    action(1, 1)
                elif state == states[1]:
                    action(1, 0)
                else:
                    say = "STATE"
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
                    say = "STATE"
                    mode = "ask"
                    feedback(mode, say)
        elif room == rooms[1]:
            if appliance == appliances[0]:
                if state == states[0]:
                    action(3, 1)
                elif state == states[1]:
                    action(3, 0)
                else:
                    say = "STATE"
                    mode = "ask"
                    feedback(mode, say)
            elif appliance == appliances[1]:
                if state == states[0]:
                    action(4, 1)
                elif state == states[1]:
                    action(4, 0)
                else:
                    say = "STATE"
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
                    say = "STATE"
                    mode = "ask"
                    feedback(mode, say)
            else:
                say = "APPLIANCE"
                mode = "ask"
                feedback(mode, say)
        else:
            say = "ROOM"
            mode = "ask"
            feedback(mode, say)




if __name__== "__main__":
  main()