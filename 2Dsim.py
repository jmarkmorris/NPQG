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
        # T3D is a mnemonic for Euclidean 3D space and 1D time.
        # Google search for T3D
            # Didn't reveal any significant conflicting use cases.
            # One historical use of relevance to computational simulation.
                # The T3D (Torus, 3-Dimensional) was Cray Research's first attempt at a massively parallel supercomputer architecture. 
                # The computer went online on July 1, 1994. 
            # Is there already a symbol for Euclidean space and time?
                # Mathematically the Euclidean space and time would use a mathematical structure called a 4-space.
                # The 4-space is often symbolized with a stylized capital R superscript 4.
                # The void of 3D space and 1D time is modeled with a 4-space mathematical structure.
                # This immediately leads to a fork in the road on math since Euclidean space and time are orthogonal concepts.

# N.B. Insight Alert! 
# Einsteinian spacetime braids space and time together into a geometry of General Relativity.
# In the NPQG era, we (will) have complete awareness of the geometry and mathematics from the perspective of Euclidean 4-space.
    # The mathematics of NPQG are expected to be straightfoward and understandable.
# Some problems require understanding the deformable frame of spacetime.
    # Einstein's General Relativity will continue to be useful in certain domains and scales.
                    # 

#
class sim(Scene):
    def construct(self):
