# The goal is to illustrate each of Maxwell's Equations in the point charge universe.
# Show how they apply and the implications.
# Show revisions if needed.
# this is the language of maxwell's equations, so need to understand them again and relate them to point charges.
# then I should be ready to simulate!
# also may need to clarify those equations!!!  especially at r=0, and v>@.
# I should do a verision in natural units, where @=1, q=1, etc.  Then do the translation.
# that J in maxwell's fourth equation sticks out like a sore thumb. that's not describing point charges.
# they need to be rewritten for point charges.

# See 3b1b and steve brunton div and curl and gradient videos and wikipedia.

# Divergence of the E field
# the unit potentials are the only entities with divergence. 
# translated into our terminology, 
# the electrino has a charge divergence of -e/6, 
# the positrino has a charge divergence of +e/6,
# that's it, there is no other divergence in the universe. This is it.
# so that is another characteristic of the unit potentials.
# Show the divergence relative to the eight-ball (t, x, y, z, vx, vy, vz, q)
# and the charge divergence for each point charge is what? 
# We have potential flow rate = q  dA/dt . Interesting, is it really a flow rate in terms of area of a sphere? Hmmm.  
# We treat the potential as if it releasing spherical surfaces with a scalar potential at the origin
# The potential comes down the 1/r curve.
# The area of a sphere is given by 4 pi r^2.
# So does that work out to a flow rate equal to the divergence?
# So the total potential on the surface at any given radius is 4 pi r^2 * q/r? 

# If we take the unit sphere then f(x,y,z) = x*xhat, y*yhat, z*zhat.
# So the natural divergence is 3 according to Brunton because each partial derivative yields 1 and they are summed by the dot product.
# But what are we trying to measure here?  Charge or potential? Or both.
# If we define the potential field as f(x,y,z,t)= q/(@)r, where r = sqrt (x^2 + y^2 + z^2)
# what are the units of divergence anyway?  Is it a charge or potential per unit area? i.e., over a sphere?
# if math defines divergence as dimensionless, should I put in the units for this specific application of math?
# It would make sense to at least have a trace of how all the dimensional analysis arises.
# oh also we need to talk about the permittivity of free space.  
# We need permittivity of spacetime to understand photon assemblies and the speed of light through spacetime assemblies.
# But permittivity of free space doesn't make sense at the level of point charges. It comes later at a higher assembly order.
# So that is our first adaptation of Maxwell's equations for point charges.
# Brunton relates positive divergence to a fluid that is decompressing.  A negative divergence is a fluid compressing.  Interesting.

# if the charge is moving, what is the effective starting charge of each sphere stream?
# It seems like it would have to be evenly distributed over the distance traveled.
# so if dx = v dt, then each sphere emits v dt as a constant rate.  
# therefore this is why we divide by the velocity.
# I'm still unhappy with how this blows up when velocity is < 1. Arghhhh.

# Brunton now ties this constant divergence as follows
# x(t) = x(0)e^t, y(t) = y(0)e^t
# arghh, am I getting this all mixed up? how to do this from first principles of the point charge universe?



# Divergence of the B field
# Check, makese sense. There are no magnetic monopoles.
# There are no other extraneous terms in this equation, so it maps directly to the point charge universe.
# However, we may find that there is a superior mathematics for the point charge approach.
# It would be cool if it was geometric.
# Many of these regular assemblies can be viewed as a standing wave that is rotating and translating. 
# Thinking that way may lead to the more general geometric solution.

# relationship of E and B.
# need to work on this
# "the curl of E is equal to -dB/dt"
# Again, no extraneous terms.
# Does this equation cover the full range of point charge paths and velocities?
# We need the general solution, not just the circle or ellipse.
# Basically each point charge in a pairwise relationship is riding on the Dirac sphere stream of the other.
# So what is that general solution. A two body solution for potential.  I would think that should exist already?
# Brunton says that if you are looking at two dimensional vector fields in i-hat, and j-hat then the curl is is k-hat.  wtf?
# So what does that mean for point charges in three dimensions? What is the dimension for curl?

