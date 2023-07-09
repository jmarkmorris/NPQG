import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import sin, cos, pi
import imageio

blue_angle = 0
red_angle = 180
frame = 0
blue_circles = []
red_circles = []
# these lists to keep track of the starting points of the expanding circles
blue_circle_centers = []
red_circle_centers = []

# tunables
orbit_radius = 0.5
point_charge_representation_radius = 0.03
angle_increment = 3
frames_between_tracers = 6
num_tracer_origins = 6
tracer_radius_increment = 0.001

def draw_circle():
    global blue_angle, red_angle, frame, blue_circles, red_circles
    
    #
    # the electrino point charge representation as a small blue sphere
    #
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.0, 1.0) # blue electrino
    angle_in_radians = blue_angle * pi / 180
    x = cos(angle_in_radians) * orbit_radius
    y = sin(angle_in_radians) * orbit_radius
    radius = point_charge_representation_radius
    glVertex2f(x, y)
    for i in range(361):
        angle_in_radians = i * pi / 180
        glVertex2f(x + radius * cos(angle_in_radians), y + radius * sin(angle_in_radians))
    glEnd()

    # the recent path
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    for i in range(blue_angle - 120, blue_angle - 1):
        angle_in_radians = i * pi / 180
        x = cos(angle_in_radians) * orbit_radius
        y = sin(angle_in_radians) * orbit_radius
        glVertex2f(x, y)
    glEnd()

    # the expanding blue tracer circles
    # seems like the code could be made less redundant?
    angle_in_radians = blue_angle * pi / 180
    x = cos(angle_in_radians) * orbit_radius
    y = sin(angle_in_radians) * orbit_radius
    if frame % frames_between_tracers == 0:
        blue_circles.append((x, y, 0))
    for cx, cy, cr in blue_circles:
        glBegin(GL_LINE_LOOP)
        glColor3f(0.5, 0.5, 1.0)
        for i in range(360):
            angle_in_radians = i * pi / 180
            glVertex2f(cx + cr * cos(angle_in_radians), cy + cr * sin(angle_in_radians))
        glEnd()
    blue_circles = [(cx, cy, cr + tracer_radius_increment) for cx, cy, cr in blue_circles if cr < 2]

    # Storing tracer origins
    for cx, cy, cr in blue_circles:
        if cr == tracer_radius_increment:
            blue_circle_centers.append((x, y))
            if len(blue_circle_centers) > num_tracer_origins:
                blue_circle_centers.pop(0)

    # Leaving tracer origins on path
    for cx, cy in blue_circle_centers:
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.5, 0.5, 1.0)
        radius = 0.01
        glVertex2f(cx, cy)
        for i in range(361):
            glVertex2f(cx + radius * cos(i * pi / 180), cy + radius * sin(i * pi / 180))
        glEnd()


    #
    # the positrino point charge representation as a small red sphere
    #
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 0.0, 0.0) #red
    angle_in_radians = red_angle * pi / 180
    x = cos(angle_in_radians) * orbit_radius
    y = sin(angle_in_radians) * orbit_radius

    radius = point_charge_representation_radius
    glVertex2f(x,y)
    for i in range(361):
        angle_in_radians = i * pi / 180
        glVertex2f(x+radius*cos(angle_in_radians),y+radius*sin(angle_in_radians))
    glEnd()
    
    # the recent path
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    for i in range(red_angle-120,red_angle + 1):
        angle_in_radians = i * pi / 180
        x=cos(angle_in_radians)*orbit_radius
        y=sin(angle_in_radians)*orbit_radius
        glVertex2f(x,y)
    glEnd()
    
    # the expanding red tracer circles
    angle_in_radians = red_angle * pi / 180
    x = cos(angle_in_radians) * orbit_radius
    y = sin(angle_in_radians) * orbit_radius
    if frame %frames_between_tracers == 0:
        red_circles.append((x,y,0))
        
    for cx,cy,cr in red_circles:
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0,0.0,0.0)
        for i in range(360):
            angle_in_radians = i * pi / 180
            glVertex2f(cx+cr*cos(angle_in_radians),cy+cr*sin(angle_in_radians))
        glEnd()
        
    red_circles=[(cx,cy,cr+tracer_radius_increment) for cx,cy,cr in red_circles if cr<2]

    # Storing tracer origins
    for cx, cy, cr in red_circles:
        if cr == tracer_radius_increment:
            red_circle_centers.append((x, y))
            if len(red_circle_centers) > num_tracer_origins:
                red_circle_centers.pop(0)

     # Leaving tracer origins on path
    for cx, cy in red_circle_centers:
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1.0, 0.5, 0.5)
        radius = 0.01
        glVertex2f(cx, cy)
        for i in range(361):
            glVertex2f(cx + radius * cos(i * pi / 180), cy + radius * sin(i * pi / 180))
        glEnd()
    
    blue_angle += angle_increment
    red_angle += angle_increment
    frame +=1

pygame.init()
display = pygame.display.list_modes()[0]
pygame.display.set_mode(display, DOUBLEBUF|OPENGL|FULLSCREEN)

aspect_ratio = display[0] / display[1]
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(-aspect_ratio, aspect_ratio,-1 ,1)

clock = pygame.time.Clock()

frames = []
duration = 20
fps = 60

while frame < duration * fps:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                quit()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    draw_circle()
    pygame.display.flip()
    clock.tick(fps)
    
    data = glReadPixels(0, 0, display[0], display[1], GL_RGB, GL_UNSIGNED_BYTE)
    image = pygame.image.frombuffer(data, (display[0], display[1]), "RGB")
    image = pygame.transform.flip(image, False, True)
    frames.append(pygame.surfarray.array3d(image))

imageio.mimwrite("animation2.mp4", frames, fps=fps)
pygame.quit()