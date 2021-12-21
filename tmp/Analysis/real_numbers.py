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
            self.wait()
            rect = SurroundingRectangle(self.axioms[i])
            
            self.play(
                self.axioms[i].animate.set_color(YELLOW),
                Write(rect), 
                run_time=2
            )
            self.play(
                Unwrite(rect), 
                self.axioms[i].animate.set_color(WHITE),
                run_time=2
            )
            

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


class Sup(Scene):
    def construct(self):
        global theorem_count
        self.prove_existance_of_sup_and_inf()
        # self.caracterize_sup_and_inf()
        # self.prove_caracterization()


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
                    r"\exists z \in \mathbb{R}\ ", 
                    r"\forall", 
                    "x", 
                    r"\in",  
                    "A", 
                    r"\ \forall", 
                    "y", 
                    r"\in", 
                    "B", 
                    r",\ ", r"x \le",  "z", r"\le y"
                )   
            ).arrange(RIGHT), # z between A and B            
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT).shift(UP * 2)


        z_maj_A = MathTex(
            r"\forall", r"x", r"\in", "A", r"\ ", r"x \le", "z",
            r"\Rightarrow", r"z \text{\ majorant\ de\ } A", r"\Rightarrow", r"z \in B"
        )

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
        self.wait()
        self.play(
            *[
                ReplacementTransform(z_exists[2][1][i + 1].copy(), z_maj_A[i]) for i in range(4)
            ],
            ReplacementTransform(z_exists[2][1][-3].copy(), z_maj_A[5]),
            ReplacementTransform(z_exists[2][1][-2].copy(), z_maj_A[6]),
        )
        self.wait()
        self.play(Write(z_maj_A[7:]))        


    def caracterize_sup_and_inf(self):
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
            MathTex(r"(ii) \quad", r" \forall \varepsilon > 0\ \exists x \in A\ \lambda \ < x + \varepsilon"),
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

    def prove_caracterization(self):
        
        
        
        proof = VGroup(
            *[
                Tex(r"\emph{Démonstration.}"),
                MathTex(r"(i) \Rightarrow (ii):", color = BLUE),
                Tex(r"Posons $\lambda = \sup A$ et soit $\varepsilon > 0$."),
                MathTex(
                    r"\lambda - \varepsilon < \lambda &\Rightarrow \lambda - \varepsilon\ \mathrm{n'est\ pas\ un\ majorant\ de}\ A.\\", 
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


class ArchimedeanProperty(Scene):
    def construct(self):
        # self.illustrate_archimedean_property()
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

        # suppose counterexample

        #x
        x_length = ValueTracker(1 / sqrt(5)) # length of x
        x_segment = always_redraw(lambda : NumberLine([0, 1], x_length.get_value()).to_edge(LEFT).shift(UP / 2)) # x segment
        x_label = always_redraw(lambda: MathTex("x").next_to(x_segment, UP, buff = SMALL_BUFF)) # x label
        x = VGroup(x_segment, x_label) # group everything together
        
        # y
        y_length = ValueTracker(2.5) # length of y
        y_segment = always_redraw(lambda : NumberLine([0, 1], y_length.get_value()).to_edge(LEFT)) # y segment
        y_label = always_redraw(lambda: MathTex("y").next_to(y_segment, DOWN, buff = SMALL_BUFF)) # y label
        y = VGroup(y_segment, y_label) # group everything together

        xs = VGroup(
            x_segment.copy(), 
            x_segment.copy().shift(x_length.get_value() * RIGHT), 
            MathTex("\\cdots").next_to(x_segment, buff=.1).shift(x_length.get_value() * RIGHT), 
            x_segment.copy().shift((x_length.get_value() + .1) * 3 * RIGHT)
        )

        self.play(Write(y), Write(x))
        
        for i in range(1, len(xs)):
            self.play(
                ReplacementTransform(xs[i - 1].copy(), xs[i]),
            )
        self.wait()
        
        brace = Brace(xs, UP, .5)
        nx = MathTex("nx").next_to(brace, UP)
        self.play(Write(brace), Write(nx))
        self.wait()




