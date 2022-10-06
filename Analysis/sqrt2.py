from manim import *

class Sqrt2Irrational(Scene):
    def construct(self):
        big_square = Square(4, color=BLUE, fill_opacity=.5).shift(LEFT*2)
        small_squares = VGroup(
            Square(2.5, color=GREEN, fill_opacity=.5),
            Square(2.5, color=GREEN, fill_opacity=.5)
        ).arrange(DOWN).shift(RIGHT*2)

        self.play(
            *[
                DrawBorderThenFill(s) for s in 
                [big_square, small_squares[0], small_squares[1]]    
            ]
        )
        
        
        self.wait()
        
        big_brace = Brace(big_square, LEFT)
        self.play(GrowFromCenter(big_brace))
        self.wait()
        