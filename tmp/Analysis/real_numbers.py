from math import sqrt
from manim import *
chapter = "I"
theorem_count = 0

class Theorem(VGroup):
    count = 0
    CONFIG = {
        "align": DOWN
    }
    def __init__(self, body, title=None):
        Theorem.count += 1
        self.body = body
        self.title = Tex(f"Théorème {chapter}.{Theorem.count} ({title})" if title else f"Théorème {chapter}.{Theorem.count}")
        # create down arranged theorem
        VGroup.__init__(
            self, 
            VGroup(
                self.title,
                self.body
            ).arrange(DOWN, aligned_edge=LEFT)
        )

class Lemma(Theorem):
    def __init__(self, body, title=None):
        Theorem.count += 1
        self.body = body
        self.title = Tex(f"Lémme {chapter}.{Theorem.count} ({title})" if title else f"Lémme {chapter}.{Theorem.count}")
        # create down arranged theorem
        VGroup.__init__(
            self, 
            VGroup(
                self.title,
                self.body
            ).arrange(DOWN, aligned_edge=LEFT)
        )

class Corollary(Theorem):
    def __init__(self, body, title=None):
        Theorem.count += 1
        self.body = body
        self.title = Tex(f"Corollaire {chapter}.{Theorem.count} ({title})" if title else f"Corollaire {chapter}.{Theorem.count}")
        # create down arranged theorem
        VGroup.__init__(
            self, 
            VGroup(
                self.title,
                self.body
            ).arrange(DOWN, aligned_edge=LEFT)
        )


class Axioms(Scene):
    def construct(self):
        self.axioms = VGroup(
            *[
                MathTex(f"\\mathrm{{axiome}}\ {i + 1}\ {axiom} ", font_size=20)
                for i, axiom in enumerate(
                    [
                        # I Addition
                        r"\forall x, y, z \in \mathbb{R},\ x + (y + z) = (x + y) + z",
                        r"\forall x, y \in \mathbb{R},\ x + y = y + x",
                        r"\exists 0 \in \mathbb{R}\ \forall x \in  \mathbb{R},\ x + 0 = 0 + x = x",
                        r"\forall x \in \mathbb{R}\ \exists y \in \mathbb{R},\ x + y = y + x = 0",
                        
                        
                        # II Multiplication
                        r"\forall x, y, z \in \mathbb{R},\ x \cdot (y \cdot z) = (x \cdot y) \cdot z",
                        r"\forall x, y \in \mathbb{R},\ x \cdot y = y \cdot x",
                        r"\exists 1 \in \mathbb{R}\ \forall x \in  \mathbb{R},\ x \cdot 1 = 1 \cdot x = x",
                        r"\forall x \in \mathbb{R} \backslash \{0\}\ \exists y \in \mathbb{R},\ x \cdot y = y\cdot x = 1",

                        # I + II Distributivity
                        r"\forall x, y, z \in \mathbb{R},\ x \cdot (y + x) = x\cdot y + x\cdot z",

                        # III Order
                        r"\forall x \in \mathbb{R},\ x \le x",
                        r"\forall x, y \in \mathbb{R},\ (x \le y \wedge y \le x) \Rightarrow x = y",
                        r"\forall x, y, z \in \mathbb{R}, (x \le y \wedge y \le z) \Rightarrow x \le z",
                        r"\forall x, y \in \mathbb{R},\ x \le y \lor y \le x",

                        # I + III Order and addition
                        r"\forall x, y, z \in \mathbb{R},\ x \le y \Rightarrow x + z \le y + z",

                        # II + III Order and multiplication
                        r"\forall x, y \in \mathbb{R},\ (0 \le x \wedge 0 \le y) \Rightarrow 0 \le x\cdot y",

                        # IV Completeness
                        r"""
                            \forall A, B \in \mathcal{P}(\mathbb{R})\backslash\{\emptyset\}, \ 
                            (\forall x \in A\ \forall y\in B,\  x \le y) 
                            \Rightarrow 
                            (\exists z \in \mathbb{R}\ \forall x \in A \ \forall y \in B, \  x \le z \le y)
                        """
                    ]
                )
            ]
        ).arrange(DOWN, aligned_edge = LEFT).to_edge(LEFT)

        self.introduce_axioms()
        self.wait()
        
    def introduce_axioms(self):
        self.play(Write(self.axioms[:15]))
        
        for i in [0, 3, 11]:
            self.play(Indicate(self.axioms[i]))
            self.wait()
            

