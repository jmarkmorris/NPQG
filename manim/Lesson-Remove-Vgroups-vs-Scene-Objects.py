from manim import *
config.frame_rate = 30
config.pixel_width = 1000
config.pixel_height = 1000
frame_count = 0

def update_path(mob, dt, tracers, circle_center):
    global frame_count
    if frame_count != 0 :
        if (frame_count % 5 == 0) :
            while len(tracers) > 4 :
                oldtracer = tracers.pop(0)
                mob.remove(oldtracer) # remove the tracer from its vgroup!!!
            tracer = Text(str(frame_count), color=WHITE).scale(0.5).move_to(circle_center)
            mob.add(tracer)
            tracers.append(tracer)
    frame_count += 1

class OrbitingCircles(Scene):
    def construct(self):
        blue_square = Square(color=PURE_BLUE, side_length=0.2, fill_opacity=.1).shift(RIGHT * 3)
        blue_recent_path = VGroup()
        self.add(blue_recent_path)
        self.add(blue_square)
        self.blue_tracers = []
        blue_recent_path.add_updater(lambda mob, dt: update_path(mob, dt, self.blue_tracers, blue_square.get_center()))
        blue_square.add_updater(lambda mob, dt: mob.rotate(TAU/3 * dt, about_point=ORIGIN))
        self.wait(3)