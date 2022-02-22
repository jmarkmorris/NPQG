from manim import *

class Electron(Scene):
    def construct(self):
        circle1 = Circle(radius=1)  # create a circle
        circle1.set_fill(WHITE, opacity=0)
        circle1.set_stroke(PURPLE_D, width=20)

        circle2 = Circle(radius=1.5)  # create a circle
        circle2.set_fill(WHITE, opacity=0)
        circle2.set_stroke(PURPLE_C,width=20)

        circle3 = Circle(radius=2)  # create a circle
        circle3.set_fill(WHITE, opacity=0)
        circle3.set_stroke(PURPLE_B,width=20)

        circle4 = Circle(radius=3)  # create a circle
        circle4.set_fill(WHITE, opacity=0)
        circle4.set_stroke(PURPLE_A,width=20)

        dot11 = Dot().move_to(circle1.get_left())
        dot12 = Dot().move_to(circle1.get_right())
        dot11.set_color(PURE_RED)
        dot12.set_color(PURE_BLUE)

        dot21 = Dot().move_to(circle2.get_left())
        dot22 = Dot().move_to(circle2.get_right())
        dot21.set_color(PURE_RED)
        dot22.set_color(PURE_BLUE)

        dot31 = Dot().move_to(circle3.get_left())
        dot32 = Dot().move_to(circle3.get_right())
        dot31.set_color(PURE_RED)
        dot32.set_color(PURE_BLUE)

        dot41 = Dot(point=([3., 0., 0.]))
        dot42 = Dot(point=([3., 0., 0.]))
        dot43 = Dot(point=([3., 0., 0.]))
        dot44 = Dot(point=([3., 0., 0.]))
        dot45 = Dot(point=([3., 0., 0.]))
        dot46 = Dot(point=([3., 0., 0.]))

        dot41.rotate_about_origin(0*DEGREES)
        dot42.rotate_about_origin(60*DEGREES)
        dot43.rotate_about_origin(120*DEGREES)
        dot44.rotate_about_origin(180*DEGREES)
        dot45.rotate_about_origin(240*DEGREES)
        dot46.rotate_about_origin(300*DEGREES)

        dot41.set_color(PURE_BLUE)
        dot42.set_color(PURE_BLUE)
        dot43.set_color(PURE_BLUE)
        dot44.set_color(PURE_BLUE)
        dot45.set_color(PURE_BLUE)
        dot46.set_color(PURE_BLUE)

        g1 = VGroup(circle1, dot11, dot12)
        g2 = VGroup(circle2, dot21, dot22)
        g3 = VGroup(circle3, dot31, dot32)
        g4 = VGroup(circle4, dot41, dot42, dot43, dot44, dot45, dot46)

        g1.add_updater(lambda mobject, dt: mobject.rotate(-dt*360*DEGREES))
        g2.add_updater(lambda mobject, dt: mobject.rotate(dt*180*DEGREES))
        g3.add_updater(lambda mobject, dt: mobject.rotate(-dt*90*DEGREES))
        g4.add_updater(lambda mobject, dt: mobject.rotate(dt*15*DEGREES))

        self.add(g1)
        self.add(g2)
        self.add(g3)
        self.add(g4)

        self.wait(16)
        self.wait(1)

