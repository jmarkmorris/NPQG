
import morpholib as morpho
morpho.importAll()
from morpholib.tools.basics import *
import math, cmath

#morpho.sample.play()

electrino = morpho.grid.Point()
electrino.size = 25
electrino.pos = complex(4,3)
electrino.fill = [0,0,1]
electrino.color = [1,1,1]
electrino.strokeWeight = 2
electrino = morpho.Actor(electrino)
electrino.newkey(60)
electrino.time(60).pos = complex(1,1)



positrino = morpho.grid.Point()
positrino.size = 25
positrino.pos = complex(-4,-3)
positrino.fill = [1,0,0]
positrino.color = [1,1,1]
positrino.strokeWeight = 2
positrino = morpho.Actor(positrino)
positrino.newkey(120)
positrino.time(120).pos= complex(-1,-1)

layer = morpho.Layer([electrino,positrino])



movie = morpho.Animation(layer)
movie.frameRate = 60
#movie.fullscreen = True
movie.windowShape= (1000,1000)
#movie.background = [0.5, 0, 0.5]
#movie.export("./movie.mp4")

movie.play()

