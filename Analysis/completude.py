from manim import *
chapter = 1
class Completude(Scene):
    def construct(self):  
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


        A_left_B = MathTex(
           r"(1)\ ", r"\forall x \in A, ",
           r"\forall y \in B, ", r"x \le y"
        )

        nothing_between = MathTex(
            r"(2)\ ", r"\neg \exists z \in \mathbb{R}, ", 
            r"\forall x \in A, ", 
            r"\forall y \in B, ", 
            r"x \le z \le y"
        )
        VGroup( # define a hole rigorously 
            A_left_B, nothing_between
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT).shift(UP * 2)
        
        
        x_label = always_redraw( # x label
            lambda: MathTex("x").move_to(real_line.number_to_point(-1)).shift(UP / 2)
        )
        y_label = always_redraw( # y label
            lambda: MathTex("y").move_to(real_line.number_to_point(3)).shift(UP / 2)
        )

        self.play(Write(A_left_B[0]))
        self.play(Write(x_label), Write(y_label))
        
        
        self.play(
            ReplacementTransform(x_label.copy(), A_left_B[1]),
            ReplacementTransform(y_label.copy(), A_left_B[2])
        )
        
        self.play(Write(A_left_B[3:]))
        self.wait()

        self.play(Write(nothing_between[0]))
        self.play(
            Write(nothing_between[1]),
            TransformMatchingShapes(
                A_left_B[1:].copy(),
                nothing_between[2:]
            )
        )

        self.wait()
        
        axiom = MathTex(
            r"\forall A, B \in \mathcal{P}(\mathbb{R}),\ ",
            r"(\forall x \in A, \forall y \in B, x \le y)", r"\Rightarrow",
            r"(\exists z \in \mathbb{R}, \forall x \in A, \forall y \in B, x \le z \le y)",
            font_size=35,
        ).shift(UP)

        self.play(
            TransformMatchingShapes(A_left_B[1:], axiom[1]),
            TransformMatchingShapes(nothing_between[1:], axiom[3]),
            FadeOut(A_left_B[0], nothing_between[0]), 
            Write(axiom[2])
        )

        self.wait()

        self.play(Write(axiom[0]))
        self.wait()


class SupExistance(Scene):
    def construct(self):
        from theorems import Theorem
        theroem = Theorem(
            title="La propriété de la borne supérieure",
            body=Tex(
                r"Si \(A\) est une partie non vide est majorée de \(\mathbb{R}\), ",
                r"alors \(A\) admet\\ une unique borne spérieure.",
                tex_environment=None
            )
        )

        self.play(Write(theroem.title))
        self.wait()
        self.play(Write(theroem.body))
        self.wait()

        self.play(FadeOut(theroem))
        self.wait()
       
        self.prove_existance_of_sup_and_inf()

    def prove_existance_of_sup_and_inf(self):
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"\usepackage{mathtools}")

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
        
            MathTex(
                r"\xRightarrow{\text{Complétude}}",
                r"\exists z \in \mathbb{R}\ ", r"\forall x \in A\ ", r"\forall y \in B\ ", r"x \le", "z",  r"\le y",
                tex_template=tex_template
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

        z_min_B_reform = Tex("($z$ est le pluse petit majorant de $A$)", font_size=30)
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
        self.play(Write(z_exists[2][1:]))
        self.wait()
        self.play(
            *[
                FadeOut(v, shift=LEFT) for v in [z_exists[0], z_exists[1], z_exists[2][0]]
            ],
            z_exists[2][1:].animate.to_corner(UL)
        )
        z_maj_A.next_to(z_exists[2][1], DOWN).to_edge(LEFT)
        z_min_B.next_to(z_maj_A, DOWN).to_edge(LEFT)
        z_sup_A.next_to(z_min_B, DOWN).to_edge(LEFT)
        z_min_B_reform.next_to(z_sup_A[4], DOWN)

        self.wait()
        self.play(
            ReplacementTransform(z_exists[2][1].copy(), z_maj_A[0]),
            ReplacementTransform(z_exists[2][3].copy(), z_maj_A[1]),
            ReplacementTransform(z_exists[2][4].copy(), z_maj_A[2]),
        )
        self.wait()
        self.play(Write(z_maj_A[3:]))        
        self.wait()
        self.play(
            ReplacementTransform(z_exists[2][2].copy(), z_min_B[0]),
            ReplacementTransform(z_exists[2][4].copy(), z_min_B[1]),
            ReplacementTransform(z_exists[2][5].copy(), z_min_B[2]),
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

