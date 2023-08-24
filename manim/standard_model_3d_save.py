# manim -pqh --disable_caching standard_model_3d.py standard_model_3d -p

# this is an example of multiple concurrent assemblies each defined by a dictionary.

# this code is sort of bulky. Possibly some cleverness related to the canonical model could make this code better.

from manim import *
import random
from numpy import array

run_time = 10
# run_time = 16
frame_rate = 3
# frame_rate = 60
# paused = False # add pause feature?


# powerpoint png export size
config.pixel_width = 2998
config.pixel_height = 1686
config.frame_rate = frame_rate

radius_I = 0.1
radius_II = 0.2
radius_III = 0.3
radius_IV = 0.1
charge_radius = 0.05
personality_offset = .5

class standard_model_3d(ThreeDScene):
    def construct(self):
        # In Manim, phi and theta are parameters that define the orientation of the camera in a 3D scene. 
        # phi is the polar angle, which is the angle between the Z-axis and the camera through the origin, measured in radians
        # theta is the azimuthal angle, which is the angle that spins the camera around the Z-axis.

        # in this animation, z is coming out of the screen. x is the assembly type, and y is the generation.
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.camera.background_color = BLACK        

        text = Paragraph(
                    ' Title : Standard Model Fermion Architecture Hypothesis, '
                    ' Author : J Mark Morris.'
                    ' Mapping : Standard model generation + Noether core dipole count = 4.\n'
                    ' Mapping : Color charge may correspond to the three geometries for each quark. '
                    ' Mapping : Electron and neutrino have no color charge due to symmetry.\n'
                    ' Mapping : High energy reactions can cause decay of outer Noether core dipoles.'
                    ' Mapping : Outer dipole decay reveals mass-energy previously shielded by superposition.\n'
                    ' Mapping : Quark orbital planes orientations logically match Weinberg angle (~tau/12).'
                    ' Note : Other charge distribution geometries for quarks and neutrinos seem counterintuitive.\n'
                    ' Mapping : Orbital poles of Noether core dipoles precess with spin "1/2" (i.e., f/2). (not shown)'
                    ' Insight : The architecture is a nested nucleus model, consistent with reductionism.\n'
                    ' Note : Consider each level of the architecture to be separated by orders of magnitude in radial distance. '
                    ' Note : Animations are abstract. The diagrams are not to scale. Radii of orbits TBD.\n',
                    font="Helvetica Neue", 
                    font_size=20, 
                    weight=ULTRALIGHT, 
                    line_spacing=0.5)
        text.scale(0.5)
        text.to_corner(UL)
        text.shift(LEFT*0.25 + UP*0.25)
        self.add_fixed_in_frame_mobjects(text)

        starting_x = -6.0
        x_increment = 1.7
        y_decrement = 2.25
        dictionary_of_assemblies = []
        for x in range(8):  
            starting_y = 1.5
            for y in range(3):
                assembly = {
                    'position': (starting_x, starting_y, 0),
                }
                dictionary_of_assemblies.append(assembly)
                
                starting_y -= y_decrement
            starting_x += x_increment

        assembly_labels = ["Electron", "Muon", "Tau", 
                           "Down A","Strange A","Bottom A", 
                           "Down B","Strange B","Bottom B", 
                           "Down C","Strange C","Bottom C", 
                           "Electron Neutrino", "Muon Neutrino", "Tau Neutrino", 
                           "Up A","Charm A","Top A", 
                           "Up B","Charm B","Top B", 
                           "Up C","Charm C","Top C",
                           ]
        
        # Best practice for initializing repetitive dictionary items
        for i, A in enumerate(dictionary_of_assemblies):
            A['font'] = "Helvetica Neue"
            A['font_size'] = 12
            A['weight'] = MEDIUM
            A['color'] = WHITE
            A['text']  = assembly_labels[i]
   
        charges_in_the_noether_core = [
            {
                'center': (radius_I,0,0),
                'color': PURE_RED,
                'dot_radius': charge_radius,
                'orbit_radius': radius_I,
                'orbit_cycles': 256,
                'orbit_rotate': 0,
                'path_rotate':[0, 0, 1],
                'orbit_normal':[0, 0, 1]
            },
            {
                'center': (-radius_I,0,0),
                'color': PURE_BLUE,
                'dot_radius': charge_radius,
                'orbit_radius': radius_I,
                'orbit_cycles': 256,
                'orbit_rotate': 0,
                'path_rotate':[0, 0, 1],
                'orbit_normal':[0, 0, 1]
            },
            {
                'center': (0,radius_II,0),
                'color': PURE_RED,
                'dot_radius': charge_radius,
                'orbit_radius': radius_II,
                'orbit_cycles': 128,
                'orbit_rotate': PI/2,
                'path_rotate':[0, 1, 0],
                'orbit_normal':[1, 0, 0]
            },
            {
                'center': (0,-radius_II,0),
                'color': PURE_BLUE,
                'dot_radius': charge_radius,
                'orbit_radius': radius_II,
                'orbit_cycles': 128,
                'orbit_rotate': PI/2,
                'path_rotate':[0, 1, 0],
                'orbit_normal':[1, 0, 0]
            },
            {
                'center': (0,0,radius_III),
                'color': PURE_RED,
                'dot_radius': charge_radius,
                'orbit_radius': radius_III,
                'orbit_cycles': 64,
                'orbit_rotate': PI/2,
                'path_rotate':[1, 0, 0],
                'orbit_normal':[0, 1, 0]
            },
            {
                'center': (0,0,-radius_III),
                'color': PURE_BLUE,
                'dot_radius': charge_radius,
                'orbit_radius': radius_III,
                'orbit_cycles': 64,
                'orbit_rotate': PI/2,
                'path_rotate':[1, 0, 0],
                'orbit_normal':[0, 1, 0]
            }
        ]

        personality_charges = [
            {
                'center': (personality_offset, radius_IV, 0),
                'dot_radius': charge_radius,
                'orbit_origin': (personality_offset, 0, 0),
                'orbit_normal': [1, 0, 0]
            },
            {
                'center': (-personality_offset, radius_IV, 0),
                'dot_radius': charge_radius,
                'orbit_origin': (personality_offset, 0, 0),
                'orbit_normal': [1, 0, 0]
            },
            {
                'center': (0, personality_offset, radius_IV),
                'dot_radius': charge_radius,
                'orbit_origin': (0, personality_offset, 0),
                'orbit_normal': [0, 1, 0]
            },
            {
                'center': (0, -personality_offset, radius_IV),
                'dot_radius': charge_radius,
                'orbit_origin': (0, personality_offset, 0),
                'orbit_normal': [0, 1, 0]
            },
            {
                'center': (radius_IV, 0, personality_offset),
                'dot_radius': charge_radius,
                'orbit_origin': (0, 0, personality_offset),
                'orbit_normal': [0, 0, 1]
            },
            {
                'center': (radius_IV, 0, -personality_offset),
                'dot_radius': charge_radius,
                'orbit_origin': (0, 0, personality_offset),
                'orbit_normal': [0, 0, 1]
            }
        ]


        assemblies = []
        for i, A in enumerate(dictionary_of_assemblies):
            
            '''
            set up the text label for each assembly.
            '''
            T = Text(
                A['text'],
                font=A['font'],
                font_size=A['font_size'],
                weight=A['weight'],
                color=A['color']
            ).move_to(A['position']+array([0,1,0]))
            self.add(T)
            # self.add_fixed_in_frame_mobjects(T)

            '''
            set up the 3D coordinate axes for each assembly.
            '''
            kwargs = {
                'x_range': [-5,5,1],
                'y_range': [-5,5,1],
                'z_range': [-5,5,1],
                'x_length': 1.5,
                'y_length': 1.5,
                'z_length': 1.5,
                'tips': False,
                'axis_config': {
                    'stroke_width':1,
                    'include_ticks': False,
                },
            }
            axes = ThreeDAxes(**kwargs)
            # x_axis_label = axes.get_x_axis_label(label="")
            # self.add(x_axis_label)
            # y_axis_label = axes.get_y_axis_label(label="")
            # self.add(y_axis_label)
            # z_axis_label = axes.get_z_axis_label(label="")
            # # z_axis_label.rotate(PI)
            # self.add(z_axis_label)
            axes.move_to(A['position'])
            self.add(axes)

            '''
            animate the noether core.
            '''
            for c, charge in enumerate(charges_in_the_noether_core):
                assembly = A['text']
                if assembly == "Electron" or assembly == "Down A" or assembly == "Down B" or assembly == "Down C" or assembly == "Electron Neutrino" or assembly == "Up A" or assembly == "Up B" or assembly == "Up C":
                    generation = 3
                elif assembly == "Muon" or assembly == "Strange A" or assembly == "Strange B" or assembly == "Strange C" or assembly == "Muon Neutrino" or assembly == "Charm A" or assembly == "Charm B" or assembly == "Charm C":
                    generation = 2
                elif assembly == "Tau" or assembly == "Bottom A" or assembly == "Bottom B" or assembly == "Bottom C" or assembly == "Tau Neutrino" or assembly == "Top A" or assembly == "Top B" or assembly == "Top C":
                    generation = 1
                
                # print(f"before if -- generation : {generation}, c : {c}")
                if (c == 2 or c == 3) and generation == 1:
                    continue
                elif (c == 4 or c == 5) and (generation == 1 or generation == 2):
                    continue
                # print(f"after if -- generation : {generation}, c : {c}")

                kwargs = {
                    'radius':charge['orbit_radius'],
                    'color':WHITE,
                    'stroke_opacity':0.5,
                    'stroke_width':1,
                    'fill_opacity':0.0,
                }
                orbital_path = Circle(**kwargs)
                orbital_path.move_to(A['position'])
                orbital_path.rotate(angle=charge['orbit_rotate'], axis=charge['path_rotate'])
                self.add(orbital_path)

                kwargs = {
                    'point':charge['center'], 
                    'radius':charge['dot_radius'], 
                    'color':charge['color'],
                }
                sphere = Dot3D(**kwargs)
                sphere.shift(A['position'])
                # self.add_foreground_mobject(sphere)  # didn't work
                self.add(sphere)

                assemblies.append(Rotating(sphere, radians=TAU*charge['orbit_cycles'], axis=charge['orbit_normal'], about_point=array(ORIGIN)+array(A['position']), rate_func=linear, run_time=run_time))
            

            '''
            animate the personality charges.
            '''
            assembly = A['text']
            for p, personality in enumerate(personality_charges):
                color = PURE_BLUE #start every charge at blue here and change selected ones to red
                if assembly == "Electron" or assembly == "Muon" or assembly == "Tau":
                    color = PURE_BLUE
                elif assembly == "Down A" or assembly == "Strange A" or assembly == "Bottom A":
                    if p == 3 or p == 5:
                        color = PURE_RED
                elif assembly == "Down B" or assembly == "Strange B" or assembly == "Bottom B":
                    if p == 1 or p == 5:
                        color = PURE_RED
                elif assembly == "Down C" or assembly == "Strange C" or assembly == "Bottom C":
                    if p == 1 or p == 3:
                        color = PURE_RED
                elif assembly == "Electron Neutrino" or assembly == "Muon Neutrino" or assembly == "Tau Neutrino":
                    if p == 1 or p == 3 or p == 5:
                        color = PURE_RED
                elif assembly == "Up A" or assembly == "Charm A" or assembly == "Top A":
                    if p == 1 or p == 2  or p == 3  or p == 4  or p == 5:
                        color = PURE_RED
                elif assembly == "Up B" or assembly == "Charm B" or assembly == "Top B":
                    if p == 0 or p == 1 or p == 3  or p == 4  or p == 5:
                        color = PURE_RED
                elif assembly == "Up C" or assembly == "Charm C" or assembly == "Top C":
                    if p == 0 or p == 1 or p == 2  or p == 3  or p == 4:
                        color = PURE_RED
              

                kwargs = {
                    'point':personality['center'],
                    'color':color,
                    'radius':personality['dot_radius'],
                }
                dot = Dot3D(**kwargs)
                dot.shift(A['position'])
                self.add(dot)
                assemblies.append(Rotating(dot, radians=TAU*32, axis=personality['orbit_normal'], about_point=array(personality['orbit_origin'])+array(A['position']), rate_func=linear, run_time=run_time))
            
            for i in range(3):
                for j in [-personality_offset, personality_offset]:
                    kwargs = {
                        'radius':radius_IV,
                        'color':WHITE,
                        'stroke_opacity':0.5,
                        'stroke_width':1,
                        'fill_opacity':0.0,
                    }
                    personality_orbital_path = Circle(**kwargs)
                    position = [0, 0, 0]
                    position[i] = j
                    personality_orbital_path.move_to(array(position)+array(A['position']))
                    if i == 0:
                        personality_orbital_path.rotate(PI/2, axis=Y_AXIS)
                    elif i == 1:
                        personality_orbital_path.rotate(PI/2, axis=X_AXIS)
                    self.add(personality_orbital_path)

            # it would be nice if we could add all the elements of each assembly to a vgroup so the whole vgroup can rotate.

        
        self.play(*assemblies)

  

        self.wait(0)

