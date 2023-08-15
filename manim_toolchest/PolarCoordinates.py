# manim -pqh --disable_caching PolarCoordinates.py PolarCoordinates -p

from manim import *

INDIGO = "#4B0082"
ELECTRIC_PURPLE = "#8F00FF"

# config.background_color = WHITE

class PolarCoordinates(Scene):
    def construct(self):

        self.camera.background_color = INDIGO

        # azimuth is theta from (1,0) going CCW (test to make sure)
        P = PolarPlane(  
            azimuth_units="PI radians",
            azimuth_step=12,
            size=6,  
            azimuth_label_font_size=33.6,  
            radius_config={"font_size": 33.6, "stroke_color": WHITE},
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 2,
                "stroke_opacity": 1
            }
        ).add_coordinates()  
        self.add(P)

        V = Vector(P.polar_to_point(3, PI/4), stroke_width=2)
        self.add(V)