from manim import *

class Convergence(Scene):
    def construct(self):
        #self.PositionDuProbleme()
        #self.PremiereConjecture()
        trivial = MathTex(r"u_n = n^2,\  n \ge 0:").to_corner(UL, buff=1)
        moinsTrivial = MathTex(r"u_n = 2^{n(-1)^n}")
        UnFleche0 = MathTex(r"u_n \rightarrow 0")
        NDefUnFleche0 = MathTex(
            r"\forall \varepsilon > 0,\ \exists,",
            r"\underbrace{", 
            "n_0", 
            "}_0",
            r"\in \mathbb{N},\ ", 
            r"\underbrace{", 
            r"|u_{n_0}|",
            "}_0", 
            r" < \varepsilon"
        )
        self.play(Write(trivial))
        self.wait()
        NDefUnFleche0.next_to(trivial, DOWN).shift(RIGHT/2)
        self.play(*[Write(NDefUnFleche0[i]) for i in [0, 2, 4, 5, 6, 8, 9]])
        self.wait()
        N0Brace = VGroup(Brace(NDefUnFleche0[1]), MathTex("0")).arrange(DOWN)
        #self.add(N0Brace)
        self.wait()

    def PositionDuProbleme(self):
        # Question principale
        question = Text("Qu'est-ce qu'on entend par ``$u_n$ converge vers ", r"$\ell$", "''?")
        
        # Question simplifiée
        question_modeste = Text("Qu'est-ce qu'on entend par ``$u_n$ converge vers ", "$0$", "''?")
        
        # Position de la question principale
        self.play(Write(question))
        self.wait()
        
        # Position de la question simplifiée
        self.play(ReplacementTransform(question, question_modeste))
        self.wait()
        
        # Éffacement de la question
        self.play(
            Write(
                question_modeste,
                rate_func = lambda t: 1 - t
            )
        )
        self.wait()
    
    def PremiereConjecture(self):
        UnFleche0 = MathTex(r"u_n \rightarrow 0").shift(UP).scale(1.5)
        equivaut = MathTex(r"\Updownarrow", "?").scale(2)
        implique2 = MathTex(r"\Downarrow", r"\quad", r"\Uparrow", "?").scale(2)
        NDefUnFleche0 = MathTex(r"\forall \varepsilon > 0,\ \exists n_0 \in \mathbb{N},\ |u_{n_0}| < \varepsilon").shift(DOWN)

        self.play(Write(UnFleche0), run_time=.5)
        self.wait()

        self.play(Write(NDefUnFleche0))
        self.wait()

        self.play(Write(equivaut[0]))
        self.wait()

        self.play(Write(equivaut[1]))
        self.wait()

        self.play(
            ReplacementTransform(equivaut[0].copy(), implique2[0]),
            ReplacementTransform(equivaut[0].copy(), implique2[2]),
            FadeOut(equivaut)
        )
        self.wait()
        implique2.set_color_by_tex("?", BLACK)
        self.play(implique2.set_color_by_tex, r"\Downarrow", GREEN)
        self.wait()
        implique2.set_color_by_tex("?", WHITE)
        self.play(Write(implique2[3]))
        self.wait()
        
        All = VGroup(UnFleche0, NDefUnFleche0, implique2)
        self.play(
            Write(
                All, rate_func = lambda t: 1 - t 
            )
        )