class Sqrt2IsNotRational(Scene):
    def construct(self):
        hyothesis = MathTex(
            r"\text{Soient }", r"p ,q \in \mathbb{N} \text{ tels que }", "{p", "^2", r"\over",  "q", "^2}", "=", "2",
            r"\text{ et }", "p", r"\wedge", "q", "=", "1"
        ).to_corner(UL)
        
        proof_p_even =  MathTex(
            "{p", "^2", r"\over",  "q", "^2}", "=", "2", r"&\Rightarrow", "p", "^2", "=", "2", "q", "^2", 
            r"\\ &\Rightarrow", "2", "|", "p", "^2", 
            r"\\ &\Rightarrow", "2", "|", "p", 
            r"\\ &\Rightarrow", "p", "=", "2", "k", r",\ k \in \mathbb{N}", 
        ).next_to(hyothesis, DOWN).to_edge(LEFT)
        
        proof_q_even =  MathTex(
            "p", "^2", "=", "2", "q", "^2", r"&\Rightarrow", "(", "2", "k", ")", "^2", "=", "2", "q", "^2",
            r"\\ &\Rightarrow", "4", "k", "^2", "=", "2", "q", "^2",
            r"\\ &\Rightarrow", "2", "k", "^2", "=", "q", "^2",
            r"\\ &\Rightarrow", "2", "|", "q", "^2",
            r"\\ &\Rightarrow", "2", "|", "q",
        ).next_to(hyothesis, DOWN).to_edge(RIGHT)

        p_q_even =  MathTex(
            "2", "|", "p", r"\wedge", "2", "|", "q",
            r"\Rightarrow", "2", "|", "p", r"\wedge", "q",
            r"\Rightarrow", "2", "|", "1"
        ).next_to(hyothesis, DOWN).to_edge(LEFT)

        changes_to_p = [
            [
                tuple(range(2, 10)),
                tuple(range(7)),
            ],
            [
                (0, 1, 3, 4, 5, 6),
                (8, 9, 12, 13, 10, 11)
            ],
            [
                (11, 8, 9),
                (15, 17, 18)
            ],
            [
                (15, 16, 17),
                (20, 21, 22)
            ],
            [
                (20, 22),
                (26, 24)
            ]
        ]

        changes_to_q = [
            [
                (8, 9, 12, 13, 10, 11),
                tuple(range(6))
            ],
            [
                (0, 0, 1, 2, 3, 4, 5),
                (7, 10, 11, 12, 13, 14, 15)
            ],
            [
                (-3, -2),
                (8, 9)
            ],
            [
                (8, 9, 11, 12, 13, 14, 15),
                tuple(range(17, 24))
            ],
            [
                (17, 18, 19, 20, 22, 23),
                (25, 26, 27, 28, 29, 30)
            ],
            [
                (25, 29, 30),
                (32, 34, 35)
            ],
            [
                (32, 33, 34),
                (37, 38, 39)
            ]
        ]

        changes_to_qp = [
            [
                [21, 22, 23], 
                [0, 1, 2]
            ],
            [
                (37, 38, 39),
                (4, 5, 6)
            ],
            [
                (0, 4, 1, 5, 2, 3, 6),
                (8, 9, 8, 9, 10, 11, 12)
            ],
            [
                (8, 9, 10, 11, 12),
                (14, 15, 16, 16, 16)
            ]
        ]
        self.play(Write(hyothesis))
        self.wait()
        self.play(
            *[
                ReplacementTransform(hyothesis[pre].copy(), proof_p_even[post])
                for pre, post in zip(*changes_to_p[0])
            ]
        )
        self.wait()
        self.play(Write(proof_p_even[7]))
        self.play(
            *[
                ReplacementTransform(proof_p_even[pre].copy(), proof_p_even[post])
                for pre, post in zip(*changes_to_p[1])
            ]
        )
        self.wait()
        self.play(Write(proof_p_even[14]))
        self.play(
            *[
                ReplacementTransform(proof_p_even[pre].copy(), proof_p_even[post])
                for pre, post in zip(*changes_to_p[2])
            ],
            Write(proof_p_even[16])
        )
        self.wait()
        self.play(Write(proof_p_even[19]))
        self.play(
            *[
                ReplacementTransform(proof_p_even[pre].copy(), proof_p_even[post])
                for pre, post in zip(*changes_to_p[3])
            ]
        )
        self.wait()
        self.play(Write(proof_p_even[23]))
        self.play(
            *[
                ReplacementTransform(proof_p_even[pre].copy(), proof_p_even[post])
                for pre, post in zip(*changes_to_p[4])
            ],
            Write(proof_p_even[25]), Write(proof_p_even[27])
        )
        self.play(Write(proof_p_even[28:]))
        self.wait()
        self.play(
            *[
                ReplacementTransform(proof_p_even[pre].copy(), proof_q_even[post])
                for pre, post in zip(*changes_to_q[0])
            ]
        )
        self.wait()
        self.play(Write(proof_q_even[6]))
        self.play(
            *[
                ReplacementTransform(proof_q_even[pre].copy(), proof_q_even[post])
                for pre, post in zip(*changes_to_q[1])
            ],
            *[
                ReplacementTransform(proof_p_even[pre].copy(), proof_q_even[post])
                for pre, post in zip(*changes_to_q[2])
            ]
        )
        self.wait()
        self.play(Write(proof_q_even[16]))
        self.play(
            *[
                ReplacementTransform(proof_q_even[pre].copy(), proof_q_even[post])
                for pre, post in zip(*changes_to_q[3])
            ]
        )
        self.wait()
        self.play(Write(proof_q_even[24]))
        self.play(
            *[
                ReplacementTransform(proof_q_even[pre].copy(), proof_q_even[post])
                for pre, post in zip(*changes_to_q[4])
            ]
        )
        self.wait()
        self.play(Write(proof_q_even[31]))
        self.play(
            *[
                ReplacementTransform(proof_q_even[pre].copy(), proof_q_even[post])
                for pre, post in zip(*changes_to_q[5])
            ],
            Write(proof_q_even[33])
        )
        self.wait()
        self.play(Write(proof_q_even[36]))
        self.play(
            *[
                ReplacementTransform(proof_q_even[pre].copy(), proof_q_even[post])
                for pre, post in zip(*changes_to_q[6])
            ]
        )
        self.wait()

        self.play(
            FadeOut(proof_q_even),
            FadeOut(proof_p_even),
            *[
                ReplacementTransform(proof_p_even[pre].copy(), p_q_even[post])
                for pre, post in zip(*changes_to_qp[0])
            ],
            *[
                ReplacementTransform(proof_q_even[pre].copy(), p_q_even[post])
                for pre, post in zip(*changes_to_qp[1])
            ]
        )
        self.play(Write(p_q_even[3]))
        self.wait()
        self.play(Write(p_q_even[7]))
        self.play(
            *[
                ReplacementTransform(p_q_even[pre].copy(), p_q_even[post])
                for pre, post in zip(*changes_to_qp[2])
            ]
        )
        self.wait()
        self.play(Write(p_q_even[13]))
        self.play(
            *[
                ReplacementTransform(p_q_even[pre].copy(), p_q_even[post])
                for pre, post in zip(*changes_to_qp[3])
            ]
        )
        self.wait()


