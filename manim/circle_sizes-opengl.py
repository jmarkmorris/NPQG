
# todo : port to manim


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import pygame
from pygame.locals import *
import math
import sys
from ctypes import *

paused = 0

def draw_circle(x, y, radius, xoffset):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x + xoffset, y + 0.05)
    for angle in range(0, 361):
        glVertex2f(x + xoffset + radius * math.cos(math.radians(angle)), y + 0.05 + radius * math.sin(math.radians(angle)))
    glEnd()

def draw_grid():
    glColor3f(0, 0, 0)
    glColor3f(1, 1, 1) # Set color to white
    glBegin(GL_LINES)
    for i in range(11):
        glVertex2f(i/10, 0)
        glVertex2f(i/10, 1)
        glVertex2f(0, i/10)
        glVertex2f(1, i/10)
    glEnd()

def draw_labels():
    font = GLUT_BITMAP_TIMES_ROMAN_24


    glColor3f(1, 1, 1) # Set color to white
    for y in range(10):
        for x in range(10):
            value_label = "r = {:.4f}".format((y*10+x+1)*0.0002)
            label_width = glutBitmapLength(font, (c_ubyte * len(value_label))(*value_label.encode('utf-8')))
            glRasterPos2f(x/10 + 0.05 - label_width/2/1200, y/10 + 0.025)
            for char in value_label:
                glutBitmapCharacter(font, ord(char))
            # coord_label = "x:{} y:{}".format(x, y)
            # label_width = glutBitmapLength(font, (c_ubyte * len(coord_label))(*coord_label.encode('utf-8')))
            # glRasterPos2f(x/10 + 0.05 - label_width/2/1200, y/10 + 0.085)
            # for char in coord_label:
            #     glutBitmapCharacter(font, ord(char))



pygame.init()
glutInit()
screen = pygame.display.set_mode((1200, 1200), OPENGL | DOUBLEBUF)
gluOrtho2D(0, 1, 1, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == K_SPACE:
                paused = not paused

    if not paused:
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)

        draw_grid()
        draw_labels()

        radius = 0.0002
        for y in range(10):
            for x in range(10):
                glColor3f(0, 0, 1)
                draw_circle(x/10, y/10, radius, 0.025)
                glColor3f(1, 0, 0)
                draw_circle(x/10, y/10, radius, 0.075)
                radius += 0.0002

        pygame.display.flip()

# When done with the static version ask Bai to animate it with orbital radius 0.25 from the center of each square.