"""
Alphabot "untimed" wrapper 
"""

# from src.client.alphabot.alphabot import AlphaBot
from src.client.alphabot.alphabot_dummy import AlphaBot
import time

"""
speed is relative to the alphabot,
and should be measured

technically the dummy one can be calculated,
but soomehow i could't manage to do it correctly
"""
linear_speed = 87.44  # should be 100, turtle/process lag?
# yep, that should be 100 al well and the same as the linear one lol
rotation_speed = 95.53
# measured with 100 (linear) and 90 (rotation)
# and they seems not to be parametrics (!?)
# dunno, too late, tomorrow's problem


class AlphaBotUntimed(AlphaBot):

    def forward(self, space):
        super().forward()
        time.sleep(space / linear_speed)
        super().stop()

    def rotate(self, amount):
        if amount > 0:
            super().left()
        else:
            super().right()
        time.sleep(amount / rotation_speed)
