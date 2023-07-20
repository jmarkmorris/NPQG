# python3 dipole_orbit_opengl.py
import pygame
from pygame.locals import *
from pygame import surface

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
from math import sin, cos, tau
import imageio

# animation
duration = 12
frame_rate = 30
paused = False

frames_between_tracer_origins = [6]
potential_sphere_radius_increment = [0.03, 0.02]
per_frame_increment_angle_in_radians = [2*tau/360]

# powerpoint png export size
# frame_width = 2999  
# frame_height = 1687
# frame_width = 2048
# frame_height = 1280
frame_width = 2000
frame_height = 1200

# tunables
# the tracer radius increment vs. angle_in_radians increment is dualistic to v/c - giving the appearance of supra, par, or infra.
# for tracer radius increment, larger is faster, smaller is slower

#——————————————————————————————————————————————————————————————————————————————

def draw_point_charge_representation(Q):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(*Q["color"])
    x,y = Q["x"],Q["y"]
    glVertex2f(x,y)
    for i in range(361):
        angle_in_radians = i * tau / 360
        glVertex2f(x + Q["point_charge_representation_radius"] * cos(angle_in_radians), y + Q["point_charge_representation_radius"] * sin(angle_in_radians))
    glEnd()

def draw_tracer_origins(Q):
    tracer_fade = 0
    tracer_fade_max = 1
    tracer_fade_delta = (tracer_fade_max / Q["num_tracer_origins"])
    for cx, cy, cr in reversed(Q["tracer_origins"]):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(*[c if c == 1.0 else tracer_fade for c in Q["color"]])
        glVertex2f(cx, cy)
        for i in range(361):
            glVertex2f(cx + Q["tracer_origin_radius"] * cos(i * tau / 360), cy + Q["tracer_origin_radius"] * sin(i * tau / 360))
        glEnd()
        tracer_fade = min(tracer_fade + tracer_fade_delta, tracer_fade_max)

#——————————————————————————————————————————————————————————————————————————————

def calculate_sphere_fade_values(Q):
    sphere_fade_values = []
    sphere_fade = 1
    sphere_fade_min = 0
    for cx, cy, cr in Q["potential_spheres"]:
        sphere_fade_values.insert(0, sphere_fade)
        sphere_fade = max(sphere_fade - Q["sphere_fade_delta"], sphere_fade_min)
    return sphere_fade_values

def draw_potential_sphere(sphere, fade_value, color):
    cx, cy, cr = sphere
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    # NOTE : This only works because we are using R (1,0,0) and B(0,0,1). 
    # NOTE : If want to use anything other than G (0,1,0) like purple, we need to redesign this.
    color = (color[0] * fade_value, color[1] * fade_value, color[2] * fade_value)
    glColor3f(*color)
    for i in range(361):
        angle_in_radians = i * tau / 360
        glVertex2f(cx + cr * cos(angle_in_radians), cy + cr * sin(angle_in_radians))
    glEnd()

# def draw_recent_path(Q):
#     glBegin(GL_LINE_STRIP)
#     glColor3f(*Q["color"])

#     loop_angle_in_radians = Q["angle_in_radians"] - Q["trailing_path_angle_in_radians"]
#     while loop_angle_in_radians < Q["angle_in_radians"] :
#         path_x = cos(loop_angle_in_radians) * Q["dipole_orbit_radius"]
#         path_y = sin(loop_angle_in_radians) * Q["dipole_orbit_radius"]
#         glVertex2f(path_x, path_y)
#         loop_angle_in_radians += Q["per_frame_increment_angle_in_radians"]
#     glEnd()

def draw_recent_path(Q):
    # Enable blending
    glEnable(GL_BLEND)
    # Set blending function
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glBegin(GL_LINE_STRIP)

    loop_angle_in_radians = Q["angle_in_radians"] - Q["trailing_path_angle_in_radians"]
    while loop_angle_in_radians < Q["angle_in_radians"] :
        # Calculate alpha value based on current angle
        alpha = (loop_angle_in_radians - (Q["angle_in_radians"] - Q["trailing_path_angle_in_radians"])) / Q["trailing_path_angle_in_radians"]
        # Set color with alpha value
        glColor4f(*Q["color"], alpha)

        path_x = cos(loop_angle_in_radians) * Q["dipole_orbit_radius"]
        path_y = sin(loop_angle_in_radians) * Q["dipole_orbit_radius"]
        glVertex2f(path_x, path_y)
        loop_angle_in_radians += Q["per_frame_increment_angle_in_radians"]
    glEnd()


#——————————————————————————————————————————————————————————————————————————————

