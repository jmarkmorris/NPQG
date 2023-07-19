

# A Python program that uses PyOpenGL to create a 3D scene with multiple spheres positioned around a volume. 
# The background is set to black and the x, y, and z axes are shown in light grey. 
# Some of the spheres are red and some are blue. 
# A 3D control interface allows the user to fly around and view the arrangement of spheres from any position and with any angle or zoom level.

# **Implementation Guide:**

# 1. Install the required libraries: PyOpenGL, NumPy, and GLUT. You can do this by running `pip install PyOpenGL numpy PyOpenGL-accelerate`.
# 2. Copy the complete Python code into a new file and save it with a `.py` extension.
# 3. Run the program by navigating to the directory where you saved the file and running `python <filename>.py` in your command prompt or terminal.

# **User Guide:**

# 1. Once the program is running, you will see a window displaying a 3D scene with multiple spheres positioned around a volume.
# 2. You can use the `W`, `A`, `S`, `D`, `Q`, and `Z` keys to move the camera forward, left, backward, right, up, and down, respectively.
# 3. You can use the `I`, `J`, `K`, and `L` keys to rotate the camera up, left, down, and right, respectively.
# 4. You can use the `+` and `-` keys to zoom in and out, respectively.
# 5. You can also use the left mouse button to rotate the camera by clicking and dragging the mouse.
# 6. You can use the right mouse button to zoom in and out by clicking and dragging the mouse up or down.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy as np

# Set the width and height of the window
width, height = 800, 600

# Set the number of spheres
num_spheres = 10

# Set the sphere radius
sphere_radius = 0.5

# Set the sphere positions
sphere_positions = np.random.rand(num_spheres, 3) * 10 - 5

# Set the sphere colors
sphere_colors = np.zeros((num_spheres, 3))
sphere_colors[:num_spheres//2] = [1, 0, 0]
sphere_colors[num_spheres//2:] = [0, 0, 1]

# Set the camera position
camera_position = np.array([0, 0, 10])

# Set the camera rotation
camera_rotation = np.array([0, 0, 0])

# Set the camera zoom
camera_zoom = 1

def display():
   # Clear the color and depth buffers
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

   # Reset the modelview matrix
   glLoadIdentity()

   # Apply the camera zoom
   glScalef(camera_zoom, camera_zoom, camera_zoom)

   # Apply the camera rotation
   glRotatef(camera_rotation[0], 1, 0, 0)
   glRotatef(camera_rotation[1], 0, 1, 0)
   glRotatef(camera_rotation[2], 0, 0, 1)

   # Apply the camera translation
   glTranslatef(-camera_position[0], -camera_position[1], -camera_position[2])

   # Draw the x axis
   glColor3f(0.5, 0.5, 0.5)
   glBegin(GL_LINES)
   glVertex3f(-100, 0, 0)
   glVertex3f(100, 0, 0)
   glEnd()

   # Draw the y axis
   glColor3f(0.5, 0.5, 0.5)
   glBegin(GL_LINES)
   glVertex3f(0, -100, 0)
   glVertex3f(0, 100, 0)
   glEnd()

   # Draw the z axis
   glColor3f(0.5, 0.5, 0.5)
   glBegin(GL_LINES)
   glVertex3f(0, 0, -100)
   glVertex3f(0, 0, 100)
   glEnd()

   # Draw the spheres
   for i in range(num_spheres):
       glPushMatrix()
       glColor3f(*sphere_colors[i])
       glTranslatef(*sphere_positions[i])
       glutSolidSphere(sphere_radius, 20, 20)
       glPopMatrix()

   # Swap the front and back buffers
   glutSwapBuffers()

   # Refresh the display
   glutPostRedisplay()

def reshape(w, h):
   global width, height
   width, height = w, h
   glViewport(0, 0, width, height)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   gluPerspective(45.0, float(width) / float(height), 1.0, 100.0)
   glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global camera_position, camera_rotation, camera_zoom

    # Cast camera_position to float
    camera_position = camera_position.astype(float)

    # Move the camera forward
    if key == b'w':
        camera_position -= np.array([np.sin(np.radians(camera_rotation[1])), 0, np.cos(np.radians(camera_rotation[1]))])
    # Move the camera backward
    elif key == b's':
        camera_position += np.array([np.sin(np.radians(camera_rotation[1])), 0, np.cos(np.radians(camera_rotation[1]))])
    # Move the camera left
    elif key == b'a':
        camera_position -= np.array([np.sin(np.radians(camera_rotation[1] + 90)), 0, np.cos(np.radians(camera_rotation[1] + 90))])
    # Move the camera right
    elif key == b'd':
        camera_position += np.array([np.sin(np.radians(camera_rotation[1] + 90)), 0, np.cos(np.radians(camera_rotation[1] + 90))])
    # Move the camera up
    elif key == b'q':
        camera_position[1] += 1
    # Move the camera down
    elif key == b'z':
        camera_position[1] -= 1
    # Rotate the camera left
    elif key == b'j':
        camera_rotation[1] += 5
    # Rotate the camera right
    elif key == b'l':
        camera_rotation[1] -= 5
    # Rotate the camera up
    elif key == b'i':
        camera_rotation[0] += 5
    # Rotate the camera down
    elif key == b'k':
        camera_rotation[0] -= 5
    # Zoom in
    elif key == b'+':
        camera_zoom *= 1.1
    # Zoom out
    elif key == b'-':
        camera_zoom /= 1.1


def mouse(button, state, x, y):
   global mouse_button, mouse_x, mouse_y
   if state == GLUT_DOWN:
       mouse_button = button
       mouse_x = x
       mouse_y = y

def motion(x, y):
   global mouse_button, mouse_x, mouse_y, camera_rotation

   # Rotate the camera with the left mouse button
   if mouse_button == GLUT_LEFT_BUTTON:
       camera_rotation[0] += y - mouse_y
       camera_rotation[1] += x - mouse_x

   # Zoom the camera with the right mouse button
   elif mouse_button == GLUT_RIGHT_BUTTON:
       camera_zoom *= 1.0 + (y - mouse_y) * 0.01

   mouse_x = x
   mouse_y = y


# Initialize GLUT
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutCreateWindow(b'OpenGL Spheres')

# Set the clear color to black
glClearColor(0, 0, 0, 0)

# Enable depth testing
glEnable(GL_DEPTH_TEST)

# Set the display callback function
glutDisplayFunc(display)

# Set the reshape callback function
glutReshapeFunc(reshape)

# Set the keyboard callback function
glutKeyboardFunc(keyboard)

# Set the mouse callback function
glutMouseFunc(mouse)

# Set the motion callback function
glutMotionFunc(motion)

# Enter the main loop
glutMainLoop()