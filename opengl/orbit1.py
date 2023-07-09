import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import sin, cos, pi

blue_angle = 0
red_angle = 180
frame = 0
blue_circles = []
red_circles = []

def draw_circle():
    global blue_angle, red_angle, frame, blue_circles, red_circles
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.0, 1.0)
    x = cos(blue_angle * pi / 180) * 0.5
    y = sin(blue_angle * pi / 180) * 0.5
    radius = 0.05
    glVertex2f(x, y)
    for i in range(361):
        glVertex2f(x + radius * cos(i * pi / 180), y + radius * sin(i * pi / 180))
    glEnd()
    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)
    for i in range(blue_angle - 160, blue_angle + 1):
        x = cos(i * pi / 180) * 0.5
        y = sin(i * pi / 180) * 0.5
        glVertex2f(x, y)
    glEnd()
    if frame % 12 == 0:
        blue_circles.append((x, y, 0))
    for cx, cy, cr in blue_circles:
        glBegin(GL_LINE_LOOP)
        glColor3f(0.5, 0.5, 1.0)
        for i in range(360):
            glVertex2f(cx + cr * cos(i * pi / 180), cy + cr * sin(i * pi / 180))
        glEnd()
    blue_circles = [(cx, cy, cr + 0.02) for cx, cy, cr in blue_circles if cr < 2]
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 0.0, 0.0)
    x = cos(red_angle * pi / 180) * 0.5
    y = sin(red_angle * pi / 180) * 0.5
    radius = 0.05
    glVertex2f(x,y)
    for i in range(361):
        glVertex2f(x+radius*cos(i*pi/180),y+radius*sin(i*pi/180))
    glEnd()
    
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0,0.0,0.0)
    for i in range(red_angle-160,red_angle+1):
        x=cos(i*pi/180)*0.5
        y=sin(i*pi/180)*0.5
        glVertex2f(x,y)
    glEnd()
    
    if frame %12 ==0:
        red_circles.append((x,y,0))
        
    for cx,cy,cr in red_circles:
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0,0.0,0.0)
        for i in range(360):
            glVertex2f(cx+cr*cos(i*pi/180),cy+cr*sin(i*pi/180))
        glEnd()
        
    red_circles=[(cx,cy,cr+0.02) for cx,cy,cr in red_circles if cr<2]
    
    blue_angle +=1
    red_angle +=1
    frame +=1

pygame.init()
display = pygame.display.list_modes()[0]
pygame.display.set_mode(display, DOUBLEBUF|OPENGL|FULLSCREEN)

aspect_ratio = display[0] / display[1]
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(-aspect_ratio, aspect_ratio,-1 ,1)

clock = pygame.time.Clock()

while True:
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
    clock.tick(30)