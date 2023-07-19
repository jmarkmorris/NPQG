import pygame
from pygame.locals import *
from pygame import surface

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
from math import sin, cos, pi
import imageio


paused = False


frame_width = 1200
frame_height = 1200
# frame_width = 2048
# frame_height = 1280
frame_rate = 30
duration = 20
orbit_radius = 0.4
point_charge_representation_radius = 0.03
tracer_origin_radius = 0.008
tracer_angle = 130

# tunables
# the tracer radius increment vs. angle increment is dualistic to v/c - giving the appearance of supra, par, or infra.
# for tracer radius increment, larger is faster, smaller is slower

tracer_radius_increment = [0.005, 0.010, 0.020]
angle_increment_per_frame = [1, 2, 3]
frames_between_tracers = [3, 4, 5, 6]


def calculate_fade_values(spheres):
    fade_values = []
    fade = 1
    fade_delta = 0.01
    fade_min = 0
    for cx, cy, cr in reversed(spheres):
        fade_values.append(fade)
        fade = max(fade - fade_delta, fade_min)
    fade_values.reverse()
    return fade_values

def draw_recent_path(angle, color):
    glBegin(GL_LINE_STRIP)
    glColor3f(*color)
    for i in range(angle - tracer_angle, angle + 1):
        angle_in_radians = i * pi / 180
        x = cos(angle_in_radians) * orbit_radius
        y = sin(angle_in_radians) * orbit_radius
        glVertex2f(x, y)
    glEnd()

def draw_point_charge_representation(x, y, color):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(*color)
    glVertex2f(x, y)
    for i in range(361):
        angle_in_radians = i * pi / 180
        glVertex2f(x + point_charge_representation_radius * cos(angle_in_radians), y + point_charge_representation_radius * sin(angle_in_radians))
    glEnd()

def draw_tracer_origins(sphere_origins, color, num_tracer_origins):
    fade = 0
    fade_max = 1
    fade_delta = 2 * fade_max / num_tracer_origins / 3
    for cx, cy in reversed(sphere_origins):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(*[c if c == 1.0 else fade for c in color])
        glVertex2f(cx, cy)
        for i in range(361):
            glVertex2f(cx + tracer_origin_radius * cos(i * pi / 180), cy + tracer_origin_radius * sin(i * pi / 180))
        glEnd()
        fade = min(fade + fade_delta, fade_max)

def draw_potential_sphere(sphere, fade, color):
    cx, cy, cr = sphere
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glColor3f(*color)
    for i in range(360):
        angle_in_radians = i * pi / 180
        glVertex2f(cx + cr * cos(angle_in_radians), cy + cr * sin(angle_in_radians))
    glEnd()


def display_legend(x, y, r, g, b, font, string):
    glColor3f(r, g, b)
    glRasterPos2f(x, y)
    for character in string:
        glutBitmapCharacter(font, ord(character))



def draw_dipole(tracer_radius_increment, angle_increment_per_frame, frames_between_tracers):
    global blue_angle, red_angle, frame, blue_tracer_origins, red_tracer_origins

    blue_angle_in_radians = blue_angle * pi / 180
    blue_x = cos(blue_angle_in_radians) * orbit_radius
    blue_y = sin(blue_angle_in_radians) * orbit_radius

    red_angle_in_radians = red_angle * pi / 180
    red_x = cos(red_angle_in_radians) * orbit_radius
    red_y = sin(red_angle_in_radians) * orbit_radius

    num_tracer_origins = math.floor(tracer_angle / (angle_increment_per_frame * frames_between_tracers))

    if frame % (frames_between_tracers) == 0:
        blue_tracer_origins.append((blue_x, blue_y, 0))
        red_tracer_origins.append((red_x, red_y, 0))

    # calculate fade values for all spheres
    blue_fade_values = calculate_fade_values(blue_tracer_origins)
    red_fade_values = calculate_fade_values(red_tracer_origins)

    # draw spheres with calculated fade values but do so in alternating fashion so that the order of spheres drawn looks good.
    for (red_potential_sphere, red_fade), (blue_potential_sphere, blue_fade) in zip(zip(red_tracer_origins, red_fade_values), zip(blue_tracer_origins, blue_fade_values)):
            
        # draw red sphere
        draw_potential_sphere(red_potential_sphere, red_fade, (1.0*red_fade, 0.1, 0.1))

        # draw blue sphere
        draw_potential_sphere(blue_potential_sphere, blue_fade, (0.1, 0.1, 1.0*blue_fade))


    # the recent path of the electrino
    draw_recent_path(blue_angle, (0.6, 0.6, 0.6))

    # the recent path of the positrino
    draw_recent_path(red_angle, (0.6, 0.6, 0.6))

    # the electrino point charge representation as a small blue sphere
    draw_point_charge_representation(blue_x, blue_y, (0.0, 0.0, 1.0))

    # the positrino point charge representation as a small red sphere
    draw_point_charge_representation(red_x, red_y, (1.0, 0.0, 0.0))

    # Storing electrino tracer origins
    for cx, cy, cr in blue_tracer_origins:
        if cr == tracer_radius_increment:
            blue_potential_sphere_origins.append((blue_x, blue_y))
            if len(blue_potential_sphere_origins) > num_tracer_origins:
                blue_potential_sphere_origins.pop(0)

    # Storing positrino tracer origins
    for cx, cy, cr in red_tracer_origins:
        if cr == tracer_radius_increment:
            red_potential_sphere_origins.append((red_x, red_y))
            if len(red_potential_sphere_origins) > num_tracer_origins:
                red_potential_sphere_origins.pop(0)

    blue_tracer_origins = [(cx, cy, cr + tracer_radius_increment) for cx, cy, cr in blue_tracer_origins if cr < 2]
    red_tracer_origins = [(cx, cy, cr + tracer_radius_increment) for cx, cy, cr in red_tracer_origins if cr < 2]

    # Leaving electrino tracer origins on path
    draw_tracer_origins(blue_potential_sphere_origins, (0.0, 0.0, 1.0), num_tracer_origins)

    # Leaving positrino tracer origins on path
    draw_tracer_origins(red_potential_sphere_origins, (1.0, 0.0, 0.0), num_tracer_origins)


    blue_angle += angle_increment_per_frame
    red_angle += angle_increment_per_frame
    frame +=1



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


