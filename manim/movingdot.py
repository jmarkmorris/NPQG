from manim import *

class MovingDot(Scene):
    def construct(self):
        circle = Circle(stroke_width=0, radius=3)
        dot = Dot(color=DARK_BLUE)
        trail = TracedPath(dot.get_center, stroke_color=BLUE, stroke_width=2, dissipating_time=1)
        self.add(circle, dot, trail)
        self.play(MoveAlongPath(dot, circle), run_time=5, rate_func=linear)



