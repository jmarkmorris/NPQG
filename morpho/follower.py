import morpholib as morpho
morpho.importAll()
from morpholib.tools.basics import *
import math, cmath


# Create a curved path that begins at x = -4 and ends at x = +4
path = morpho.graph.realgraph(lambda x: 0.2*(x**3 - 12*x), -4, 4)

class Follower(morpho.Skit):
    def makeFrame(self):
        t = self.t

        # Create a generic Point figure
        point = morpho.grid.Point()
        # Set the position of the point to be the path's
        # position at parameter t.
        point.pos = path.positionAt(t)

        return point



# Set the follower to begin at the END of the path,
# just to change things up a little.
myfollower = Follower(t=0)

# Turn it into an actor, and set its t value to be 0
# after 2 seconds (60 frames) have passed.
myfollower = morpho.Actor(myfollower)
myfollower.newendkey(60)
myfollower.last().t = 1

# Include both the original path and the follower, so
# we can clearly see that the follower is following the
# intended path.
movie = morpho.Animation(morpho.Layer([path, myfollower]))
movie.play()