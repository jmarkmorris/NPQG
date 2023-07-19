# manim --show_in_file_browser dipole_orbit_manim.py OrbitingCircles -p
from manim import *
from manim import RED, BLUE 
from manim import config

# animation
duration = 12
frame_rate = 60
frames_between_tracer_origins = 6

# radii
dipole_orbit_radius = 2.0
point_charge_representation_radius = 0.1
tracer_origin_radius = 0.02
sphere_fade_delta = 0.010
potential_sphere_radius_increment = 0.06

# angles in radians
total_rotation_angle_in_radians = 2*TAU
trailing_path_angle_in_radians = 130*TAU/360
per_frame_increment_angle_in_radians = total_rotation_angle_in_radians / (duration * frame_rate )
num_tracer_origins = trailing_path_angle_in_radians / (per_frame_increment_angle_in_radians * frames_between_tracer_origins) - 1

# powerpoint png export size
config.pixel_width = 2998
config.pixel_height = 1686
config.frame_rate = frame_rate
frame_width = 2  
frame_height = 2
frame_count = 0

def draw_recent_path(point_charge_state):
    # not sure these three lines are needed
    path_x = np.cos(point_charge_state["angle_in_radians"] - trailing_path_angle_in_radians) * dipole_orbit_radius
    path_y = np.sin(point_charge_state["angle_in_radians"] - trailing_path_angle_in_radians) * dipole_orbit_radius
    points = [[path_x,path_y,0]]
    loop_angle_in_radians = point_charge_state["angle_in_radians"] - trailing_path_angle_in_radians
    while loop_angle_in_radians < point_charge_state["angle_in_radians"] :
        path_x = np.cos(loop_angle_in_radians) * dipole_orbit_radius
        path_y = np.sin(loop_angle_in_radians) * dipole_orbit_radius
        points.append([path_x, path_y, 0])
        loop_angle_in_radians += 1*TAU/360
    
    recent_path = VGroup()
    n_segments = len(points) - 1
    for path_segment in range(n_segments):
        segment = Line(points[path_segment], points[path_segment+1])
        segment.set_color(point_charge_state["color"])
        segment.set_stroke(opacity=(path_segment+1)/n_segments)
        recent_path.add(segment)
    
    return recent_path

########################################################

def update_path(mob, dt, point_charge_state):
    global frame_count, per_frame_increment_angle_in_radians, num_tracer_origins
    
    color=point_charge_state["color"]
    
    point_charge_state["angle_in_radians"] += per_frame_increment_angle_in_radians
    point_charge_state["opacity"] = max(0, point_charge_state["opacity"] - dt / 10)
    updated_path = draw_recent_path(point_charge_state)
    
    if (frame_count % frames_between_tracer_origins == 0) :
        tracer_origin = Circle(color=color, radius=tracer_origin_radius, fill_opacity=1).move_to(point_charge_state["circle"].get_center())
        point_charge_state["tracer_origins"].append(tracer_origin)
        if (len(point_charge_state["tracer_origins"]) > num_tracer_origins) :
            point_charge_state["tracer_origins"].pop(0)
        point_charge_state["potential_spheres"].append((point_charge_state["circle"].get_center()[0], point_charge_state["circle"].get_center()[1], 0))


    potential_spheres = point_charge_state["potential_spheres"]
    point_charge_state["sphere_fade_values"] = calculate_sphere_fade_values(potential_spheres)
    for index, potential_sphere in enumerate(point_charge_state["potential_spheres"]) :
        fade_value = point_charge_state["sphere_fade_values"][index]
        sphere = draw_potential_sphere(potential_sphere, fade_value, interpolate_color(BLACK, point_charge_state["color"], fade_value))
        updated_path.add(sphere)

    point_charge_state["potential_spheres"] = [(cx, cy, cr + potential_sphere_radius_increment/frames_between_tracer_origins) for cx, cy, cr in point_charge_state["potential_spheres"] if cr < 5]

    dot = 0
    for tracer_origin in point_charge_state["tracer_origins"] :
        tracer_origin.set_color(interpolate_color(color, WHITE, (num_tracer_origins - dot) / (2 * num_tracer_origins)))
        updated_path.add(tracer_origin)
        dot += 1

    mob.become(updated_path)