class Completude(Scene):
    def construct(self):
        self.define_hole()        
        

    def define_hole(self):
        
        # create the objects
          
        real_line = NumberLine([-10, 10], 20) # real line
        
        line_label = always_redraw( # R label
            lambda: 
                MathTex(r"\mathbb{R}").move_to(real_line.number_to_point(-6.7) + UP * 0.5)    
        ) 
        
        hole = always_redraw( # hole
            lambda:
                Circle( 
                    .05, YELLOW, fill_color = BLACK, 
                    fill_opacity = 1, stroke_width = 2
                ).move_to(real_line.number_to_point(2.3))     
        )
        
        # braces for A (left) and B(right)
        A_brace = always_redraw( # left brace
            lambda:
                BraceBetweenPoints( 
                    real_line.number_to_point(-7.5),
                    hole.get_left(),
                    direction = DOWN
                )
        )
        A_label = always_redraw( # left label
            lambda:
                MathTex("A").next_to(A_brace, DOWN, buff = SMALL_BUFF)
        )
        
        B_brace = always_redraw( # right brace
            lambda:
                BraceBetweenPoints(
                    hole.get_right(),
                    real_line.number_to_point(7.5),
                    direction = DOWN
                )
        )
        B_label = always_redraw( # right label
            lambda:
                MathTex("B").next_to(B_brace, DOWN, buff = SMALL_BUFF)
        )
        
        # Draw everything
        self.play(Create(real_line), Write(line_label))
        self.play(GrowFromCenter(hole))
        self.wait()
        self.play(
            *[GrowFromCenter(brace) for brace in [A_brace, B_brace]],
            run_time = .5,
            rate_func = linear
        )
        self.play(Write(A_label), Write(B_label))
        self.wait()
        self.play(real_line.animate.shift(DOWN))

        hole_definition = VGroup( # define a hole rigorously 
            MathTex(
                r"(1)\ ", 
                r"\forall", 
                "x", 
                r"\in",  
                "A", 
                r"\ \forall", 
                "y", 
                r"\in", 
                "B", 
                r",\  x \le y"
            ), # A is left of B
            MathTex(
                r"(2)\ ", 
                r"\neg \exists z \in \mathbb{R}\ ", 
                r"\forall", 
                "x", 
                r"\in",  
                "A", 
                r"\ \forall", 
                "y", 
                r"\in", 
                "B", 
                r",\  x \le z \le y"
            ) # No reals between A and B
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT).shift(UP * 2)
        
        x_tracker = ValueTracker(-1)
        y_tracker = ValueTracker(3)
        x_label = always_redraw( # x label
            lambda: MathTex("x").move_to(real_line.number_to_point(x_tracker.get_value())).shift(UP / 2)
        )
        y_label = always_redraw( # y label
            lambda: MathTex("y").move_to(real_line.number_to_point(y_tracker.get_value())).shift(UP / 2)
        )

        self.play(Write(hole_definition[0][0]))
        self.play(Write(x_label), Write(y_label))
        
        
        for label, set_label, offset in zip([x_label, y_label], [A_label, B_label], [1, 5]):
            self.play(
                ReplacementTransform(label.copy(), hole_definition[0][offset + 1]),
                ReplacementTransform(set_label.copy(), hole_definition[0][offset + 3]),
                Write(hole_definition[0][offset]),
                Write(hole_definition[0][offset + 2]),
            )
        
        self.play(Write(hole_definition[0][9:]))
        self.wait()

        self.play(Write(hole_definition[1][0]))
        self.play(ReplacementTransform(hole.copy(), hole_definition[1][1]),)
        self.play(
            ReplacementTransform(hole_definition[0][1:9].copy(), hole_definition[1][2:10]),
        )
        self.play(Write(hole_definition[1][10]))
        
        self.wait()
    
    def state_axiom_of_continuity(self):
        pass

    def restate_all(self):
        pass


