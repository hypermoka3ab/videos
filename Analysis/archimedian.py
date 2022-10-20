from manim import *

class ArchimedianProperty(Scene):
    def construct(self):
        self.illustrate_property()
        self.wait()
        self.state_theorem()
        self.wait()        
        self.prove_it()

    def state_theorem(self):
        from theorems import Theorem
        
        theorem = Theorem(
            title="Propriété d'Archimède",
            body=Tex(
                "Pour tout ", r"\(x>0\)", " et pour tout ",
                r"\(y\in\mathbb{R}\)", " il existe un ", r"\(n\in\mathbb{N}\)",
                " tel que ", r"\(nx>y\)", " i.e:",
                r"\[\forall x>0, \forall y\in\mathbb{R}, \exists n\in\mathbb{N}, \ nx>y\]",
                tex_environment=None,
                font_size=40
            )
        )

        self.play(Write(theorem.title))
        self.wait()
        self.play(Write(theorem.body))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])


    def prove_it(self):
        anti_hyothesis = MathTex(r"\forall n\in\mathbb{N},\ nx \le y").shift(UP).to_edge(LEFT)
        a_major = MathTex(
            r"\Rightarrow", r"A=\{nx|n\in\mathbb{N}\} \text{ et majoré}", r", s=\sup{A}"
        ).next_to(anti_hyothesis, DOWN).to_edge(LEFT)
        caracterise = MathTex(
            "s-x < nx", r"\Rightarrow s < (n+1)x", r"\in A", r"\ \square"
        ).next_to(a_major, DOWN).to_edge(LEFT)

        self.play(Write(anti_hyothesis))
        self.wait()
        for part in a_major:
            self.play(Write(part))
            self.wait()

        for part in caracterise:
            self.play(Write(part))
            self.wait()

    def illustrate_property(self):
        from math import sqrt
        
        y_to_x_ratio = 2*sqrt(5)
        nxs = ValueTracker(1)
        x_length = ValueTracker(1)
        x_segment = always_redraw(
            lambda:
            NumberLine(
                [0, nxs.get_value()],
                unit_size=x_length.get_value(),
            ).to_edge(LEFT).shift(UP)
        )
        x_label = MathTex("x").next_to(x_segment, UP)

        y_length = y_to_x_ratio * x_length.get_value()
        y_segment = NumberLine([0, 1], y_length).to_edge(LEFT)
        y_label = MathTex("y").next_to(y_segment, DOWN)

        self.play(
            Create(x_segment), Create(y_segment),
            Write(x_label), Write(y_label)
        )
        

        self.wait()
        for _ in range(1, int(y_to_x_ratio)+1):
            self.play(nxs.animate.increment_value(1))
            self.wait()

        self.play(
            nxs.animate.set_value(int(y_to_x_ratio*1.5)+1),
            x_length.animate.set_value(x_length.get_value()/1.5)
        )
        self.wait()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        