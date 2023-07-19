# bring variable name in line with manim
# use dictionary like manim
# use radians
# test
# finally compare code and look for more optimizations


# python3 dipole_orbit_opengl.py
import pygame
from pygame.locals import *
from pygame import surface

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
from math import sin, cos, pi
import imageio

# animation
duration = 12
frame_rate = 30
frames_between_tracer_origins = [2, 3]
paused = False

# radii
dipole_orbit_radius = 0.4
point_charge_representation_radius = 0.03
tracer_origin_radius = 0.008
potential_sphere_radius_increment = [0.015, 0.014, 0.013, 0.012, 0.011, 0.01, 0.008, 0.006]
sphere_fade_delta = 0.010

# angles in radians
trailing_path_angle_in_radians = 130*TAU/360
per_frame_increment_angle_in_radians = [2*TAU/360, 3*TAU/360]

frame_width = 2999  # powerpoint png export size
frame_height = 1687
# frame_width = 2048
# frame_height = 1280

# tunables
# the tracer radius increment vs. angle_in_radians increment is dualistic to v/c - giving the appearance of supra, par, or infra.
# for tracer radius increment, larger is faster, smaller is slower


def calculate_sphere_fade_values(spheres):
    sphere_fade_values = []
    sphere_fade = 1
    sphere_fade_min = 0
    for _ in spheres:
        sphere_fade_values.insert(0, sphere_fade)
        sphere_fade = max(sphere_fade - sphere_fade_delta, sphere_fade_min)
    return sphere_fade_values

def draw_recent_path(point_charge_state):
    glBegin(GL_LINE_STRIP)
    glColor3f(*color)

    loop_angle_in_radians = point_charge_state["angle_in_radians"] - trailing_path_angle_in_radians
    while loop_angle_in_radians < point_charge_state["angle_in_radians"] :
        path_x = cos(loop_angle_in_radians) * dipole_orbit_radius
        path_y = sin(loop_angle_in_radians) * dipole_orbit_radius
        glVertex2f(path_x, path_y)
        loop_angle_in_radians += 1*TAU/360
    glEnd()

def draw_point_charge_representation(x, y, point_charge_state):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(*point_charge_state["color"])
    glVertex2f(x, y)
    for i in range(361):
        angle_in_radians = i * pi / 180
        glVertex2f(x + point_charge_representation_radius * cos(angle_in_radians), y + point_charge_representation_radius * sin(angle_in_radians))
    glEnd()

def draw_tracer_origins(point_charge_state, color, num_tracer_origins):
    tracer_fade = 0
    tracer_fade_max = 1
    tracer_fade_delta = 2 * tracer_fade_max / num_tracer_origins / 3
    for cx, cy, cr in reversed(point_charge_state["tracer_origins"]):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(*[c if c == 1.0 else tracer_fade for c in point_charge_state["color"]])
        glVertex2f(cx, cy)
        for i in range(361):
            glVertex2f(cx + tracer_origin_radius * cos(i * pi / 180), cy + tracer_origin_radius * sin(i * pi / 180))
        glEnd()
        tracer_fade = min(tracer_fade + tracer_fade_delta, tracer_fade_max)

def draw_potential_sphere(sphere, fade_value, color):
    cx, cy, cr = sphere
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    # NOTE : This only works because we are using R (1,0,0) and B(0,0,1). 
    # NOTE : If want to use anything other than G (0,1,0) like purple, we need to redesign this.
    color = (color[0] * fade_value, color[1] * fade_value, color[2] * fade_value)
    glColor3f(*color)
    for i in range(360):
        angle_in_radians = i * pi / 180
        glVertex2f(cx + cr * cos(angle_in_radians), cy + cr * sin(angle_in_radians))
    glEnd()

def display_legend(x, y, r, g, b, font, string):
    glColor3f(0.5, 0.0, 0.5) # set the color to purple
    glRectf(x-.1, y-.03, x + 1.3, y+.05) # draw the rectangle
    glColor3f(r, g, b)
    glRasterPos2f(x, y)
    for character in string:
        glutBitmapCharacter(font, ord(character))

########################################################

