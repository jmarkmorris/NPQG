from manim import *

class NPQGlogo(Scene):
    def construct(self):

        # Note : Encountered problems trying to set different fonts and see what looked best. The default is ok for now.

        Nsquare = Square(side_length=2.2)
        Nsquare.set_stroke('#0000ff', width=20, opacity=100)
        Nsquare.set_fill(WHITE, opacity=100)
        Ncircle = Circle(radius=.95, color='#0000ff')
        Ncircle.set_stroke('#0000ff', width=20, opacity=100)
        Ncircle.add(Text(text= "N", color='#0000ff',font_size=2.2*DEFAULT_FONT_SIZE,weight=NORMAL, stroke_width=10))
        # Ncircle.add(Text(text= "N", color='#0000ff',font="Engravers MT",font_size=2.2*DEFAULT_FONT_SIZE,weight=NORMAL, stroke_width=10))
        N = VGroup(Nsquare, Ncircle)
        
        Psquare = Square(side_length=2.2)
        Psquare.set_stroke('#ff0000', width=20, opacity=100)
        Psquare.set_fill(WHITE, opacity=100)
        Pcircle = Circle(radius=.95, color='#ff0000')
        Pcircle.set_stroke('#ff0000', width=20, opacity=100)
        Pcircle.add(Text(text= "P", color='#ff0000',font_size=2.2*DEFAULT_FONT_SIZE,weight=NORMAL, stroke_width=10))
        # Pcircle.add(Text(text= "P", color='#ff0000',font="Engravers MT",font_size=2.2*DEFAULT_FONT_SIZE,weight=NORMAL, stroke_width=10))
        P = VGroup(Psquare, Pcircle)
        
        Qsquare = Square(side_length=2.2)
        Qsquare.set_stroke('#800080', width=20, opacity=100)
        Qsquare.set_fill(WHITE, opacity=100)
        Qcircle = Circle(radius=.95, color='#800080')
        Qcircle.set_stroke('#800080', width=20, opacity=100)
        Qcircle.add(Text(text= "Q", color='#800080',font_size=2.2*DEFAULT_FONT_SIZE,weight=NORMAL, stroke_width=10))
        # Qcircle.add(Text(text= "Q", color='#800080',font="Engravers MT",font_size=2.2*DEFAULT_FONT_SIZE,weight=NORMAL, stroke_width=10))
        Q = VGroup(Qsquare, Qcircle)

        Gsquare = Square(side_length=2.2)
        Gsquare.set_stroke('#008b29', width=20, opacity=100)
        Gsquare.set_fill(WHITE, opacity=100)
        Gcircle = Circle(radius=.95, color='#008b29')
        Gcircle.set_stroke('#008b29', width=20, opacity=100)
        Gcircle.add(Text(text= "G", color='#008b29',font_size=2.2*DEFAULT_FONT_SIZE,weight=NORMAL, stroke_width=10))
        # Gcircle.add(Text(text= "G", color='#008b29',font="Engravers MT",font_size=2.2*DEFAULT_FONT_SIZE,weight=NORMAL, stroke_width=10))
        G = VGroup(Gsquare, Gcircle)

        N.move_to([-1.25,1.25,0])
        P.next_to(N, RIGHT, buff=0.5)        
        Q.next_to(N, DOWN, buff=0.5)        
        G.next_to(Q, RIGHT, buff=0.5)  

        Logo = VGroup(N,P,Q,G)      
        
        # self.add(Logo)
        self.play(GrowFromPoint(Logo, ORIGIN, rate_func=rate_functions.rush_from))
        self.play(Indicate(N, color='#0000ff'), 
                  Indicate(P, color='#ff0000'), 
                  Indicate(Q, color='#800080'), 
                  Indicate(G, color='#008b29'))
        # self.play(Indicate(P, color='#ff0000'))
        # self.play(Indicate(Q, color='#800080'))
        # self.play(Indicate(G, color='#008b29'))

        self.wait(2)
       


# between the circle and the border put a pattern or leave white for now and do that later on special occasions, like google.
# or write out the words on the outer edge of each circle Neoclassical Physics and Quantum Gravity
