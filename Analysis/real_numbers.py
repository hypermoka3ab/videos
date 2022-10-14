from math import sqrt
from manim import *
from theorems import Theorem, Corollary

chapter = "I"
theorem_count = 0
   




class SupCaracterisation(Scene):
    def construct(self):
        self.state_theorem()
        self.wait()
        self.prove_theorem()

    def state_theorem(self):
        global chapter
        global theorem_count

        # establish theorem
        theorem = VGroup(
            Tex(f"Théorème\\ {chapter}.{theorem_count}"),
            Tex(
                r"Soit $A \subset \mathbb{R}$  un ensemble non vide est $\lambda$ un majorant de $A$."                
            ),
            Tex("Les deux propositions suivantes sont équivalantes:"),
            MathTex(r"(i)  \quad", r"\lambda = \sup A"),
            MathTex(r"(ii) \quad", r" \forall \varepsilon > 0\ \exists x \in A\ \lambda - \varepsilon < x"),
        ).arrange_submobjects(DOWN, aligned_edge = LEFT).to_edge(LEFT)
        
        theorem_count += 1
        for i in range(3):
            self.play(Write(theorem[i]))
            self.wait(i/3 + .5)
        for prop in theorem[3], theorem[4]:
            self.play(Write(prop[0]))
            self.wait(.5)
            self.play(Write(prop[1]))
            self.wait()
        
        self.play(DrawBorderThenFill(
            SurroundingRectangle(theorem, color = WHITE, buff = 0.5)
        ))
        self.wait()

        # clean up
        self.play(
            *[FadeOut(o) for o in self.mobjects]
        )
        self.clear()

    def prove_theorem(self):    
        proof = VGroup(
            *[
                Tex(r"\emph{Démonstration.}"),
                MathTex(r"(i) \Rightarrow (ii):", color = BLUE),
                Tex(r"Posons $\lambda = \sup A$ et soit $\varepsilon > 0$."),
                MathTex(
                    r"\lambda - \varepsilon < \lambda &\Rightarrow \lambda - \varepsilon\ \text{n'est\ pas\ un\ majorant\ de}\ A.\\", 
                    r"&\Rightarrow \exists x \in A\ \lambda - \varepsilon < x\\",
                    r"& \Rightarrow \lambda < x + \varepsilon"
                ),
                MathTex(r"(ii) \Rightarrow (i):", color = BLUE),
                Tex(r"Soit $\lambda$ un majorant de $A$ qui vérifie $(ii)$ et soit $\alpha < \lambda$.")
            ]
        ).arrange_submobjects(DOWN, aligned_edge = LEFT).to_edge(LEFT)
        proof[2:4].shift(RIGHT)
        proof[5].shift(RIGHT)
        self.play(Write(proof.scale(.7)))
        self.wait()


