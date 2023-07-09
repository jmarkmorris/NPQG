import morpholib as morpho
morpho.importAll()
from morpholib.tools.basics import *
import math, cmath

class Tracker(morpho.Skit):
    def makeFrame(self):
        # The t value is stored as a tweenable attribute
        # of the tracker itself. Let's extract it just
        # to simplify the later syntax.
        t = self.t

        # Turn t into a string formatted so
        # it's rounded to the third decimal place
        # and always displays three digits to the right
        # of the decimal place, appending zeros if necessary.
        number = morpho.text.formatNumber(t, decimal=3, rightDigits=3)

        # The label's text is the stringified version of
        # the "number" object, which does the job of
        # rounding and appending trailing zeros for us.
        label = morpho.text.Text(number)
        return label

# Construct an instance of our new Tracker Skit.
# By default, t is initialized to t = 0.
mytracker = Tracker()

# Turn it into an actor, and have its t value progress
# to the number 1 over the course of 2 seconds (60 frames)
mytracker = morpho.Actor(mytracker)
mytracker.newendkey(60)
mytracker.last().t = 1

movie = morpho.Animation(mytracker)
movie.play()