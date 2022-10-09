from manim import *

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
        hole_definition = VGroup( # define a hole rigorously 
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
            r"\forall A, B \in \mathcal{P}(\mathbb{R})\setminus\{\emptyset\},\ ",
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
