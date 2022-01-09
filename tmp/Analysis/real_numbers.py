from math import sqrt
from manim import *
chapter = "I"
global theorem_count 
theorem_count = 1

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
        self.illustrate_archimedean_property()
        self.state_theorem()
        self.prove_archimedean_property()

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
        theorem = VGroup(
            Tex("Théorème"),
            Tex(r"Soient $x > 0$ et $y \in \mathbb{R}$, ", r"il existe $n \in \mathbb{N}$ tel que $nx > y$", r". càd: "),
            MathTex(r"\forall x > 0\ \forall y \in \mathbb{R}\ \exists n \in \mathbb{N}\ nx > y"),
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT)
        theorem[-1].shift(RIGHT * 3)

        self.play(Write(theorem))
        self.play(Write(SurroundingRectangle(theorem, color=WHITE)))
        self.wait()
        self.play(*[FadeOut(o) for o in self.mobjects])
        self.wait()


class QDesnse(Scene):
    def construct(self):
        self.prove_Q_dense()

        
    def prove_Q_dense(self):
        real_line = NumberLine([-4, 4], 15) # real line
        line_label = always_redraw( # R label
            lambda: 
                MathTex(r"\mathbb{R}").move_to(real_line.number_to_point(-3.6) + UP * 0.5)    
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
            r"\\ & \Rightarrow", r"x < {p\over q} < y",
            tex_to_color_map={"q": YELLOW, "p": YELLOW}
        ).to_corner(UL)

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
        self.play(Write(q_exists[:10]))
        self.wait()
        self.play(Write(q_exists[10]))
        self.play(
            ReplacementTransform(x_label, qx_label),
            ReplacementTransform(y_label, qy_label),
            ReplacementTransform(q_exists[1].copy(), q_exists[11]),
            ReplacementTransform(q_exists[3].copy(), q_exists[12]),
            ReplacementTransform(q_exists[4].copy(), q_exists[13]),
            ReplacementTransform(q_exists[1].copy(), q_exists[14]),
            ReplacementTransform(q_exists[5].copy(), q_exists[15]),
            ReplacementTransform(q_exists[10].copy(), q_exists[16]),
        )
        self.wait()
        self.play(Write(p_label), Write(q_exists[17:28]))
        self.wait()
        self.play(
            ReplacementTransform(p_label, p_over_q_label),
            ReplacementTransform(qx_label, x_label),
            ReplacementTransform(qy_label, y_label),
            Write(q_exists[28:]),
        )
        self.play(Write(inQ))
        self.wait()


