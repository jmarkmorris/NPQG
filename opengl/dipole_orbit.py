import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from math import sin, cos, pi
import imageio

blue_angle = 0
red_angle = 180
frame = 0
paused = False

# Lists
blue_circles = []
red_circles = []
# these lists keep track of the starting points of the expanding circles
blue_circle_centers = []
red_circle_centers = []
frame_width = 1200
frame_height = 1200
# frame_width = 2048
# frame_height = 1280
frame_rate = 30
duration = 20
orbit_radius = 0.5
point_charge_representation_radius = 0.03
tracer_origin_radius = 0.01
tracer_angle = 130

# tunables
# the tracer radius increment vs. angle increment is dualistic to v/c - giving the appearance of supra, par, or infra.
# for tracer radius increment, larger is faster, smaller is slower


# very pleasing
# tracer_radius_increment = 0.005 
# angle_increment = 1
# frames_between_tracers = 4

# # gorgeous
# tracer_radius_increment = 0.001 
# angle_increment = 3
# frames_between_tracers = 6

# # good set for simple v < @
# tracer_radius_increment = 0.01 
# angle_increment = 1
# frames_between_tracers = 5

# # good set for v=@.  
# tracer_radius_increment = 0.02  
# angle_increment = 1
# frames_between_tracers = 12

# frames_between_tracers = 12
# frames_between_tracers = 8
# frames_between_tracers = 4  #wow!
# frames_between_tracers = 2  #wow!
# frames_between_tracers = 1  #wow!

# the tracer radius increment vs. angle increment is dualistic to v/c - giving the appearance of supra, par, or infra.
# smaller is towards > @ –– larger is towards < @, 
# tracer_radius_increment = 0.00835   #  worked well at orbit radius 0.5
# tracer_radius_increment = 0.0083   # worked well at orbit radius 0.5
# tracer_radius_increment = 0.0067   # closest to @ so far.
# tracer_radius_increment = 0.0065   # beautiful > @ pattern
# tracer_radius_increment = 0.0063   # beautiful > @ pattern
# tracer_radius_increment = 0.006   # beautiful > @ pattern
# tracer_radius_increment = 0.005   # beautiful > @ pattern
# tracer_radius_increment = 0.004   # beautiful > @ pattern
# tracer_radius_increment = 0.003   # beautiful > @ pattern
# tracer_radius_increment = 0.002   # beautiful > @ pattern
# tracer_radius_increment = 0.001   # beautiful > @ pattern
# tracer_radius_increment = 0.01   # < @ pattern
# tracer_radius_increment = 0.02   # < @ pattern
# tracer_radius_increment = 0.04   # < @ pattern

num_tracer_origins = math.floor(tracer_angle / (angle_increment * frames_between_tracers))

