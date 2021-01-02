"""
Measure alphabot speeds [space/second]

python <(wget -qO- https://raw.githubusercontent.com/PietroJominiITIS/alphabotbot/master/scripts/alphabot_measure.py)
"""

import RPi.GPIO as GPIO
import time
from sys import argv


class AlphaBot():

    def __init__(self, in1=12, in2=13, ena=6, in3=20, in4=21, enb=26):
        self.IN1 = in1
        self.IN2 = in2
        self.IN3 = in3
        self.IN4 = in4
        self.ENA = ena
        self.ENB = enb

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        self.forward()
        self.PWMA = GPIO.PWM(self.ENA, 500)
        self.PWMB = GPIO.PWM(self.ENB, 500)
        self.PWMA.start(40)  # 50
        self.PWMB.start(40)  # 50

    def forward(self):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)

    def backward(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)

    def left(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)

    def right(self):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)

    def setPWMA(self, value):
        self.PWMA.ChangeDutyCycle(value)

    def setPWMB(self, value):
        self.PWMB.ChangeDutyCycle(value)

    def setMotor(self, left, right):
        if((right >= 0) and (right <= 100)):
            GPIO.output(self.IN1, GPIO.HIGH)
            GPIO.output(self.IN2, GPIO.LOW)
            self.PWMA.ChangeDutyCycle(right)
        elif((right < 0) and (right >= -100)):
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.HIGH)
            self.PWMA.ChangeDutyCycle(0 - right)
        if((left >= 0) and (left <= 100)):
            GPIO.output(self.IN3, GPIO.HIGH)
            GPIO.output(self.IN4, GPIO.LOW)
            self.PWMB.ChangeDutyCycle(left)
        elif((left < 0) and (left >= -100)):
            GPIO.output(self.IN3, GPIO.LOW)
            GPIO.output(self.IN4, GPIO.HIGH)
            self.PWMB.ChangeDutyCycle(0 - left)


def measure_linear(bot, st=2):
    print('Measuring linear speed')

    start = time.time()
    bot.forward()

    while time.time() - start < st:
        pass

    bot.stop()
    space = float(input("Enter the distance traveled: "))

    return space / st


def measure_angular(bot, st=2):
    print('Measuring linear speed')

    start = time.time()
    bot.right()

    while time.time() - start < st:
        pass

    bot.stop()
    space = float(input("Enter the angle performed: "))

    return space / st


def main():
    st = float(argv[1]) if len(argv) > 1 else 2
    bot = AlphaBot()

    linear = measure_linear(bot, st=st)
    print(f'\nLinear speed: {linear} [per second]\n\n')

    angular = measure_angular(bot, st=st)
    print(f'\nAngular speed: {angular} [per second]\n\n')


if __name__ == "__main__":
    main()