class SupExistance(Scene):
    def construct(self):
        global theorem_count
        self.prove_existance_of_sup_and_inf()

    def prove_existance_of_sup_and_inf(self):
        hole_coord = ValueTracker(2.3)
        # A_B_distance = ValueTracker(0.)
        real_line = NumberLine([-10, 10], 20) # real line
        line_label = always_redraw( # R label
            lambda: 
                MathTex(r"\mathbb{R}").move_to(real_line.number_to_point(-6.7) + UP * 0.5)    
        )

        A_brace = always_redraw( # left brace
            lambda:
                BraceBetweenPoints( 
                    real_line.number_to_point(-7.5),
                    real_line.number_to_point(hole_coord.get_value()),
                    direction = DOWN
                )
        )
        A_label = always_redraw( # left label
            lambda:
                MathTex("A").next_to(A_brace, DOWN, buff = SMALL_BUFF)
        )
        
        B_brace = always_redraw( # right brace
            lambda:
                BraceBetweenPoints(
                    real_line.number_to_point(hole_coord.get_value()),
                    real_line.number_to_point(7.5),
                    direction = DOWN
                )
        )
        B_label = always_redraw( # right label
            lambda:
                MathTex("B").next_to(B_brace, DOWN, buff = SMALL_BUFF)
        )

        B_definition = MathTex(r"B =", r"\{y\in\mathbb{R}|\forall x \in A,\  x\le y\}").to_edge(LEFT).shift(UP * 2)

        z_exists = VGroup(
            MathTex(r"(i)\ ", r"A, B \neq \emptyset"), # A, B are not empty sets
            MathTex(r"(ii)\ ", r"\forall x \in A\ \forall y \in B,\  x \le y"), # A left of B
            VGroup(
                VGroup(Tex("Complétude", font_size=15), MathTex(r"\Longrightarrow")).arrange(DOWN, buff=SMALL_BUFF),
                MathTex(
                    r"\exists z \in \mathbb{R}\ ", r"\forall x \in A\ ", r"\forall y \in B\ ", r"x \le", "z",  r"\le y"
                )   
            ).arrange(RIGHT), # z between A and B            
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT).shift(UP * 2)


        z_maj_A = MathTex(
            r"\forall x \in A\ ", r"x \le", "z",
            r"\Rightarrow", r"z \text{\ majorant\ de\ } A", r"\Rightarrow", r"z \in B"
        )

        z_min_B = MathTex(
           r"\forall y \in B\ ", "z", r"\le y",
            r"\Rightarrow", r"z \text{\ minorant\ de\ } B"
        )

        z_sup_A = MathTex(
            r"z \in B", r"\wedge", r"z \text{\ minorant\ de\ } B",
            r"\Rightarrow", r"z = \min B",
            r"\Rightarrow", r"z = \sup A", r"\ \square"
        )

        z_min_B_reform = Tex("($z$ est le pluse petit majorant de $A$)", font_size=15)
        self.play(
            Create(real_line), Write(line_label),
        )
        
        self.wait()

        self.play(
            GrowFromCenter(A_brace),
            Write(A_label)
        )
        self.wait()

        self.play(
            GrowFromCenter(B_brace),
            Write(B_label)
        )

        self.play(Write(B_definition[0]))
        self.play(Write(B_definition[1]))
        self.wait()
        self.play(Unwrite(B_definition), run_time = .5)
        self.wait()
        self.play(real_line.animate.shift(DOWN * 2))

        self.play(Write(z_exists[:2]))
        self.wait()
        self.play(GrowFromCenter(z_exists[2][0]))
        self.wait()
        self.play(Write(z_exists[2][1]))
        self.wait()
        self.play(
            *[
                FadeOut(v, shift=LEFT) for v in [z_exists[0], z_exists[1], z_exists[2][0]]
            ],
            z_exists[2][1].animate.to_corner(UL)
        )
        z_maj_A.next_to(z_exists[2][1], DOWN).to_edge(LEFT)
        z_min_B.next_to(z_maj_A, DOWN).to_edge(LEFT)
        z_sup_A.next_to(z_min_B, DOWN).to_edge(LEFT)
        z_min_B_reform.next_to(z_sup_A[4], DOWN)

        self.wait()
        self.play(
            ReplacementTransform(z_exists[2][1][1].copy(), z_maj_A[0]),
            ReplacementTransform(z_exists[2][1][3].copy(), z_maj_A[1]),
            ReplacementTransform(z_exists[2][1][4].copy(), z_maj_A[2]),
        )
        self.wait()
        self.play(Write(z_maj_A[3:]))        
        self.wait()
        self.play(
            ReplacementTransform(z_exists[2][1][2].copy(), z_min_B[0]),
            ReplacementTransform(z_exists[2][1][4].copy(), z_min_B[1]),
            ReplacementTransform(z_exists[2][1][5].copy(), z_min_B[2]),
        )
        self.wait()
        self.play(Write(z_min_B[3:]))
        self.wait()
        self.play(
            ReplacementTransform(z_maj_A[-1].copy(), z_sup_A[0]),
            ReplacementTransform(z_min_B[-1].copy(), z_sup_A[2]),
        )
        self.play(Write(z_sup_A[1]))
        self.wait()
        self.play(Write(z_sup_A[3:5]))
        self.wait()
        self.play(Write(z_min_B_reform))
        self.play(
            Write(z_sup_A[5:-1]),
        )
        self.wait()
        self.play(Write(z_sup_A[-1]))
        self.wait()


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
        real_line = NumberLine([-.5, 3.1], 15, numbers_to_include=[0, 2]).shift(LEFT)
        self.play(Create(real_line))
        self.wait()

        A_brace = BraceBetweenPoints(real_line.number_to_point(0), real_line.number_to_point(sqrt(2)), UP)
        A_text = MathTex("A").next_to(A_brace, UP)
        A = VGroup(A_brace, A_text)
        self.play(GrowFromCenter(A[0]), Write(A[1]))
        self.wait()


        s_tracker = ValueTracker(sqrt(2.5))
        s_squared = always_redraw(
            lambda: VGroup(
                MathTex("s^2", font_size=30),
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1)
            ).arrange(UP, buff=SMALL_BUFF).next_to(real_line.number_to_point(s_tracker.get_value() ** 2), DOWN, buff=0)
        )
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


