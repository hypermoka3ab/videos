from manim import *

class Logic(Scene):
    
    
    def construct(self):
        self.add_sound("tmp/foundations/prop")
        self.define_proposition()
        self.introduce_truth_tables()

    def introduction(self):
        """
        Reasoning, proofs, and asking what is a proposition.
        """
        
        # Ask what is a proposition?
        question = Text("C'est quoi Une proposition ?", font = "Latin Modern")
        self.play(Write(question))
        pass

    def define_proposition(self):
        """
        Intuitive explanation of the notion of a proposition and truth value, and hook for truth tables
        """
        one = MathTex("(1", ")")
        zero = MathTex("(0", ")")
        true = MathTex(r"(\mathrm{Vrai}", ")")
        false = MathTex(r"(\mathrm{Faux}", ")")
        T = MathTex("(V", ")")
        F = MathTex("(F", ")")

        P = MathTex("P = ", r'\mathrm{``}2\ \mathrm{est\ un\ nombre\ pair"}')
        Q = MathTex("Q = ", r'\mathrm{``}3\ \mathrm{est\ un\ nombre\ pair"}').shift(DOWN)
        
        for o in one, true, T:
            o.next_to(P, RIGHT)
        for z in zero, false, F:
            z.next_to(Q, RIGHT)


        self.wait(6)
        self.play(Write(P[1]), run_time=2)
        self.play(Write(true))
        
        self.wait(2)
        self.play(Write(P[0]))
        self.wait(1)
        

        self.play(Write(Q[1]), run_time=2)
        self.play(Write(false))
        self.wait(2)
        self.play(Write(Q[0]))
        self.wait(7)

        self.play(*[ReplacementTransform(f, l) for f, l in zip(true, T)])
        self.play(*[ReplacementTransform(f, l) for f, l in zip(false, F)])
        self.play(*[ReplacementTransform(f, l) for f, l in list(zip(T, one)) + list(zip(F, zero))])
        self.wait(8)

        PandQ = MathTex(r'\mathrm{``}2\ \mathrm{est\ un\ nombre\ pair"\ }', r'\mathrm{et\ }', r'\mathrm{``}3\ \mathrm{est\ un\ nombre\ pair"}').shift(UP * 2)
        QimpP = MathTex(r'\mathrm{Si\ }', r'\mathrm{``}3\ \mathrm{est\ un\ nombre\ pair"}', r'\mathrm{\ alors\ }', r'\mathrm{``}2\ \mathrm{est\ un\ nombre\ pair"}').shift(UP)

        self.play(*[ReplacementTransform(f.copy(), l) for f, l in [(P[1], PandQ[0]) , (Q[1], PandQ[2])]])
        self.play(Write(PandQ[1]))
        self.wait(3)
        self.play(*[ReplacementTransform(f.copy(), l) for f, l in [(P[1], QimpP[3]) , (Q[1], QimpP[1])]])
        self.play(Write(QimpP[0]), Write(QimpP[2]))
        self.wait(2)

        self.play(*[FadeOut(f) for f in [P, Q, PandQ, QimpP, one, zero]])

        self.wait(6)

        retenir = Text("Ce qu'il faut retenir: ").to_edge(UP)
        self.play(Write(retenir))
        self.wait(2)
        ponits = [
            Text("1. Elles ont une valeur de vérité.\n").scale(.8).shift(UP),
            Text("2. Elles peuvent être composées pour\n donner des propositions plus complexes.\n").scale(.8),
            Text("3. Dans ce cas, la valeur de vérité de la\n proposition qui résulte dépend exclusivement\n des valeurs de vérité de ses composantes.\n").scale(.8).shift(DOWN * 2)
        ]
        for p in ponits:
            self.play(Write(p))
            self.wait(3.5)
        self.wait(2)
    def introduce_truth_tables(self):
        pass

class TruthTable(Scene):
    def construct(self):
        vals = VGroup(
            MathTex("111"), MathTex("0"), MathTex("1"), MathTex("0")
        ).arrange_in_grid(2, 2)
        rects = VGroup(*[
            SurroundingRectangle(v) for v in vals
        ])
        self.play(Create(vals), Create(rects))
        self.wait(2)