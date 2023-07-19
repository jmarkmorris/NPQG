from OpenGL.GL import *
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((1,1), pygame.OPENGL | pygame.DOUBLEBUF)

max_size = glGetIntegerv(GL_MAX_TEXTURE_SIZE)
print(f"Maximum texture size: {max_size}x{max_size}")