def draw_circle():
    global blue_angle, red_angle, frame, blue_circles, red_circles

    blue_angle_in_radians = blue_angle * pi / 180
    blue_x = cos(blue_angle_in_radians) * orbit_radius
    blue_y = sin(blue_angle_in_radians) * orbit_radius

    red_angle_in_radians = red_angle * pi / 180
    red_x = cos(red_angle_in_radians) * orbit_radius
    red_y = sin(red_angle_in_radians) * orbit_radius


    # the expanding blue tracer circles
    if frame % frames_between_tracers == 0:
        blue_circles.append((blue_x, blue_y, 0))
    fade = 1
    fade_delta = 0.015
    fade_min = 0
    for cx, cy, cr in reversed(blue_circles):
        glLineWidth(2)
        glBegin(GL_LINE_LOOP)
        glColor3f(0, 0, 1.0*fade)
        for i in range(360):
            angle_in_radians = i * pi / 180
            glVertex2f(cx + cr * cos(angle_in_radians), cy + cr * sin(angle_in_radians))
        glEnd()
        fade = max(fade - fade_delta, fade_min)
    blue_circles = [(cx, cy, cr + tracer_radius_increment) for cx, cy, cr in blue_circles if cr < 2]
    
    # the expanding red tracer circles
    if frame %frames_between_tracers == 0:
        red_circles.append((red_x,red_y,0))
    fade = 1
    for cx,cy,cr in reversed(red_circles):
        glLineWidth(2)
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0*fade,0,0)
        for i in range(360):
            angle_in_radians = i * pi / 180
            glVertex2f(cx+cr*cos(angle_in_radians),cy+cr*sin(angle_in_radians))
        glEnd()
        fade = max(fade - fade_delta, fade_min)
    red_circles = [(cx, cy, cr + tracer_radius_increment) for cx, cy, cr in red_circles if cr < 2]
    
    # the recent path of the electrino
    glBegin(GL_LINE_STRIP)
    glColor3f(0.6, 0.6, 0.6)
    for i in range(blue_angle - tracer_angle, blue_angle + 1):
        angle_in_radians = i * pi / 180
        x = cos(angle_in_radians) * orbit_radius
        y = sin(angle_in_radians) * orbit_radius
        glVertex2f(x, y)
    glEnd()

    # the recent path of the positrino
    glBegin(GL_LINE_STRIP)
    glColor3f(0.6, 0.6, 0.6)
    for i in range(red_angle - tracer_angle, red_angle + 1):
        angle_in_radians = i * pi / 180
        x=cos(angle_in_radians)*orbit_radius
        y=sin(angle_in_radians)*orbit_radius
        glVertex2f(x,y)
    glEnd()

    #
    # the electrino point charge representation as a small blue sphere
    #
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.0, 1.0) # blue electrino
    glVertex2f(blue_x, blue_y)
    for i in range(361):
        angle_in_radians = i * pi / 180
        glVertex2f(blue_x + point_charge_representation_radius * cos(angle_in_radians), blue_y + point_charge_representation_radius * sin(angle_in_radians))
    glEnd()

    #
    # the positrino point charge representation as a small red sphere
    #
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 0.0, 0.0) #red
    glVertex2f(red_x,red_y)
    for i in range(361):
        angle_in_radians = i * pi / 180
        glVertex2f(red_x+point_charge_representation_radius*cos(angle_in_radians),red_y+point_charge_representation_radius*sin(angle_in_radians))
    glEnd()

    # Storing electrino tracer origins
    for cx, cy, cr in blue_circles:
        if cr == tracer_radius_increment:
            blue_circle_centers.append((blue_x, blue_y))
            if len(blue_circle_centers) > num_tracer_origins:
                blue_circle_centers.pop(0)

    # Storing positrino tracer origins
    for cx, cy, cr in red_circles:
        if cr == tracer_radius_increment:
            red_circle_centers.append((red_x, red_y))
            if len(red_circle_centers) > num_tracer_origins:
                red_circle_centers.pop(0)

    # Leaving electrino tracer origins on path
    fade = 0
    fade_max = 1
    fade_delta = 2 * fade_max / num_tracer_origins / 3
    for cx, cy in reversed(blue_circle_centers):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(fade, fade, 1.0)
        glVertex2f(cx, cy)
        for i in range(361):
            glVertex2f(cx + tracer_origin_radius * cos(i * pi / 180), cy + tracer_origin_radius * sin(i * pi / 180))
        glEnd()
        fade = min(fade + fade_delta, fade_max)

    # Leaving positrino tracer origins on path
    fade = 0
    for cx, cy in reversed(red_circle_centers):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1.0, fade, fade)
        glVertex2f(cx, cy)
        for i in range(361):
            glVertex2f(cx + tracer_origin_radius * cos(i * pi / 180), cy + tracer_origin_radius * sin(i * pi / 180))
        glEnd()
        fade = min(fade + fade_delta, fade_max)
    
    blue_angle += angle_increment
    red_angle += angle_increment
    frame +=1

pygame.init()
display = pygame.display.list_modes()[0]
pygame.display.set_mode((frame_width, frame_height), DOUBLEBUF|OPENGL)

aspect_ratio = frame_width / frame_height
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(-aspect_ratio, aspect_ratio,-1,1)

clock = pygame.time.Clock()

frames = []
fps = frame_rate

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
        draw_circle()
        pygame.display.flip()
        clock.tick(fps)

        data = glReadPixels(0, 0, frame_width, frame_height, GL_RGB, GL_UNSIGNED_BYTE)
        image = pygame.image.frombuffer(data, (frame_width, frame_height), "RGB")
        # This will make the mp4 run in the reverse direction
        # image = pygame.transform.flip(image, False, True)
        frames.append(pygame.surfarray.array3d(image))

imageio.mimwrite("animation2.mp4", frames, fps=fps)
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
# They also need to be shrinkable from the smallest visible red and blue circles and then incrementing for each step up. Hmm interesting.
# so perhaps a small progression 1,2,4,8,16,32... and then double that.
# Can you make poster size art? That would be cool to make my own posters and print them!

