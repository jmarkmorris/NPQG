
## manim PointMovingOnShapes.py PointMovingOnShapes -pqh --disable_caching -p

from manim import *

class PointMovingOnShapes(Scene):
    def construct(self):
        circle = Circle(radius=1, color=WHITE)
        dot = Dot(color=PURE_BLUE).shift(RIGHT)

        self.play(GrowFromCenter(circle))
        self.add(dot)
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.wait()