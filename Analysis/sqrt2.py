from manim import *

class Sqrt2Irrational(Scene):
    def construct(self):
        big_square = Square(4, color=BLUE, fill_opacity=.2)
        A, B, C, D = big_square.get_vertices()
        self.play(DrawBorderThenFill(big_square))
        
        self.wait()
        
        sub_squares = VGroup(
            SquareInSquare(big_square, A, .75, fill_color=RED, fill_opacity=.2),
            SquareInSquare(big_square, C, .75, fill_color=RED, fill_opacity=.2) 
        )

        self.play(DrawBorderThenFill(sub_squares))
        self.wait()


class SquareInSquare(Polygon):
    def __init__(
        self, 
        square:Square, 
        corner:np.ndarray, 
        proportion, 
        **kwargs
    ):

        sc = corner * proportion
        A, B, C, D = square.get_vertices() * proportion
        
        if np.array_equal(B, sc): 
            B, C, D = [C, D, A]
        elif np.array_equal(C, sc): 
            B, C, D = [D, A, B]
        elif np.array_equal(D, sc): 
            B, C, D = [A, B, C]
        
        A = corner * (1 - proportion)

        Polygon.__init__(self, corner, A+B, A+C, A+D, **kwargs)

        