# Oct 2023, watching Dr. Don Lincoln new video on magnetism. Very interesting. 
# I been watching several videos on how magnetism is taught. 
# Dr. Don has made it clear to me that the level described is potentially very different than the point charge level and math.
# He described relativistic effects on the charges in a current making a wire become non-neutral when carrying a current, 
# relative to a moving charged particle, let's say electron.
# Relativity means we are talking about spacetime assemblies, and the change in electron geometry with velocity.
# Wow, even this pattern is an example of nature echoing its patterns at different scales.  Wow.
# Ok, so that is all the permission I need so I can think differently.  
# I do not need a 1 to 1 mapping of electromagnetic theory to the point charge level.
# Instead, I am looking for the simpler behaviour at the point charge level that then maps directly to the higher level theory and math.
# which all begs the question it all comes down to which is understanding the specific equations for all cases of two point charges.
# That comes down to the dirac sphere stream from the emitting charge to the receiving charge.
# I think I understand much of the influence of the path of the emitter. (the eight ball : t, x, y, z, dx/dt, dy/dt, dz/dt, q)
# Assuming the sensible idea of constant rate emission of potential.
# So now it comes down to the equation for a receiver at any potential velocity intersecting a Dirac sphere.
# And once we have that, then we have superposition of action from every possible charge within the designated scope of the
# simulation, and someday with an AI generated background adding some shaped variation as desired.

# Ok, if we think in terms of each pair of point charges, then each point charge is always intersecting somewhere on the Dirac
# sphere stream of the other. Think of it like a giant ski slope.  
# If the partner is a like charge the force tends to push you down the ski slope.
# An electrino, being a negative potential is at the negative pole of potential. A positrino sphere stream exerts action up the slope.
# An positrino, being a positive potential is at the positive pole of potential. A electrino sphere stream exerts action down the slope.
# But action is symmetrical on the 1/r curve. How cool is that? So we can think of this from either perspective.
# Gosh, I remember drawing a picture way back in 2018 when I was pondering the ontology of potential. 
# The portion of the receiver velocity that is orthogonal to the emitter's sphere stream (i.e., along the surface) experiences no action?
# That seems to make sense, because at any time t, the potential is identical everywhere on the sphere, i.e., in any direction on the sphere.
# Next we focus on the component of velocity that is on the line that coincides with the radius of the intersecting sphere.
# Alright. Let's go through the cases.  Remember that emitter potential magnitude has been reduced by a factor of v. (And at v=0 it's a Dirac delta).
# Case 1 : Emitter positrino : Receiver electrino
#   The action is a force towards the path location at emission.
#   If v (||r) is moving away, the action must slow v in that direction.
#   If v (||r) is moving toward, the action increasess v in that direction.
# Case 2 : switch case 1. Everything is the same.
# Case 3 : electrino:electrino or positrino:positrino
#   The action is a force away from the path location at emission.
#   If v (||r) is moving away, the action increasess v in that direction.
#   If v (||r) is moving toward, the action must slow v in that direction.
# So is that it?  We need write down the geometry of the situation and do out sin()s and cosine()s. 
# And then see what happens in simulation. 
# Will this be a simple formula where q1 and q2 resolve the direction of the force?  Prolly. We'll see.
# Another cool think about this approach is that it is velocity agnostic in a way. 
# It doesn't care when the point charge velocity blasts through c or @.  
# We have assigned no a priori fundamental speed limit to the point charge. 
# It's pretty cool (and fortunate) that a natural speed limit emerges in an electrino:positrino binary.

# In a simulation we need to store the path history of all relevant point charges, which could be a few or a lot depending on the objective.
# The task at every t is to find all the Dirac sphere crossings for each pair of point charges.
# Usually there will only be one crossing, but if v has exceeded @ there may be more than one.
# We will need efficient algorithms to deterine those crossings. Some algorithms may be simulation objective dependent.
# There is no doubt many mathematical and computational techniques that will be developed.
# Quite a bit over my head here, but I wonder if there is such a thing as a 4D space filling curve (t,x,y,z)?
# That way we could computationally store path extents (A to B) very inexpensively. 
# This would be the level to do the first pass intersections. 
# Perfect, you can use this data structure to reduce both the amount of computation and the memory for computing intersections.
# Most of the cubes for each point charge pair will not have an intersection with time t-now. So those are quickly eliminated.
# You probably want to tune the granularity of the first level cubes.
#
# It may makes sense to cache 4D cubes? This is a tradeoff. 
# What is the latency and compute resource for a cube cache lookup or cube calculation? 
# Ok, so let's say there's an intersection detected in the first level 4D cube? Then what?
# Here is where we either do a cube cache lookup or go direct to calculation. Of course on a cache miss we also do the calculation.
# And there are all kinds of ways to keep going one or multiple levels at a time.
# We continue descending this computational structure until we calculate the intersection to within the simulation requirement.

# On top of all this we might also introduce some spatial indices so we can go more directly to a finer granularity cube.
# How cool is this???