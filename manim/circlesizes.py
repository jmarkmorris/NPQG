# manim -pqh --disable_caching circlesizes.py circlesizes -p

# from manim import *

# # import math
# # import sys
# # from ctypes import *

# # frame_rate = 60
# config.pixel_width = 2998
# config.pixel_height = 1686
# # config.frame_rate = frame_rate

# INDIGO = "#4B0082"

# colors = [PURE_BLUE, PURE_RED]

# class circlesizes(Scene):
#     def construct(self):
#         self.camera.background_color = INDIGO # looks good


#         grid = NumberPlane(
#             x_range=[-7, 7],
#             y_range=[-4, 4],
#             axis_config={
#                 "stroke_color": WHITE,
#                 "stroke_width": 1,
#                 "include_ticks": False,
#                 "include_tip": False,
#             },
#             background_line_style={
#                 "stroke_color": ELECTRIC_PURPLE,
#                 "stroke_width": 1,
#             }
#         )
#         self.add(grid)


from manim import *

ELECTRIC_PURPLE = "#8F00FF"
INDIGO = "#4B0082"

colors = [PURE_BLUE, PURE_RED]

class circlesizes(Scene):
    def construct(self):
        self.camera.background_color = INDIGO

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
                "stroke_color": ELECTRIC_PURPLE,
                "stroke_width": 1,
            }
        )
        self.add(grid)

        for x in range(-7, 7):
            for y in range(-4, 4):
                left_circle = Circle(radius=0.2, color=colors[0]).move_to([x + 0.25, y+0.75, 0])
                left_circle.set_fill(color=colors[0], opacity=1)
                right_circle = Circle(radius=0.2, color=colors[1]).move_to([x + 0.75, y+0.75, 0])
                right_circle.set_fill(color=colors[1], opacity=1)
                self.add(left_circle, right_circle)


        self.wait(0.5)


