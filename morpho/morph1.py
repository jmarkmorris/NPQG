import morpholib as morpho
morpho.importAll()
from morpholib.tools.basics import *


# Create a blue dot
dot = morpho.grid.Point()
dot.color = [0,0,1] # blue color
dot.size = 10

# Create a circle path for the dot to follow
circle = morpho.shapes.Ellipse(0+0j,2,2)
circle.color = [0,0,1] # blue color

# Create a light blue trail for the last pi radians
trail = morpho.grid.arc(radius=100, start=pi, end=2*pi)
trail.color = [0.5, 0.5, 1] # light blue color

# Create a figure that moves the dot along the circle at constant velocity
dotMover = morpho.Actor(dot)
dotMover.newendkey(120) # 120 frames (2 seconds at 60fps)
dotMover.newkey(0, pos=circle.pos(0))
dotMover.newkey(120, pos=circle.pos(2*pi))

# Create a figure that moves the trail along the circle at constant velocity
trailMover = morpho.Actor(trail)
trailMover.newendkey(120) # 120 frames (2 seconds at 60fps)
trailMover.newkey(0, start=pi, end=2*pi)
trailMover.newkey(120, start=3*pi, end=4*pi)

# Create a Morpho animation with the dot and trail figures
animation = morpho.Animation([dotMover, trailMover])
animation.play()
