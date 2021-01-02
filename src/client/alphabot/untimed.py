"""
Alphabot "untimed" wrapper 
"""

try:
    from src.client.alphabot.alphabot import AlphaBot
    # TODO measure
    linear_speed = None
    rotation_speed = None

except ImportError:
    from src.client.alphabot.alphabot_dummy import AlphaBot
    linear_speed = 87.5
    rotation_speed = 105

import time


class AlphaBotUntimed(AlphaBot):

    def backward(self, space):
        super().backward()
        time.sleep(space / linear_speed)
        super().stop()

    def forward(self, space):
        super().forward()
        time.sleep(space / linear_speed)
        super().stop()

    def rotate(self, amount):
        if amount > 0:
            super().left()
        else:
            super().right()
        time.sleep(abs(amount) / rotation_speed)
