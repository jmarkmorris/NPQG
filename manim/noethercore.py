# # manim noethercore.py noethercore -pqm --disable_caching -p

from manim import *
import random
import json

INDIGO = "#4B0082"
run_time = 16
frame_rate = 60
# paused = False # add pause feature?

# powerpoint png export size
config.pixel_width = 2998
config.pixel_height = 1686
config.frame_rate = frame_rate

radius_I = 0.25
radius_II = 1.00
radius_III = 1.75

class noethercore(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        self.camera.background_color = INDIGO

        spheres = [
            {
                'radius': 0.10,
                'resolution':(30, 15),
                'u_range':(0, TAU),
                'v_range':(0, PI)
            },
            {
                'radius': 0.10,
                'resolution':(30, 15),  
                'u_range':(0, TAU),
                'v_range':(0, PI)
            },
            {
                'radius': 0.10,
                'resolution':(30, 15),
                'u_range':(0, TAU),
                'v_range':(0, PI)
            },
            {
                'radius': 0.10,
                'resolution':(30, 15),
                'u_range':(0, TAU),
                'v_range':(0, PI)
            },
            {
                'radius': 0.10,
                'resolution':(30, 15),
                'u_range':(0, TAU),
                'v_range':(0, PI)
            },
            {
                'radius': 0.10,
                'resolution':(30, 15),
                'u_range':(0, TAU),
                'v_range':(0, PI)
            }
        ]
        charges = [
            {
                'center': (radius_I,0,0),
                'color': PURE_RED,
                'orbit_radius': radius_I,
                'orbit_cycles': 64,
                'orbit_rotate': 0,
                'path_rotate':[0, 0, 1],
                'orbit_normal':[0, 0, 1]
            },
            {
                'center': (-radius_I,0,0),
                'color': PURE_BLUE,
                'orbit_radius': radius_I,
                'orbit_cycles': 64,
                'orbit_rotate': 0,
                'path_rotate':[0, 0, 1],
                'orbit_normal':[0, 0, 1]
            },
            {
                'center': (0,radius_II,0),
                'color': PURE_RED,
                'orbit_radius': radius_II,
                'orbit_cycles': 32,
                'orbit_rotate': PI/2,
                'path_rotate':[0, 1, 0],
                'orbit_normal':[1, 0, 0]
            },
            {
                'center': (0,-radius_II,0),
                'color': PURE_BLUE,
                'orbit_radius': radius_II,
                'orbit_cycles': 32,
                'orbit_rotate': PI/2,
                'path_rotate':[0, 1, 0],
                'orbit_normal':[1, 0, 0]
            },
            {
                'center': (0,0,radius_III),
                'color': PURE_RED,
                'orbit_radius': radius_III,
                'orbit_cycles': 16,
                'orbit_rotate': PI/2,
                'path_rotate':[1, 0, 0],
                'orbit_normal':[0, 1, 0]
            },
            {
                'center': (0,0,-radius_III),
                'color': PURE_BLUE,
                'orbit_radius': radius_III,
                'orbit_cycles': 16,
                'orbit_rotate': PI/2,
                'path_rotate':[1, 0, 0],
                'orbit_normal':[0, 1, 0]
            }
        ]

        kwargs = {
            'x_range': [-5,5,1],
            'y_range': [-5,5,1],
            'z_range': [-5,5,1],
            'x_length': 8,
            'y_length': 8,
            'z_length': 6,
            'axis_config': {
                'tip_shape': ArrowTriangleTip
            }
        }
        axes = ThreeDAxes(**kwargs)
        x_axis_label = axes.get_x_axis_label(label="x")
        self.add(x_axis_label)
        y_axis_label = axes.get_y_axis_label(label="y")
        self.add(y_axis_label)
        z_axis_label = axes.get_z_axis_label(label="z")
        z_axis_label.rotate(PI)
        self.add(z_axis_label)
        self.add(axes)

        animations = []
        for charge in charges:
            orbital_path = Circle(radius=charge['orbit_radius'], color=WHITE, stroke_opacity=0.5, stroke_width=1)
            orbital_path.rotate(angle=charge['orbit_rotate'], axis=charge['path_rotate'])
            self.add(orbital_path)

        for sphere_kwargs, charge in zip(spheres, charges):
            sphere = Sphere(center=charge['center'], **sphere_kwargs)
            sphere.move_to(charge['center']) # needed?
            sphere.set_color(charge['color'])
            self.add(sphere)

            animations.append(Rotating(sphere, radians=TAU*charge['orbit_cycles'], axis=charge['orbit_normal'], about_point=ORIGIN, rate_func=linear, run_time=run_time))

        self.begin_ambient_camera_rotation(rate=TAU/2)
        self.play(*animations)
        self.stop_ambient_camera_rotation()

        self.wait(0)


            #     'scaling': LogBase(),
            # json_string = json.dumps(sphere_kwargs, indent=4)
            # print(json_string)
        # json_string = json.dumps(spheres, indent=4)
        # print(json_string)
        # json_string = json.dumps(charges, indent=4)
        # print(json_string)