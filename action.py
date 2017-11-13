import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

BED_LIGHT = 3
BED_FAN = 18
BED_AC = 11
LIVING_LIGHT = 16
LIVING_FAN = 5

GPIO.setup(BED_LIGHT, GPIO.OUT)
GPIO.setup(BED_FAN, GPIO.OUT)
GPIO.setup(BED_AC, GPIO.OUT)
GPIO.setup(LIVING_LIGHT, GPIO.OUT)
GPIO.setup(LIVING_FAN, GPIO.OUT)

PWM_BED_LIGHT = GPIO.PWM(BED_LIGHT, 50)
PWM_BED_FAN = GPIO.PWM(BED_FAN, 50)
PWM_BED_AC = GPIO.PWM(BED_AC, 50)
PWM_LIVING_LIGHT = GPIO.PWM(LIVING_LIGHT, 50)
PWM_LIVING_FAN = GPIO.PWM(LIVING_FAN, 50)

PWM_BED_LIGHT.start(0)
PWM_BED_FAN.start(0)
PWM_BED_AC.start(0)
PWM_LIVING_LIGHT.start(0)
PWM_LIVING_FAN.start(0)


def action(pin_no, state):
    if (pin_no == BED_LIGHT):
        PWM_BED_LIGHT.ChangeDutyCycle(state)
    elif (pin_no == BED_FAN):
        PWM_BED_FAN.ChangeDutyCycle(state)
    elif (pin_no == BED_AC):
        state = (state * 100)/28
        PWM_BED_AC.ChangeDutyCycle(state)
    elif (pin_no == LIVING_LIGHT):
        PWM_LIVING_LIGHT.ChangeDutyCycle(state)
    elif (pin_no == LIVING_FAN):
        PWM_LIVING_FAN.ChangeDutyCycle(state)