class ArchimedeanProperty(Scene):
    def construct(self):
        # self.illustrate_archimedean_property()
        self.state_theorem()
        # self.prove_archimedean_property()

    def illustrate_archimedean_property(self):
        # x
        x_length = ValueTracker(1 / sqrt(5)) # length of x
        x_segment = always_redraw(lambda : NumberLine([0, 1], x_length.get_value()).to_edge(LEFT).shift(UP / 2)) # x segment
        x_label = always_redraw(lambda: MathTex("x").next_to(x_segment, UP, buff = SMALL_BUFF)) # x label
        x = VGroup(x_segment, x_label) # group everything together
        
        # y
        y_length = ValueTracker(2) # length of y
        y_segment = always_redraw(lambda : NumberLine([0, 1], y_length.get_value()).to_edge(LEFT)) # y segment
        y_label = always_redraw(lambda: MathTex("y").next_to(y_segment, DOWN, buff = SMALL_BUFF)) # y label
        y = VGroup(y_segment, y_label) # group everything together
        
        self.play(
            Create(x_segment),
            Create(y_segment),
            Write(x_label),
            Write(y_label),
        )
        self.wait()
            
        xs_group = always_redraw(
            lambda:
                VGroup(
                *[
                    x_segment.copy().shift(x_length.get_value() * RIGHT * i) 
                    for i in range(int(y_length.get_value() / x_length.get_value()) + 1)
                ]
            )
        )
        for i in range(1, len(xs_group)):
            self.play(
                ReplacementTransform(xs_group[i - 1].copy(), xs_group[i]),
                )
            self.wait()

        self.play(*[FadeOut(o) for o in self.mobjects])
        self.wait()


        # Theorem statement
        # global chapter
        # global theorem_count
        # theorem = VGroup(
        #     Tex(f"Théorème {chapter}.{theorem_count}"),
        #     Tex("Soient $x > 0$ et $y \\in \\mathbb{R}$"),
        #     MathTex(r"\exists n \in \mathbb{N}, \quad nx > y")
        # ).arrange_submobjects(DOWN, aligned_edge=LEFT).to_edge(RIGHT)
        # for line in theorem:
        #     self.play(Write(line))

        # self.play(Write(SurroundingRectangle(theorem, color=WHITE)))
        # self.wait()
        # self.play(
        #     *[FadeOut(o) for o in self.mobjects + [x_segment]]
        # )
        # self.clear()
        # self.wait()
        
    def prove_archimedean_property(self):
        font_size = 40
        
        initial_assumption = VGroup(
            Tex(r"Soient $x > 0$ et $y \in \mathbb{R}$, ", r"si $y \le 0$, on prends $n = 1$."),
            Tex(r"Sinon, supposons que $x > 0$ et $y > 0$ sont un contre-exemple."),
            VGroup(Tex(r"càd:"), MathTex(r"\forall n \in \mathbb{N}\ nx \le y")).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)

        proof = VGroup(
            MathTex(r"\forall n \in \mathbb{N}\ nx \le y"),
            Tex(r"Autrement dit, ", "$y$ est un majorant de ", r"$A = \{nx| n\in \mathbb{N}\}$"),
            MathTex(r"\text{Posons }", "s","=", r"\sup A", r"\text{,\ le\ lémme\ de sup nous\ garentie\ que:}"), 
            MathTex(r"\forall",  r"\varepsilon", "> 0", r", \exists n \in \mathbb{N}\ s-\varepsilon \le nx"),
            MathTex(
                r"\text{Si on prend } \varepsilon = x\text{, on a: }", 
                "s", "-", "x",  r"\le",  "n_0", "x", 
                r"\text{, pour un certain } n_0\in\mathbb{N}."
            ),
            MathTex(r"\text{Donc: }", "s", r"\le", "(", "n_0", "+", "1", ")", "x"),
            MathTex(
                r"\text{Or, }", "(", "n_0", "+", "1", ")", "x", r"\in A.", 
            ),
            MathTex(r"\text{Ceci est absurde car }", "s", r"\text{ est un majorant de } ", "A.", r"\square")
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        for line in initial_assumption:
            for component in line:
                self.play(Write(component))
                self.wait()

        self.play(
            *[FadeOut(c) for c in list(initial_assumption) if c != initial_assumption[-1][-1]],
            ReplacementTransform(initial_assumption[-1][-1].copy(), proof[0]),
        )
        self.wait()
        self.play(Write(proof[1][0]))
        self.play(Write(proof[1][1:]))
        self.wait()
        self.play(Write(proof[2][:4]))
        self.wait(.5)
        self.play(Write(proof[2][4:]))
        self.wait()
        self.play(Write(proof[3][:3]))
        self.play(Write(proof[3][3:]))
        self.wait()
        self.play(Write(proof[4][0]))
        self.wait(.5)
        self.play(Write(proof[4][1:7]))
        self.wait(.5)
        self.play(Write(proof[4][7:]))
        self.wait()
        self.play(Write(proof[5][0]))
        self.wait()
        self.play(
            *[
                ReplacementTransform(proof[4][i+1].copy(), proof[5][j+1])
                for i, j in zip([0, 3, 4, 1, 2, 5], [0, 1, 3, 4, 5, 7])
            ], 
            Write(proof[5][3]),
            Write(proof[5][7]),
        )
        self.wait()
        self.play(Write(proof[6][0]))
        self.wait(.5)
        self.play(
            *[
                ReplacementTransform(proof[5][i].copy(), proof[6][j])
                for i, j in zip(list(range(3, 9)), list(range(1, 7)))
            ],
            Write(proof[6][7]),
        )
        self.wait()
        self.play(Write(proof[7][:-1]))
        self.wait()
        self.play(Write(proof[7][-1]))
        self.wait()
        
        

    def state_theorem(self):
        theorem = Theorem(
            title="Archimède",
            body=VGroup(
                Tex(r"Soient $x > 0$ et $y \in \mathbb{R}$, ", r"il existe $n \in \mathbb{N}$ tel que $nx > y$", r". càd: "),
                MathTex(r"\forall x > 0\ \forall y \in \mathbb{R}\ \exists n \in \mathbb{N}\ nx > y"),
            ).arrange(DOWN).to_edge(LEFT)
        ) 
        

        self.play(Write(theorem))
        self.play(Write(SurroundingRectangle(theorem, color=WHITE)))
        self.wait()
        self.play(*[FadeOut(o) for o in self.mobjects])
        self.wait()


class QDense(Scene):
    def construct(self):
        self.prove_Q_dense()

        
    def prove_Q_dense(self):
        real_line = NumberLine([-2, 2], 15) # real line
        line_label = always_redraw( # R label
            lambda: 
                MathTex(r"\mathbb{R}").move_to(real_line.number_to_point(-1.8) + UP * 0.5)    
        )
        x_tracker = ValueTracker(.2) # x tracker
        y_tracker = ValueTracker(.7) # y tracker
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
        not_q = int(np.abs(1 / (y_tracker.get_value() - x_tracker.get_value())))
        qx_label = always_redraw(
            lambda: VGroup(
                MathTex(
                    "qx", font_size=30, tex_to_color_map={"q":YELLOW}
                ).next_to(real_line.number_to_point(not_q * x_tracker.get_value()), UP, buff = SMALL_BUFF),
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point(x_tracker.get_value() * not_q), DOWN, buff=0)
            )
        )
        qy_label = always_redraw(
            lambda: VGroup(
                MathTex(
                    "qy", font_size=30, tex_to_color_map={"q": YELLOW}
                ).next_to(real_line.number_to_point(not_q * y_tracker.get_value()), UP, buff = SMALL_BUFF),
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point(y_tracker.get_value() * not_q), DOWN, buff=0)
            )
        )
        p_label = always_redraw(
            lambda: MathTex("p", font_size=30).set_color(YELLOW).next_to(real_line.number_to_point(int(not_q * y_tracker.get_value())), UP, buff = SMALL_BUFF)
        )
        p_over_q_label = always_redraw(
            lambda: VGroup(
                Triangle(stroke_width=0, fill_color=WHITE, fill_opacity=1).scale(.1).set_color(YELLOW),
                MathTex(r"p\over q", font_size=30).set_color(YELLOW)
            ).arrange(DOWN, buff=SMALL_BUFF).next_to(real_line.number_to_point(int(not_q * y_tracker.get_value()) / not_q), DOWN, buff=0)
        )

        inQ = always_redraw(
            lambda: MathTex(r"\in \mathbb{Q}", font_size=30).next_to(p_over_q_label, RIGHT, buff=SMALL_BUFF)
        )

        q_exists = MathTex(
            r"\exists q \in \mathbb{N}\ ", "q", "(", "y", "-", "x", ")", "> 1",
            r"& \Rightarrow ", "q", "y", "-", "q", "x", "> 1", 
            r"\\ & \Rightarrow", r"\exists p \in \mathbb{Z}\ ", "q", "x", "<", "p", "<", "q", "y",
            r"\\ & \Rightarrow", r"x", "<", "{p \over q}",  "<",  "y", r"\ \square",
        ).to_corner(UL)


        changes = [
            [
                (1, 3, 4, 1, 5, 7),
                (9, 10, 11, 12, 13, 14)
            ],
            [
                (17, 18, 19, 20, 22),
                (25, 26, 27, 28, 29)
            ]
        ]
        self.play(
            Write(real_line),
            Write(line_label),
        )
        self.wait()
        self.play(
            Write(x_label[0]),
            GrowFromCenter(x_label[1]),
            Write(y_label[0]),
            GrowFromCenter(y_label[1])
        )
        self.play(Write(q_exists[:8]))
        self.wait()
        self.play(Write(q_exists[8]))
        self.play(
            ReplacementTransform(x_label, qx_label),
            ReplacementTransform(y_label, qy_label),
            *[
                ReplacementTransform(q_exists[pre].copy(), q_exists[post])
                for pre, post in zip(*changes[0])
            ]
        )
        self.wait()
        self.play(Write(p_label), Write(q_exists[15:24]))
        self.wait()
        self.play(
            ReplacementTransform(p_label, p_over_q_label),
            ReplacementTransform(qx_label, x_label),
            ReplacementTransform(qy_label, y_label),
            Write(q_exists[24]),
            *[
               ReplacementTransform(q_exists[pre].copy(), q_exists[post])
                for pre, post in zip(*changes[1])
            ],    
        )
        self.play(Write(inQ))
        self.play(Write(q_exists[-1]))
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