def update_path(point_charge_state):
    global frame_count, per_frame_increment_angle_in_radians, num_tracer_origins, frames_between_tracer_origins, potential_sphere_radius_increment)

    point_charge_state["x"] = cos(point_charge_state["angle_in_radians"]) * dipole_orbit_radius
    point_charge_state["y"] = sin(point_charge_state["angle_in_radians"]) * dipole_orbit_radius

    if frame_count % (frames_between_tracer_origins) == 0:
        point_charge_state["potential_spheres"].append((point_charge_state["x"], point_charge_state["y"], 0))

    num_tracer_origins = math.floor(trailing_path_angle_in_radians / (frames_between_tracer_origins*per_frame_increment_angle_in_radians))

    potential_spheres = point_charge_state["potential_spheres"]
    point_charge_state["sphere_fade_values"] = calculate_sphere_fade_values(potential_spheres)

    # draw spheres with calculated sphere_fade values but do so in alternating fashion so that the order of spheres drawn looks good.
    for index, potential_sphere in enumerate(point_charge_state["potential_spheres"]) :
        fade_value = point_charge_state["sphere_fade_values"][index]
        sphere = draw_potential_sphere(potential_sphere, fade_value, point_charge_state["color"]))
        updated_path.add(sphere)
            

        draw_recent_path(blue_angle_in_radians, (0.6, 0.6, 0.6))

        draw_point_charge_representation(blue_x, blue_y, (0.0, 0.0, 1.0))

    if frame_count % (frames_between_tracer_origins) == 0:
        # print(f"frame_count: {frame_count}")

        blue_tracer_origins.append((blue_x, blue_y, 0))
        if len(blue_tracer_origins) > num_tracer_origins:
            blue_tracer_origins.pop(0)

        blue_potential_spheres = [(cx, cy, cr + potential_sphere_radius_increment/frames_between_tracer_origins) for cx, cy, cr in blue_potential_spheres if cr < 2]

        draw_tracer_origins(point_charge_state, num_tracer_origins)



    blue_angle_in_radians += per_frame_increment_angle_in_radians
    red_angle_in_radians += per_frame_increment_angle_in_radians
    frame_count +=1

pygame.init()
pygame.font.init()
display = pygame.display.list_modes()[0]
pygame.display.set_mode((frame_width, frame_height), DOUBLEBUF|OPENGL)

aspect_ratio = frame_width / frame_height
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(-aspect_ratio, aspect_ratio,-1,1)

clock = pygame.time.Clock()

fps = frame_rate

for a_radius in potential_sphere_radius_increment:
    for b_angle_in_radians_increment in per_frame_increment_angle_in_radians:
        for c_fbt in frames_between_tracer_origins:
            frames = []
            frame_count = 0
            # Add the initial circles and tracer_origins to the dictionary.
            self.point_charge_state = {
                "blue": {
                    "angle_in_radians": 0,
                    "opacity": 1,
                    "color": (0.0, 0.0, 1.0),
                    "tracer_origins": [],
                    "x": dipole_orbit_radius,
                    "y": 0,
                    "potential_spheres": []
                },
                "red": {
                    "angle_in_radians": PI,
                    "opacity": 1,
                    "color": (1.0, 0.0, 0.0),
                    "tracer_origins": [],
                    "x": -dipole_orbit_radius,
                    "y": 0,
                    "potential_spheres": []
                }
            }
            blue_angle_in_radians = 0
            red_angle_in_radians = PI
            # these lists keep track of the expanding spheres
            blue_potential_spheres = []
            red_potential_spheres = []
            blue_tracer_origins = []
            red_tracer_origins = []
            while frame_count < duration * fps:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            quit()
                        elif event.key == K_SPACE:
                            paused = not paused

                if not paused:
                    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                    update_path(self.point_charge_state, a_radius, b_angle_in_radians_increment, c_fbt)
                    label_text = f"potential_sphere_radius_increment: {a_radius}, per_frame_increment_angle_in_radians: {b_angle_in_radians_increment}, frames_between_tracer_origins: {c_fbt}"
                    filename = f"dipole-{a_radius}-{b_angle_in_radians_increment}-{c_fbt}.mp4"
                    x = -0.65
                    y = 0.9
                    r, g, b = 1, 1, 1 # white color
                    # font = GLUT_BITMAP_HELVETICA_18
                    font = GLUT_BITMAP_TIMES_ROMAN_24
                    display_legend(x, y, r, g, b, font, label_text)

                    glutSwapBuffers()
                    pygame.display.flip()
                    clock.tick(fps)

                    data = glReadPixels(0, 0, frame_width, frame_height, GL_RGB, GL_UNSIGNED_BYTE)
                    image = pygame.image.frombuffer(data, (frame_width, frame_height), "RGB")
                    image = pygame.transform.rotate(image, 270)
                    # This will make the mp4 run in the reverse direction
                    # image = pygame.transform.flip(image, False, True)
                    frames.append(pygame.surfarray.array3d(image))

            imageio.mimwrite(filename, frames, fps=fps)

pygame.quit()
