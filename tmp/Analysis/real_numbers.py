from manim import *

class Axioms(Scene):
    def construct(self):
        axioms = MathTex(
            r"1-\ \forall x, y \in \mathbb{R},\ x + y = y + x",
            r"1-\ \forall x, y \in \mathbb{R},\ x \cdot y = y \cdot x",
        ).align_submobjects(LEFT)

        self.play(Write(axioms))
        self.wait(2)

class Continuity(Scene):
    def construct(self):
        """
        """

        real_line = NumberLine([-10, 10], 20)
        line_label = MathTex(r"\mathbb{R}").to_edge(edge = LEFT, buff = SMALL_BUFF).shift(UP * .5)
        hole = Circle(
            .05, WHITE, fill_color = BLACK, 
            fill_opacity = 1, stroke_width = 1
        ).move_to(real_line.number_to_point(2.3))
        
        left_brace = BraceBetweenPoints(
            real_line.get_left(),
            hole.get_left(),
            direction = DOWN
        )
        A_label = MathTex("A").next_to(left_brace, DOWN, buff = SMALL_BUFF)


        right_brace = BraceBetweenPoints(
            hole.get_right(),
            real_line.get_right(),
            direction = DOWN
        )
        B_label = MathTex("B").next_to(right_brace, DOWN, buff = SMALL_BUFF)
        
        self.play(Create(real_line), Write(line_label))
        
        self.play(GrowFromCenter(hole))
        self.wait()

        self.play(
            *[GrowFromCenter(brace) for brace in [left_brace, right_brace]],
            run_time = .5,
            rate_func = linear
        )
        self.play(Write(A_label), Write(B_label))
        self.wait()