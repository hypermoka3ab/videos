from manim import *

class ArchimedianProperty(Scene):
    def construct(self):
        self.state_theorem()
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

        self.add(theorem)
        self.wait()

    def prove_it(self):
        pass