class Sqrt2IsReal(Scene):
    def construct(self):
        self.disprove_s2_gt_2()

    def disprove_s2_gt_2(self):
        real_line = NumberLine([-.5, 3.1], 15, numbers_to_include=[0, 2]).shift(LEFT)
        self.play(Create(real_line))
        self.wait()

        A_brace = always_redraw(lambda: BraceBetweenPoints(real_line.number_to_point(0), real_line.number_to_point(sqrt(2)), UP))
        A_text = always_redraw(lambda: MathTex("A").next_to(A_brace, UP))
        A = VGroup(A_brace, A_text)
        self.play(GrowFromCenter(A[0]), Write(A[1]))
        self.wait()


        s_tracker = ValueTracker(sqrt(2.5))
        s_squared_triangle = always_redraw(
            lambda: Triangle(stroke_width=0, fill_color=WHITE, fill_opacity=1).scale(.1).next_to(
                real_line.number_to_point(s_tracker.get_value() ** 2), DOWN, buff = 0
            )
        )
        s_squared_text = always_redraw(
            lambda: MathTex(r"s^2").scale(.5).next_to(s_squared_triangle, DOWN, buff = SMALL_BUFF)
        )
        s_squared = VGroup(s_squared_triangle, s_squared_text)
        self.play(Write(s_squared[0]), GrowFromCenter(s_squared[1]))
        self.wait()

        s = always_redraw(
            lambda: VGroup(
                MathTex("s", font_size=30),
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1)
            ).arrange(UP, buff=SMALL_BUFF).next_to(real_line.number_to_point(s_tracker.get_value()), DOWN, buff=0) 
        )
        self.play(ReplacementTransform(s_squared.copy(), s))
        self.wait()

        ε_tracker = ValueTracker(0.1)
        s_ε_squared_triangle = always_redraw(
            lambda: Triangle(stroke_width=0, fill_color=WHITE, fill_opacity=1).scale(.1).next_to(
                real_line.number_to_point((s_tracker.get_value() - ε_tracker.get_value()) ** 2), DOWN, buff=0
            )
        )
        
        s_ε_squared_text = always_redraw(
            lambda: MathTex(r"(s - \varepsilon)^2", font_size=25).next_to(s_ε_squared_triangle, DOWN, buff=SMALL_BUFF)
        )
        s_ε_squared = VGroup(s_ε_squared_triangle, s_ε_squared_text)
        
        self.play(GrowFromCenter(s_ε_squared[0]))
        self.wait()

        s_ε_triangle = always_redraw(
            lambda: Triangle(stroke_width=0, fill_color=WHITE, fill_opacity=1).scale(.1).next_to(
                real_line.number_to_point(s_tracker.get_value() - ε_tracker.get_value()), DOWN, buff=0
            )
        )
        
        s_ε_text = always_redraw(
            lambda: MathTex(r"s - \varepsilon", font_size=25).next_to(s_ε_triangle, DOWN, buff=SMALL_BUFF)
        )
        s_ε = VGroup(s_ε_triangle, s_ε_text)

        epsilon_brace = always_redraw(
            lambda: BraceBetweenPoints(
                real_line.number_to_point(s_tracker.get_value() - ε_tracker.get_value()), real_line.number_to_point(s_tracker.get_value()), UP
            )
        )
        epsilon_text = always_redraw(
            lambda: MathTex(r"\varepsilon").next_to(epsilon_brace, UP)
        )
        
        self.play(ReplacementTransform(s_ε_squared[0].copy(), s_ε[0]))

        self.wait()
        epsilon = VGroup(epsilon_brace, epsilon_text)
        self.play(GrowFromCenter(epsilon[0]), Write(epsilon[1]))
        self.wait()
        self.play(Write(s_ε[1]))
        self.play(Write(s_ε_squared[1]))
        self.wait()

        self.play(ε_tracker.animate.set_value(.25))
        self.wait()

        self.play(ε_tracker.animate.set_value(.1))
        self.wait()


        proof = MathTex(
            r"(s - \varepsilon)^2", ">",  "2", r"&\Rightarrow", "s^2", "-", "4", "s", r"\varepsilon",  "+", r"\varepsilon^2", ">", 
            "s^2", "-", "4", r"\varepsilon", ">", "2", r"\\",
            r"\varepsilon", "<", r"{s^2", "-", "2", r"\over", "4}", r"&\\",
        ).to_corner(UL)

        gt2 = MathTex(">", "2").next_to(proof[10], RIGHT)
        
        self.play(
            ReplacementTransform(s_ε_squared[1].copy(), proof[0]),
            ReplacementTransform(real_line.get_number_mobject(2), proof[2]),
            GrowFromCenter(proof[1]),
        )
        self.wait()
        self.play(Write(proof[3]))
        self.play(
            ReplacementTransform(proof[0].copy(), proof[4:11]),
            ReplacementTransform(proof[1:3].copy(), gt2),
        )
        self.wait()

        self.play(
            ReplacementTransform(gt2[0].copy(), proof[11]),
            ReplacementTransform(gt2, proof[16:18]),
        )
        self.wait()
        self.play(
            *[
                ReplacementTransform(proof[i].copy(), proof[j])
                for i, j in zip([4, 5, 6, 8], [12, 13, 14, 15])
            ]
        )
        self.wait()

        self.play(Indicate(proof[4:11]))
        self.play(Indicate(proof[12:16]))
        self.wait()

        self.play(
            *[
                ReplacementTransform(proof[i].copy(), proof[j])
                for i, j in zip(list(range(12, 18)), [21, 22, 25, 19, 20, 23])
            ],
            Write(proof[24]),
        )
        self.wait()

        self.play(Indicate(proof[19:26]))
        self.wait()

    def initial_attempt(self):
        A_definition = MathTex(r"A =", r"\{x\in\mathbb{R}_+|x^2 < 2\}").to_corner(UL)
        s_definition = MathTex(r"s = \sup A").next_to(A_definition, DOWN).to_edge(LEFT)
        s_justification = Tex(r"($2$ est un majorant de $A$)").next_to(s_definition, RIGHT)
        
        
        self.play(Write(A_definition))
        self.wait()        
        self.play(Write(s_definition))
        self.play(Write(s_justification), run_time = .8)
        self.wait()
        self.play(
            FadeOut(A_definition),
            FadeOut(s_justification),
            s_definition.animate.to_corner(UL)
        )
        self.wait()
        alternatives = VGroup(
            MathTex("s^2 > 2"),
            MathTex("s^2 < 2"),
            MathTex("s^2 = 2"),
        ).arrange(DOWN, aligned_edge = LEFT).next_to(s_definition, DOWN)
        
        for alternative in alternatives:
            self.play(Write(alternative))

        self.play(
            *[FadeOut(o) for o in [s_definition, alternatives[1], alternatives[2]]],
            alternatives[0].animate.to_corner(UL)
        )
        self.wait()

        proof = VGroup(
            Tex(r"Soit $0 < \varepsilon < 1$, ", r"$(s - \varepsilon)^2 = s^2 -2s\varepsilon + \varepsilon^2$", r"$\ge s^2 -4\varepsilon$", "."),
            Tex(r"En choisissant $\varepsilon < {s^2 - 2 \over 4}$, ", r"on obtient ",  r"$(s - \varepsilon)^2 > 2$"),
            MathTex(
                r"\forall x \in A\ ", r"(s - \varepsilon)^2 > 2",  r"> x^2", 
                r"\Rightarrow", r"(s - \varepsilon)^2 > x^2", r"\Rightarrow",  r"s -\varepsilon> x"
            ),
            Tex(r"Autrement dit, ", r"$s - \varepsilon$ est un majorant de $A$."),
            Tex(r"ce qui est absurde car $s- \varepsilon < s = \sup A$.")

        ).arrange(DOWN, aligned_edge=LEFT).next_to(alternatives[0], DOWN).to_edge(LEFT)
        
        self.play(Write(proof[0][0]))
        self.play(Write(proof[0][1]))
        self.wait()
        self.play(Write(proof[0][2:]))
        self.wait()
        self.play(Write(proof[1][0]))
        self.play(Write(proof[1][1:]))
        self.wait()
        self.play(Write(proof[2][0]))
        self.play(ReplacementTransform(proof[1][2].copy(), proof[2][1]))
        self.play(Write(proof[2][2]))
        for item in proof[2][3:]:
            self.play(Write(item))
            self.wait()
        self.wait()
        self.play(Write(proof[3]))
        self.wait()
        self.play(Write(proof[4]))
        self.wait()
        

        self.play(Write(always_redraw(lambda : Cross(alternatives[0]))))
        self.wait()
        self.play(
            FadeOut(proof),
            alternatives[0].animate.next_to(s_definition, DOWN),
            FadeIn(alternatives[1]),
            FadeIn(alternatives[2])
        )
        self.wait()
        self.play(Write(always_redraw(lambda : Cross(alternatives[1]))))
        self.wait()
        self.play(alternatives[2].animate.move_to(ORIGIN).to_edge(UP).set_color(YELLOW))
        self.play(Create(SurroundingRectangle(alternatives[2], color = YELLOW)))
        self.wait()




