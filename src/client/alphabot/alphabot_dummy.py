"""
Dummy AlphaBot for testing purposes
basically, a big mess 
TODO make rotation somehow realistic
"""

import turtle
import time
from threading import Thread
from enum import Enum


class AlphaBot():

    def __init__(self, _d_scale=1, rdelay=.01, speed=100, direction=0, width=750, height=750):
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

        self._d_pos = (0, 0)
        self._d_rot = 0

        self._d_scale = _d_scale

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
            ctr = time.time()

            self.dir += self.rotation * self.speed * elapsed
            space = self.speed * elapsed
            if self.going_forward:
                space *= 1
            elif self.going_backward:
                space *= -1
            else:
                space *= 0

            bot.setheading(self.dir)
            bot.forward(space / self._d_scale)

            self._d_rot = bot.heading()
            self._d_pos = bot.pos()