def update_path(Q):
    global frame_count

    Q["x"] = cos(Q["angle_in_radians"]) * Q["dipole_orbit_radius"]
    Q["y"] = sin(Q["angle_in_radians"]) * Q["dipole_orbit_radius"]

    if frame_count % (Q["frames_between_tracer_origins"]) == 0:
        Q["potential_spheres"].append((Q["x"], Q["y"], 0))

    Q["sphere_fade_values"] = calculate_sphere_fade_values(Q)

    draw_recent_path(Q)
    draw_point_charge_representation(Q)
    draw_tracer_origins(Q)
    for index, potential_sphere in enumerate(Q["potential_spheres"]) :
        draw_potential_sphere(potential_sphere, Q["sphere_fade_values"][index], Q["color"])
            

    if frame_count % (Q["frames_between_tracer_origins"]) == 0:
        Q["tracer_origins"].append((Q["x"], Q["y"], 0))
        if len(Q["tracer_origins"]) > Q["num_tracer_origins"]:
            Q["tracer_origins"].pop(0)

    Q["potential_spheres"] = [(cx, cy, cr + Q["potential_sphere_radius_increment"]/Q["frames_between_tracer_origins"]) for cx, cy, cr in Q["potential_spheres"] if cr < 2]
    Q["angle_in_radians"] += Q["per_frame_increment_angle_in_radians"]


pygame.init()
pygame.font.init()
display = pygame.display.list_modes()[0]
pygame.display.set_mode((frame_width, frame_height), DOUBLEBUF|OPENGL)
aspect_ratio = frame_width / frame_height
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(-aspect_ratio, aspect_ratio,-1,1)
clock = pygame.time.Clock()

for a_radius in potential_sphere_radius_increment:
    for b_angle_in_radians_increment in per_frame_increment_angle_in_radians:
        for c_fbt in frames_between_tracer_origins:
            frames = []
            frame_count = 0

            Q = {
                "blue": {
                    "angle_in_radians": tau/2,
                    "trailing_path_angle_in_radians": 130*tau/360,
                    "potential_sphere_radius_increment": a_radius,
                    "per_frame_increment_angle_in_radians": b_angle_in_radians_increment,
                    "frames_between_tracer_origins": c_fbt,
                    "num_tracer_origins": 1,
                    "opacity": 1,
                    "color": (0.0, 0.0, 1.0),
                    "tracer_origins": [],
                    "x": -0.4,
                    "y": 0,
                    "dipole_orbit_radius": 0.5,
                    "point_charge_representation_radius": 0.03,
                    "tracer_origin_radius": 0.01,
                    "sphere_fade_delta": 0.020,
                    "potential_spheres": []
                },
                "red": {
                    "angle_in_radians": 0,
                    "trailing_path_angle_in_radians": 130*tau/360,
                    "potential_sphere_radius_increment": a_radius,
                    "per_frame_increment_angle_in_radians": b_angle_in_radians_increment,
                    "frames_between_tracer_origins": c_fbt,
                    "num_tracer_origins": 1,
                    "opacity": 1,
                    "color": (1.0, 0.0, 0.0),
                    "tracer_origins": [],
                    "x": 0.4,
                    "y": 0,
                    "dipole_orbit_radius": 0.5,
                    "point_charge_representation_radius": 0.03,
                    "tracer_origin_radius": 0.01,
                    "sphere_fade_delta": 0.020,
                    "potential_spheres": []
                }
            }
            for Q_key in Q:
                Q[Q_key]["sphere_fade_values"] = calculate_sphere_fade_values(Q[Q_key])
                Q[Q_key]["num_tracer_origins"] = Q[Q_key]["trailing_path_angle_in_radians"] / (Q[Q_key]["frames_between_tracer_origins"]*Q[Q_key]["per_frame_increment_angle_in_radians"]) - 1
                draw_recent_path(Q[Q_key])

            while frame_count < duration * frame_rate:

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
                    for Q_key in Q:
                        update_path(Q[Q_key])

                    label_text = f"potential_sphere_radius_increment: {a_radius}, per_frame_increment_angle_in_radians: {b_angle_in_radians_increment}, frames_between_tracer_origins: {c_fbt}"
                    x, y = -1.2, 0.9
                    glColor3f(0.5, 0.0, 0.5) # set the color to purple
                    glRectf(x-0.1, y-.03, x + 2.6, y+.05) # draw the rectangle
                    glColor3f(1, 1, 1) # white color
                    glRasterPos2f(x, y)
                    for character in label_text:
                        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(character))

                    glutSwapBuffers()
                    pygame.display.flip()
                    clock.tick(frame_rate)

                    data = glReadPixels(0, 0, frame_width, frame_height, GL_RGB, GL_UNSIGNED_BYTE)
                    image = pygame.image.frombuffer(data, (frame_width, frame_height), "RGB")
                    image = pygame.transform.rotate(image, 270)
                    # This will make the mp4 run in the reverse direction
                    # image = pygame.transform.flip(image, False, True)
                    frames.append(pygame.surfarray.array3d(image))
                    frame_count +=1

            filename = f"dipole-{a_radius}-{b_angle_in_radians_increment}-{c_fbt}.mp4"
            imageio.mimwrite(filename, frames, fps=frame_rate)

pygame.quit()