class QDense2(Scene):
    def construct(self):
        # self.illustrate_many_rationals()
        Axy_definition = MathTex(r"A_{x, y} = ", r"\{", r"r \in \mathbb{Q}| x < r < y", r"\}").to_corner(UL)
        Axy_finite = MathTex(r"A_{x, y} = ", r"\{", "r_1",  "<",  "r_2", "<", r"\cdots", "<", "r_n", r"\}").to_corner(UL)
        s = MathTex("s", "=", r"{r_1",  "+",  "r_2",  r"\over 2}").next_to(Axy_finite, DOWN).to_edge(LEFT)
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{stmaryrd}")
        s_in_A = MathTex(
            "x < ", "r_1", "<", "s", "<", "r_2", "< y", r"&\Rightarrow", r"s\in A_{x, y}",
            r"\\ & \Rightarrow", r"s = r_i", r"\text{ pour un certain }", r"i \in \llbracket 1, n \rrbracket",
            tex_template=template
        ).next_to(s, DOWN).to_edge(LEFT)

        s_between_xy = MathTex("r_1", "<", "s", "<", "r_2").next_to(s_in_A, DOWN).to_edge(LEFT)
        r_between_xy = MathTex(
            "r_1", "<", "r_i", "<", "r_2",
            r"\Rightarrow", "1", "<", "i", "<", "2", r"\square"
        ).next_to(s_in_A, DOWN).to_edge(LEFT)
       
        self.play(Write(Axy_definition))
        self.wait()
        self.play(
            ReplacementTransform(Axy_definition[1], Axy_finite[1]),
            ReplacementTransform(Axy_definition[2], Axy_finite[2:9:2]),
            ReplacementTransform(Axy_definition[-1], Axy_finite[-1]),
        )
        self.wait()
        self.play(*[GrowFromCenter(mob) for mob in Axy_finite[3:9:2]])
        self.wait()
        self.play(
            ReplacementTransform(Axy_finite[2].copy(), s[2]),
            ReplacementTransform(Axy_finite[4].copy(), s[4]),
            GrowFromCenter(s[3]),
        )
        self.play(Write(s[5]))
        self.wait()
        self.play(Write(s[:2]))
        self.wait()
        self.play(
            ReplacementTransform(s[0].copy(), s_in_A[3]),
            ReplacementTransform(Axy_finite[2:4].copy(), s_in_A[1:3]),
            ReplacementTransform(Axy_finite[3:5].copy(), s_in_A[4:6]),
        )
        self.wait()
        self.play(Write(s_in_A[0]), Write(s_in_A[6]))
        self.wait()
        self.play(Write(s_in_A[7:]))
        self.wait()
        self.play(ReplacementTransform(s_in_A[1:6].copy(), r_between_xy[:5]))
        self.wait()
        # self.play(
        #     ReplacementTransform(s_in_A[10].copy(), r_between_xy[2]),
        #     ReplacementTransform(s_between_xy[2], r_between_xy[2], run_time=1.5),
        #     Write(r_between_xy)
        # )
        # self.wait()

        self.play(Write(r_between_xy[5:]))
        self.wait()

        

    def illustrate_many_rationals(self):
        real_line = NumberLine([-2, 2], 15) # real line
        line_label = always_redraw( # R label
            lambda: 
                MathTex(r"\mathbb{R}").move_to(real_line.number_to_point(-1.8) + UP * 0.5)    
        )
        x_tracker = ValueTracker(.1) # x tracker
        y_tracker = ValueTracker(.9) # y tracker
        x_label = always_redraw( # x label
            lambda: VGroup(
                MathTex("x", font_size=30).next_to(real_line.number_to_point(x_tracker.get_value()), UP, buff = SMALL_BUFF),
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point(x_tracker.get_value()), DOWN, buff=0)
            )
        )
        y_label = always_redraw( # y label
            lambda: VGroup(
                MathTex("y", font_size=30).next_to(real_line.number_to_point(y_tracker.get_value()), UP, buff = SMALL_BUFF),
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point(y_tracker.get_value()), DOWN, buff=0)
            ) 
        )

        r_label = always_redraw( # r label
            lambda: VGroup(
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point((x_tracker.get_value() + y_tracker.get_value()) / 2), DOWN, buff=0),
                MathTex(r"r", font_size=30),
            ).arrange(DOWN, buff=SMALL_BUFF).next_to(real_line.number_to_point((x_tracker.get_value() + y_tracker.get_value()) / 2), DOWN, buff=0)
        )

        r_prime_label = always_redraw( # r' label
            lambda: VGroup(
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point((x_tracker.get_value() + y_tracker.get_value()) / 2), DOWN, buff=0),
                MathTex(r"r^{\prime}", font_size=30),
            ).arrange(DOWN, buff=SMALL_BUFF).next_to(real_line.number_to_point(0.7), DOWN, buff=0)
        )

        r_2prime_label = always_redraw( # r" label
            lambda: VGroup(
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point((x_tracker.get_value() + y_tracker.get_value()) / 2), DOWN, buff=0),
                MathTex(r"r^{\prime\prime}", font_size=30),
            ).arrange(DOWN, buff=SMALL_BUFF).next_to(real_line.number_to_point(0.3), DOWN, buff=0)
        )

        self.add(real_line, line_label, x_label, y_label)
        self.wait()
        self.play(
            GrowFromCenter(r_label[0]),
            Write(r_label[1])
        )
        self.wait()
        self.play(
            Indicate(y_label),
            Indicate(r_label),
        )
        self.play(
            GrowFromCenter(r_prime_label[0]),
            Write(r_prime_label[1])
        )
        self.wait()
        self.play(
            Indicate(x_label),
            Indicate(r_label),
        )
        self.play(
            GrowFromCenter(r_2prime_label[0]),
            Write(r_2prime_label[1])
        )
        self.wait()
        self.play(
            *[
                FadeOut(mob) for mob in self.mobjects
            ]
        )
        self.wait()


