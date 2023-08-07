
# A helpful way to draw a grid when composing the animation
INDIGO = "#4B0082"
    grid = NumberPlane(
        x_range=[-7, 7],
        y_range=[-4, 4],
        axis_config={
            "stroke_color": WHITE,
            "stroke_width": 1,
            "include_ticks": False,
            "include_tip": False,
        },
        background_line_style={
            "stroke_color": INDIGO,
            "stroke_width": 1,
        }
    )
    self.add(grid)

# A easy to read way to define a dictionary.
# A way to pass a dictionary to a function rather than a long args list.
from manim import *

class jj(Scene):
    def construct(self):
        
        kwargs = {
            'side_length': 5, 
            'stroke_color': GREEN, 
            'fill_color': BLUE, 
            'fill_opacity': 0.75
        }
        sq = Square(**kwargs)
        # sq = Square(side_length=5, stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.75)

        # self.play(Create(sq), run_time=3)
        self.play(Create(sq), run_time=3, subcaption="this is my caption", subcaption_duration=3)

        self.wait() 