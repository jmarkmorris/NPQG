# manim -pqh emergence.py emergence -p
# add argument handling
# manim -pqh emergence.py emergence -p --arg 1 2 3.14 4.56
# argv[1] : blah [default = x]
# argv[2] : 
# argv[3] : 
# argv[4] : 
#
from manim import *
import random
import itertools
from colour import Color
import math

config.frame_rate = 60

class ColoredDot(Dot):
    # def __init__(self, color, coordinates, **kwargs):
    def __init__(self, color, coordinates, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.coordinates = coordinates

class Bzzzt(Line):
    def __init__(self, start, end, **kwargs):
        super().__init__(start, end, color=Color("#8F00FF"), stroke_width=10, **kwargs)

def get_next_coordinates(graph, velocities, vertex_key, dt):
    current_coordinates = graph.vertices[vertex_key].get_center()
    displacement = np.array([0.0, 0.0, 0.0])
    for other_vertex_key in graph.vertices:
        if other_vertex_key == vertex_key:
            continue  #  the > @ could go here in the ultimate simulation.
        other_vertex_coordinates = graph.vertices[other_vertex_key].get_center()
        direction = other_vertex_coordinates - current_coordinates
        direction = direction / np.linalg.norm(direction)
        distance = np.linalg.norm(other_vertex_coordinates - current_coordinates)

        velocity = velocities[vertex_key]
        
        dsquare = max(0.6, distance * distance) # temporary shim to prevent velocity from blowing up
        if dt > 0:
            if graph.vertices[vertex_key].color == graph.vertices[other_vertex_key].color:
                new_velocity = 0.99 * velocity - 0.003 * direction / (dsquare * dt)
                displacement += new_velocity * dt
            else:
                new_velocity = 0.99 * velocity + 0.003 * direction / (dsquare * dt)
                displacement += new_velocity * dt
            velocities[vertex_key] = new_velocity

    next_coordinates = current_coordinates + displacement
    # Keep the vertex on the edge if it bumps there, and add a touch line indicator.
    if next_coordinates[0] <= -7 or next_coordinates[0] >= 7:
        touch_line_start = next_coordinates - np.array([0, 0.1, 0])
        touch_line_end = next_coordinates + np.array([0, 0.1, 0])
        touch_line = Line(touch_line_start, touch_line_end)
        graph.add(touch_line)

    if next_coordinates[1] <= -4 or next_coordinates[1] >= 4:
        touch_line_start = next_coordinates - np.array([0.1, 0, 0])
        touch_line_end = next_coordinates + np.array([0.1, 0, 0])
        touch_line = Bzzzt(touch_line_start, touch_line_end)
        graph.add(touch_line)
    # this could go above
    next_coordinates[0] = max(-7, min(next_coordinates[0], 7))
    next_coordinates[1] = max(-4, min(next_coordinates[1], 4))
    next_coordinates[2] = 0


    return next_coordinates

class emergence(Scene):
    def construct(self):
        
        # Get the command line arguments
        int_arg1 = int(sys.argv[1])
        int_arg2 = int(sys.argv[2])
        float_arg1 = float(sys.argv[3])
        float_arg2 = float(sys.argv[4])

        colors = [PURE_RED, PURE_BLUE]
        # x_range = (-3, 3)
        # y_range = (-3, 3)
        x_range = (-2, 2)
        y_range = (-1, 1)

        # num_vertices = 24
        # num_vertices = 12  # add the ingredients for a fermion and see what happens
        num_vertices = 12 
        vertices = {f'v{i}': ColoredDot(colors[i % 2], [random.uniform(*x_range), random.uniform(*y_range), 0]) for i in range(num_vertices)}
        vertex_config = {v: {'color': vertices[v].color, 
                             'stroke_width': 1, 
                             'fill_opacity': 1, 
                             'radius': 0.06} for v in vertices}
        layout = {}
        layout = {v: vertices[v].coordinates for v in vertices}
        
        VelocityMultiplier = math.pow(10, 0) # the animation fails if velocity is too high. Not sure why. Possible bug.
        velocities = {f'v{i}': np.array([(random.choice([-1, 1]) * random.uniform(.1, .2) * VelocityMultiplier) if j != 2 else 0 for j in range(3)]) for i in range(num_vertices)}

        edges = list(itertools.combinations(vertices.keys(), 2))
        edge_config = {
            edge: {
                'color': vertices[edge[0]].color if vertices[edge[0]].color == vertices[edge[1]].color 
                        else Color("#8F00FF"),   # Electric Purple!
                'stroke_width': 1 #1.5 is good if focused on relationships, but overpowers the vertices.
            } for edge in edges
        }

        G = Graph(vertices.keys(), 
                  edges, 
                  layout=layout, 
                  vertex_config=vertex_config, 
                  edge_config=edge_config)
        
        rect = Rectangle(
            color=WHITE,
            fill_opacity=0,
            stroke_width=4,
            height=8,
            width=14
        )
        
        self.add(rect)
        
        self.play(Create(G))
        
        def update_vertices(mob, dt):
            
            # Calculate the next positions of all vertices
            next_positions = {}
            for vertex in mob.vertices:
                next_positions[vertex] = get_next_coordinates(mob, velocities, vertex, dt)

            # Move all vertices to their next positions
            for vertex in mob.vertices:
                mob.vertices[vertex].move_to(next_positions[vertex])

        G.add_updater(update_vertices)
        self.wait(60)
