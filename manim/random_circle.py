


from manim import *
import random

class RandomCircle(Scene):
    def construct(self):
        circle = Circle(fill_color=DARK_BLUE, fill_opacity=1, stroke_width=0, radius=0.1)
        self.add(circle)
        last_point = circle.get_center()
        for _ in range(20):
            random_angle = random.uniform(0, 3*TAU/2)
            if (last_point[0] > 0) and (last_point[1] > 0) :
                random_angle = random_angle + TAU/2
            elif (last_point[0] > 0) and (last_point[1] < 0) :
                random_angle = random_angle
            if (last_point[0] < 0) and (last_point[1] > 0) :
                random_angle = random_angle + TAU            
            else :
                random_angle = random_angle + TAU/2
            arc = ArcBetweenPoints(last_point, last_point + 0.5*RIGHT, angle=random_angle)
            self.play(MoveAlongPath(circle, arc), run_time=5)
            
            
            line = Line(last_point, circle.get_center(), color=BLUE)
            self.add(line)
            last_point = circle.get_center()
