from manim import *
import random
import itertools

class ColoredDot(Dot):
    def __init__(self, color, coordinates, velocity, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.coordinates = coordinates
        self.velocity = velocity

def get_next_coordinates(graph, vertex_key):
    current_coordinates = graph.vertices[vertex_key].get_center()
    displacement = np.array([0.0, 0.0, 0.0])
    for other_vertex_key in graph.vertices:
        if other_vertex_key == vertex_key:
            continue
        other_vertex_coordinates = graph.vertices[other_vertex_key].get_center()
        direction = other_vertex_coordinates - current_coordinates
        direction = direction / np.linalg.norm(direction)
        distance = np.linalg.norm(other_vertex_coordinates - current_coordinates)
        if graph.vertices[vertex_key].color == graph.vertices[other_vertex_key].color:
            displacement -= 0.001 * direction / distance
        else:
            displacement += 0.001 * direction / distance

    next_coordinates = current_coordinates + displacement
    return next_coordinates

class GraphExample(Scene):
    def construct(self):
        colors = [PURE_RED, PURE_BLUE]
        vertices = {}
        x_range = (-6, 6)
        y_range = (-3, 3)

        vertices = {f'v{i}': ColoredDot(colors[i % 2], [random.uniform(*x_range), random.uniform(*y_range), 0], **np.random.rand(3))** for i in range(20)}

        edges = list(itertools.combinations(vertices.keys(), 2))
        edge_config = {edge: {'color': vertices[edge[0]].color if vertices[edge[0]].color == vertices[edge[1]].color else interpolate_color(vertices[edge[0]].color, vertices[edge[1]].color, 0.5), 'stroke_width': 1} for edge in edges}
        
        vertex_config = {v: {'color': vertices[v].color} for v in vertices}

        layout = {}
        for v in vertices:
            layout[v] = vertices[v].coordinates
        
        G = Graph(vertices.keys(), edges, layout=layout, vertex_config=vertex_config, edge_config=edge_config)
        self.play(Create(G))
        
        

        def update_vertices(mob, dt):
            for vertex in mob.vertices:
                next_coordinates = mob.vertices[vertex].get_center() + mob.vertices[vertex].velocity[:3] * dt
                mob.vertices[vertex].move_to(next_coordinates)
        
        G.add_updater(update_vertices)
        self.wait(5)