for a_value in tracer_radius_increment:
    for b_value in angle_increment_per_frame:
        for c_value in frames_between_tracers:
            frames = []
            frame = 0
            blue_angle = 0
            red_angle = 180
            # these lists keep track of the expanding spheres
            blue_tracer_origins = []
            red_tracer_origins = []
            blue_potential_sphere_origins = []
            red_potential_sphere_origins = []
            while frame < duration * fps:

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
                    draw_dipole(a_value, b_value, c_value)
                    # label_text = f"tracer_radius_increment: {a_value}, angle_increment_per_frame: {b_value}, frames_between_tracers: {c_value}"
                    # x = 100
                    # y = 200
                    # r, g, b = 1, 1, 1 # white color
                    # font = GLUT_BITMAP_9_BY_15
                    # string = "mark"
                    # glClearColor(0.5, 0, 0.5, 1) # purple background
                    # glClear(GL_COLOR_BUFFER_BIT)
                    # display_legend(x, y, r, g, b, font, string)
                    # glutSwapBuffers()
                    pygame.display.flip()
                    clock.tick(fps)

                    # this works too, but won't pick up the pygame surface labels.  Also this may be slower.
                    data = glReadPixels(0, 0, frame_width, frame_height, GL_RGB, GL_UNSIGNED_BYTE)
                    image = pygame.image.frombuffer(data, (frame_width, frame_height), "RGB")

                    # This will make the mp4 run in the reverse direction
                    # image = pygame.transform.flip(image, False, True)
                    frames.append(pygame.surfarray.array3d(image))
                    frame += 1

            filename = f"dipole-{a_value}-{b_value}-{c_value}.mp4"
            imageio.mimwrite(filename, frames, fps=fps)

pygame.quit()


# to do

# reframe everything in terms of true units where field speed = 1 = @
# q = -/+ 1
# print the tunables on a label area below the animation? 
# display all the parameters on the frame
# unknot why everything is confused.
# It would be nice if frame rate was independent and we just displayed the time scale.
# from the point of view of the point charges, nothing changes. They are surfing on a particular point in the superimposed wave.
# add coloring for the potential in each small grid cell - what is the low, mean, high?
# i guess the angle increment per frame is the proxy for velocity. So can we tie it to velocity?
# show the chords from the current location to where the intersecting partner and self potentials were emitted.  **** Great feature.
# I'm having problems getting the mp4 to have the same orientation as the screen. if the screen is landscape, the mp4 is portrait. Temporarily using square frame.
# Redo how length of tracer path and tracer origins are calculated so they tie together automatically.
# Awesome idea : Animate right to left in landscape mode with logarithmic x.  Dipole I, then II, then III, then personality charges. 
# Then start merging them from left to right and showing the precession as well.
# I need to write the routines so they can all take an x,y,z,t displacement or a vector velocity!
# They also need to be shrinkable from the smallest visible red and blue spheres and then incrementing for each step up. Hmm interesting.
# so perhaps a small progression 1,2,4,8,16,32... and then double that.
# Can you make poster size art? That would be cool to make my own posters and print them!


# bugs
# can't get labels to work
# loop is working but sometimes tracer origins are wrong