def calculate_sphere_fade_values(spheres):
    sphere_fade_values = []
    sphere_fade = 1
    sphere_fade_min = 0
    for _ in spheres:
        sphere_fade_values.insert(0, sphere_fade)
        sphere_fade = max(sphere_fade - sphere_fade_delta, sphere_fade_min)
    return sphere_fade_values

def draw_potential_sphere(sphere, sphere_fade, color):
    cx, cy, cr = sphere
    circle = Circle(radius=cr, color=color, stroke_width=2, fill_opacity=0).move_to([cx, cy, 0])
    circle.set_stroke(opacity=sphere_fade)
    return circle

def display_legend(x, y, color, font, string):
    
    # Create the rectangle
    rect = Rectangle(width=1.4, height=0.08, fill_color=PURPLE, fill_opacity=1)
    rect.next_to(np.array([x,y,0]), LEFT)
    
    # Create the text
    text = Text(string, color=color, font=font)
    text.next_to(rect, RIGHT)
    


def get_updater(self, point_charge_state_key):
    def updater(mob, dt):
        update_path(mob, dt, self.point_charge_state[point_charge_state_key])
    return updater

class OrbitingCircles(Scene):
    
    # the construct is called once per animation.
    def construct(self):
        global frame_count

        # Add the initial circles and tracer_origins to the dictionary.
        self.point_charge_state = {
            "blue": {
                "circle": Circle(color=PURE_BLUE, radius=point_charge_representation_radius, fill_opacity=1).shift(RIGHT * dipole_orbit_radius),
                "angle_in_radians": 0,
                "opacity": 1,
                "color": PURE_BLUE,
                "tracer_origins": [],
                "potential_spheres": []
            },
            "red": {
                "circle": Circle(color=PURE_RED, radius=point_charge_representation_radius, fill_opacity=1).shift(LEFT * dipole_orbit_radius),
                "angle_in_radians": PI,
                "opacity": 1,
                "color": PURE_RED,
                "tracer_origins": [],
                "potential_spheres": []
            }
        }
        for point_charge_state_key in self.point_charge_state:
            potential_spheres = self.point_charge_state[point_charge_state_key]["potential_spheres"]
            sphere_fade_values = calculate_sphere_fade_values(potential_spheres)
            self.point_charge_state[point_charge_state_key]["sphere_fade_values"] = sphere_fade_values
            self.add(self.point_charge_state[point_charge_state_key]["circle"])
            self.point_charge_state[point_charge_state_key]['recent_path'] = draw_recent_path(self.point_charge_state[point_charge_state_key])
            self.add(self.point_charge_state[point_charge_state_key]['recent_path'])
        

        for point_charge_state_key in self.point_charge_state:
            updater = get_updater(self, point_charge_state_key)
            self.point_charge_state[point_charge_state_key]['recent_path'].add_updater(updater)

        self.add_updater(self.increment_frame_count)

        self.play(
            Rotate(self.point_charge_state["blue"]["circle"], angle=total_rotation_angle_in_radians, about_point=ORIGIN),
            Rotate(self.point_charge_state["red"]["circle"], angle=total_rotation_angle_in_radians, about_point=ORIGIN),
            run_time=duration,
            rate_func=linear,
        )

        for point_charge_state_key in self.point_charge_state:
            updater = get_updater(self, point_charge_state_key)
            self.point_charge_state[point_charge_state_key]['recent_path'].remove_updater(updater)

    def increment_frame_count(self, dt):
        global frame_count
        frame_count += 1