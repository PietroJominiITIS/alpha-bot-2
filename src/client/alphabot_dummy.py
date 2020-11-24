"""
Dummy AlphaBot for testing purposes
"""

import turtle
import time
from threading import Thread
from enum import Enum


class Alphabot():

    def __init__(self, rdelay=.01, speed=100, direction=0, width=750, height=750):
        self.rdelay = rdelay
        self.speed = speed
        self.dir = direction
        self.going_forward = False
        self.rotation = 1
        self.going_backward = False

        self.width = width
        self.height = height

        self.running = True
        self.worker = Thread(target=self.dm)
        self.worker.daemon = True
        self.worker.start()

    def forward(self):
        self.going_forward = True
        self.going_backward = False
        self.rotation = 0

    def stop(self):
        self.going_forward = False
        self.going_backward = False
        self.rotation = 0

    def backward(self):
        self.going_forward = True
        self.going_backward = True
        self.rotation = 0

    def left(self):
        self.going_forward = False
        self.going_backward = False
        self.rotation = 1

    def right(self):
        self.going_forward = False
        self.going_backward = False
        self.rotation = -1

    def __del__(self):
        self.running = False

    def dm(self):
        scr = turtle.Screen()
        scr.title("Alphabot dummy")
        scr.setup(self.width, self.height)

        bot = turtle.Turtle()
        bot.speed('fastest')

        ctr = time.time()
        while self.running:
            elapsed = time.time() - ctr
            if elapsed < self.rdelay:
                continue

            actual_speed = self.speed * elapsed
            distance = actual_speed * self.going_forward * -1 if self.going_backward else 1
            self.dir += self.rotation * actual_speed

            bot.setheading(self.dir)
            bot.forward(distance)

            print(elapsed, distance, self.dir)

            ctr = time.time()
