from manim import *


class State(VGroup):
    def __init__(self, label:MathTex, is_initial=False, is_final=False):
        self.label = label
        self.outer = VGroup()

        self.outer += Ellipse(width=label.width+.5, height=label.height+.5, stroke_width=1.5, color=WHITE) 
        # Circle(radius=0.5, stroke_width=1.5, color=WHITE)
        if is_final:
            self.outer += Ellipse(width=self.outer.width-.1, height=self.outer.height-.1, stroke_width=1.5, color=WHITE)
        if is_initial:
            self.outer += MathTex(r"\Rightarrow").rotate(-PI / 4).next_to(self.outer[0], UL, buff=-.15)
        
        VGroup.__init__(
            self,
            VGroup(self.outer, self.label)
        )


class Automaton(VMobject):
    def __init__(self):
        pass

class Test(Scene):
    def construct(self):
        s = State(MathTex(r"{s_0, s_1, s_2}"), True, True)
        self.play(Create(s))
        self.wait()