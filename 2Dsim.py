from manim import *
from manim.utils.unit import Percent

# manim -pqh 2Dsim.py sim
#
# Context : Project to discover and document the math of NPQG in conjunction with simulation.
#
# This file : primitive simulation of electrinos and positrinos as Dots in a 2D space and time. (points in a 3-space of real numbers)
    # Notes and script brainstorm follow
    # Case 1 : KE + PE without collisions
    # Case 2 : KE + PE with collisions
    # Use this segment in conjunction with the overall dipole math video. A stepping stone to the full simulation and visualization.
    # What is the time step for the discrete time simulation? How many steps per frame? Tunable.
    # Granularity frame by frame at 4K, composing each frame by specifying the dots.
    # Show field fronts originated point charge T3D history. 
        
                    # 

#
class sim(Scene):
    def construct(self):
