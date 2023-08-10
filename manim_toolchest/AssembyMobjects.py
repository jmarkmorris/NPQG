# These are some ideas and tools for working using mobjects to build up assemblies and assemblies of assemblies.


# You can scale Manim mobjects. One way to do this is by using the scale method of the Mobject class. 
# You can scale a Mobject instance named mob by calling mob.scale(scale_factor), where scale_factor is the desired scaling factor. 
# You can also use an updater function to scale a Mobject over time.
# i.e., use mob.scale(1.02) in an updater function to slowly increase the size of the square by two percent at each update iteration.

# Research how to do this in manim where the sub-mobjects are 3D animations themselves, that evolve.

# Ideally want everything about the behaviour specified via an API dictionary.
# I'm not quite sure how that works in Manim. Is everything working off the same clock?