class FiniteInfinite(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{stmaryrd}")
        inf_question = Tex("Qu'est-ce qu'un ensemble ", " in", "fini", " ?").to_corner(UL)
        fin_question = Tex("Qu'est-ce qu'un ensemble ", " fini", " ?").to_corner(UL)
        
        # finite intuition
        finite_intuition = MathTex("E", " = ", r"\{", "x_1, ", "x_2, ", r"\cdots, ", "x_n" r"\}").next_to(fin_question, DOWN).to_edge(LEFT)

        # finite definition

        # map f:
        f_map = VGroup(
            MathTex("f", ":"),
            VGroup(
                Brace(
                    VGroup(
                        MathTex(r"\llbracket 1, n \rrbracket \rightarrow E", tex_template=template),
                        MathTex(r"i \mapsto x_i"),
                    ).arrange(DOWN, aligned_edge=LEFT), LEFT
                ),
                VGroup(
                    MathTex(r"\llbracket 1, n \rrbracket \rightarrow E", tex_template=template),
                    MathTex(r"i \mapsto x_i")
                ).arrange(DOWN, aligned_edge=LEFT),
            ),
            Tex("est une bijection.")
        ).arrange(RIGHT, buff=MED_SMALL_BUFF).next_to(finite_intuition, DOWN).to_edge(LEFT)
        
        self.play(Write(inf_question[:-1]), rate_func=smooth)
        self.play(Write(inf_question[-1]))
        self.wait()
        self.play(ReplacementTransform(inf_question[1:], fin_question[1:]))
        self.wait()
        self.play(Write(finite_intuition))
        self.wait()
        for i in f_map:
            self.play(Write(i))
        self.wait()


class IrrationalsDense(Scene):
    def construct(self):
        self.state_theorem()
        self.set_things_up()
        self.proof()

    def state_theorem(self):
        theorem = Corollary(
            body=VGroup(
                Tex("Soit $x$ et $y$ deux nombres réels tels que $x < y$."),
                Tex("Il existe une infinité de nombres irrationels $s$ tels que $x < s < y$.")
            ).arrange(DOWN, aligned_edge=LEFT),
        )
        self.play(Write(theorem))
        self.play(Write(SurroundingRectangle(theorem, color=WHITE)))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])


    def proof(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{stmaryrd}")
        A = MathTex("A").move_to((DOWN * 1 + LEFT * 2) * 2)
        s2A = MathTex(r"\sqrt{2}A").move_to((DOWN * 1 + RIGHT * 2) * 2)
        i1n = MathTex(r"\llbracket 1, n \rrbracket", tex_template=template).move_to((UP * 1 + RIGHT * 2) *  2)

        f_arrow = VGroup(Arrow(A.get_right(), s2A.get_left(), buff=SMALL_BUFF),)
        f_arrow += MathTex("f").next_to(f_arrow.submobjects[0], UP, buff=SMALL_BUFF)
        f = MathTex(r"r \mapsto r\sqrt{2}").next_to(f_arrow[0], UP, buff=SMALL_BUFF)

        g_arrow = VGroup(Arrow(s2A.get_top(), i1n.get_bottom(), buff=SMALL_BUFF))
        g_arrow += MathTex("g").next_to(g_arrow.submobjects[0], RIGHT, buff=SMALL_BUFF)
        
        fg_arrow = VGroup(Arrow(A.get_top(), i1n.get_left(), buff=SMALL_BUFF))
        fg_arrow += MathTex("f", r"\circ",  "g").rotate(
            fg_arrow.submobjects[0].get_angle()
        ).next_to(fg_arrow.submobjects[-1].get_center(), UL, buff=SMALL_BUFF)
        
        comutative_diagram = VGroup(A, s2A, i1n, f_arrow, g_arrow, fg_arrow)    
        
        s2A_infinit = MathTex(r"\sqrt{2}A", r"\text{ est infini}").to_corner(UL)
        B_infinit = MathTex(r"\Rightarrow", r"B \text{ est infini }", r"\square .").next_to(s2A_infinit, DOWN).to_edge(LEFT)
        
        self.add(A, s2A)
        self.wait(.5)
        self.play(GrowArrow(f_arrow[0]))
        self.wait(.5)
        self.play(Write(f))
        self.wait(.5)
        self.play(ReplacementTransform(f, f_arrow[1]))
        self.wait()
        self.play(Write(i1n))
        self.play(GrowArrow(g_arrow[0]), Write(g_arrow[1]))
        self.wait()
        self.play(GrowArrow(fg_arrow[0]))
        self.play(
            ReplacementTransform(g_arrow[1].copy(), fg_arrow[1][2]),
            ReplacementTransform(f_arrow[1].copy(), fg_arrow[1][0]),
        )
        self.play(Write(fg_arrow[1][1]))
        self.wait()
        self.play(Create(Cross(fg_arrow[1])))
        self.wait()
        self.play(Create(Cross(g_arrow[1])))
        self.wait()
        self.play(ReplacementTransform(s2A.copy(), s2A_infinit[0]))
        self.play(Write(s2A_infinit[1]))
        self.wait()
        for mob in B_infinit:
            self.play(Write(mob))
            self.wait()

    def set_things_up(self):
        B = MathTex("B", " = ", r"\{s \in \mathbb{R}\setminus\mathbb{Q}|x < s < y\}").to_corner(UL)
        A = MathTex(r"A", " = ", r"\left\{r\in  \mathbb{Q}\left|{x\over\sqrt{2}} < r < {y\over\sqrt{2}}\right\}").next_to(B, DOWN).to_edge(LEFT)
        s2A = MathTex(r"\sqrt{2}A", " = ", r"\left\{r\sqrt{2}\left|r \in A\right\}").next_to(A, DOWN).to_edge(LEFT)
        s2A_included_B = MathTex(
            r"\sqrt{2}A", r"\subset", "B", r"\Rightarrow", r"\left(B \text{ est fini } \Rightarrow \sqrt{2}A \text{ est fini } \right)"
        ).next_to(s2A, DOWN).to_edge(LEFT)

        self.play(Write(B))
        self.wait()
        self.play(Write(A))
        self.wait()
        self.play(Write(s2A))
        self.wait()
        self.play(
            ReplacementTransform(s2A[0].copy(),s2A_included_B[0]),
            ReplacementTransform(B[0].copy(),s2A_included_B[2]),
            GrowFromCenter(s2A_included_B[1])
        )
        self.wait()
        self.play(Write(s2A_included_B[3:]))
        self.wait()
        self.play(A[0].copy().animate.move_to((DOWN * 1 + LEFT * 2) * 2), s2A[0].animate.move_to((DOWN * 1 + RIGHT * 2) * 2))
        self.remove(*self.mobjects)



class Intro(Scene):
    def construct(self):
        analyse = Tex("Analyse ",  "réelle?").shift(UP)
        etude_des_fonctions = Tex(
            "Étude des limites des fonctions ",
            r"\((\mathbb{R} \to \mathbb{R})\)"
        )
        self.play(Write(analyse))
        self.wait()
        self.play(ReplacementTransform(analyse[0].copy(), etude_des_fonctions[0]))
        self.wait()
        self.play(ReplacementTransform(analyse[1].copy(), etude_des_fonctions[1]))
        self.wait()
        
        R = Tex(r"\(\mathbb{R}\)?", font_size=80)
        self.play(
            ReplacementTransform(analyse, R),
            ReplacementTransform(etude_des_fonctions, R)
        )
        self.wait()

        approches = Graph(
            ["R", "constructive", "axiomatique"],
            [("R", "constructive"), ("R", "axiomatique")],
            vertex_mobjects={
                "R": Tex(r"\(\mathbb{R}\)?", font_size=80), 
                "constructive": Tex("Constructive"), 
                "axiomatique": Tex("Axiomatique")
            }, layout="tree", root_vertex="R",
            edge_config={"buff": MED_LARGE_BUFF}
        )
        
        self.play(ReplacementTransform(R, approches["R"]))
        for v in approches.vertices:
            if v != "R":
                self.play(Create(approches.edges[("R", v)]))
                self.play(Write(approches[v]))
                self.wait()

        

        