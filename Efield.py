from manim import *
from manim.utils.unit import Percent

# manim -pqh Efield.py Efield
#
# ideas for illustrating fields. Line width and opacity fall off with radius. 
#
class Efield(Scene):
    def construct(self):
        self.add(Dot(color='#0000ff').move_to([-3,0,0]))
        self.add(Dot(color='#ff0000').move_to([+3,0,0]))
        self.wait(0.1)
        for percent in range (1,24,1):
            Ecircle=Circle(radius=percent * Percent(X_AXIS))
            Ecircle.set_stroke(color='#0000ff',opacity=1-percent/20, width=16-percent/2)
            Ecircle.move_to([-3,0,0])
            self.add(Ecircle)

            Pcircle=Circle(radius=percent * Percent(X_AXIS))
            Pcircle.set_stroke(color='#ff0000',opacity=1-percent/20, width=16-percent/2)
            Pcircle.move_to([+3,0,0])
            self.add(Pcircle)
            
            self.wait(0.1)
            self.remove(Ecircle)
            self.remove(Pcircle)
