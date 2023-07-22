# To Do
# add the two point charge scenario starting from various points around the edge of a box and at various velocities. Do controlled experiments. Multiple boxes on the screen.
# manim -pql graph.py GraphExample -p
# manim -pqh graph.py GraphExample -p
#
from manim import *
import random
import itertools

class ColoredDot(Dot):
    # def __init__(self, color, coordinates, velocity, **kwargs):
    def __init__(self, color, coordinates, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.coordinates = coordinates
        # self.velocity = velocity

def get_next_coordinates(graph, velocities, vertex_key, dt):
    current_coordinates = graph.vertices[vertex_key].get_center()
    displacement = np.array([0.0, 0.0, 0.0])
    for other_vertex_key in graph.vertices:
        if other_vertex_key == vertex_key:
            continue
        other_vertex_coordinates = graph.vertices[other_vertex_key].get_center()
        direction = other_vertex_coordinates - current_coordinates
        direction = direction / np.linalg.norm(direction)
        distance = np.linalg.norm(other_vertex_coordinates - current_coordinates)

        velocity = velocities[vertex_key]
        
        dsquare = max(0.6, distance * distance) # temporary shim to prevent velocity from blowing up
        if dt > 0:
            if graph.vertices[vertex_key].color == graph.vertices[other_vertex_key].color:
                # print(f"velocity = {velocity}, velocity delta = {0.000001 * direction / dt}")
                new_velocity = 0.99 * velocity - 0.003 * direction / (dsquare * dt)
                displacement += new_velocity * dt
            else:
                new_velocity = 0.99 * velocity + 0.003 * direction / (dsquare * dt)
                displacement += new_velocity * dt
            velocities[vertex_key] = new_velocity

    next_coordinates = current_coordinates + displacement
    # if (next_coordinates[0] < -8):
    #     next_coordinates[0] += 16
    # elif (next_coordinates[0] > 8):
    #     next_coordinates[0] -= 16

    # if (next_coordinates[1] < -5):
    #     next_coordinates[1] += 10
    # elif (next_coordinates[1] > 5):
    #     next_coordinates[1] -= 10
    if (next_coordinates[0] < -7):
        next_coordinates[0] += 14
    elif (next_coordinates[0] > 7):
        next_coordinates[0] -= 14

    if (next_coordinates[1] < -4):
        next_coordinates[1] += 8
    elif (next_coordinates[1] > 4):
        next_coordinates[1] -= 8

    next_coordinates[2] = 0

    return next_coordinates

class GraphExample(Scene):
    def construct(self):
        colors = [PURE_RED, PURE_BLUE]
        # vertices = {}
        # x_range = (-3, 3)
        # y_range = (-3, 3)
        x_range = (-2, 2)
        y_range = (-1, 1)

        # 2 is boring - straighe line case
        # 3 is interesting. A dipole orbit and the third charge weakly captured at a distance. Hmmm. LOL. Another case A B A oscillating transversely.
        # 4 is fascinating. Two dipoles with entangled orbits. Seems to be two ways to do this that I've seen so far.
        # 5 is funky and wild. Lots of variation, semi stability, and decay.
        # 6 often reaches a stable state, but have seen it destabilize.
        # 7 odd charge eventually causes stability decay
        # 24 is pretty good. 
        # 32 too many.
        num_vertices = 12
        vertices = {f'v{i}': ColoredDot(colors[i % 2], [random.uniform(*x_range), random.uniform(*y_range), 0]) for i in range(num_vertices)}
        velocities = {f'v{i}': np.array([random.uniform(0.0001, 0.0002) for _ in range(3)]) for i in range(num_vertices)}
        for v in velocities.values():
            v[2] = 0

        edges = list(itertools.combinations(vertices.keys(), 2))
        
        edge_config = {
            edge: {
                'color': vertices[edge[0]].color if vertices[edge[0]].color == vertices[edge[1]].color 
                        else interpolate_color(vertices[edge[0]].color, vertices[edge[1]].color, 0.5),
                'stroke_width': 1
            } for edge in edges
        }

        # vertex_config = {v: {'color': vertices[v].color, 'stroke_width': 1, 'fill_opacity': 1, 'radius': 0.04} for v in vertices}
        vertex_config = {v: {'color': vertices[v].color, 'stroke_width': 1, 'fill_opacity': 1, 'radius': 0.06} for v in vertices}

        layout = {}
        for v in vertices:
            layout[v] = vertices[v].coordinates
        
        G = Graph(vertices.keys(), edges, layout=layout, vertex_config=vertex_config, edge_config=edge_config)
        self.play(Create(G))
        
        def update_vertices(mob, dt):
            
            # Calculate the next positions of all vertices
            next_positions = {}
            scale = 1.0
            for vertex in mob.vertices:
                next_positions[vertex] = get_next_coordinates(mob, velocities, vertex, dt)

            # Move all vertices to their next positions
            for vertex in mob.vertices:
                mob.vertices[vertex].move_to(next_positions[vertex])

        G.add_updater(update_vertices)
        self.wait(30)
