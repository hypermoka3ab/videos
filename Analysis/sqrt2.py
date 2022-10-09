from manim import *

class Sqrt2Irrational(Scene):
    def construct(self):
        BIG_COLOR = "#76de1b"
        SMALL_COLOR = "#ee4f4f"
        SMALLEST_COLOR ="#0a86eb"
        MED_COLOR = "#b26238"
        ALPHA = .7

        big_square = Square(
            4, color=BIG_COLOR, 
            fill_opacity=.6, stroke_width=0
        ).to_edge(LEFT)
        A, B, C, D = big_square.get_vertices()
        
        Ap, Dp = (A + B * 3) / 4, (A + D * 3) / 4
        Bp, Cp = (B * 3 + C) / 4, (C + D * 3) / 4
        E = Ap + Dp - A
        F = Bp + Cp - C
        Ep = Cp + Dp - D
        Fp = Ap + Bp - B

        nested_squares = VGroup(
            big_square,
            Polygon(A, Ap, E, Dp, color=SMALL_COLOR, fill_opacity=.4, stroke_width=0),
            Polygon(F, Bp, C, Cp, color=SMALL_COLOR, fill_opacity=.4, stroke_width=0),
            Polygon(Ap, B, Bp, Fp, color=SMALLEST_COLOR, fill_opacity=.4, stroke_width=0),
            Polygon(Dp, Ep, Cp, D, color=SMALLEST_COLOR, fill_opacity=.4, stroke_width=0),
        )
        
        small_square = nested_squares[1].copy().next_to(big_square, RIGHT)
        
        self.play(
            DrawBorderThenFill(big_square),
            DrawBorderThenFill(small_square)
        )

        self.wait()

        self.play(
            ReplacementTransform(small_square, nested_squares[1]),
            ReplacementTransform(small_square.copy(), nested_squares[2]),
        )
        self.wait()

        self.play(DrawBorderThenFill(nested_squares[-2:]))
        self.wait()

        small_union = Polygon(
            A, Ap, Fp, Bp, C, Cp, Ep, Dp, 
            color=SMALL_COLOR, fill_opacity=.4, 
            stroke_width=0
        )

        proof = VGroup(
            big_square.copy().scale(.3),
            MathTex("-"),
            VGroup(*nested_squares[-2:].copy().scale(.3)).arrange(DOWN),
            MathTex("="),
            small_union.copy().scale(.3),
            MathTex("="),
            VGroup(*nested_squares[1:3].copy().scale(.3)).arrange(DOWN),
            MathTex("-"),
            Polygon(F, Fp, E, Ep, color=MED_COLOR, fill_opacity=.4, stroke_width=0).copy().scale(.3)
        ).arrange(RIGHT).next_to(big_square, RIGHT)
        
    
        self.play(ReplacementTransform(small_union, proof[4]))
        self.play(Write(proof[3]), Write(proof[-4]))
        self.wait()

        self.play(
            *[
                ReplacementTransform(pre.copy(), post) for pre, post
                in zip(
                    [
                        big_square, *nested_squares[-2:], *nested_squares[1:3], Polygon(
                            F, Fp, E, Ep, color=MED_COLOR, fill_opacity=.4, stroke_width=0
                        )
                    ],
                    [proof[0], *proof[2], *proof[-3], proof[-1]]
                )
            ], Write(proof[1]), Write(proof[-2])
        )
        self.wait()

        conclusion = VGroup(
            proof[2].copy().scale(1/.3), 
            MathTex("="),
            proof[-1].copy().scale(1/.3) 
        ).arrange(RIGHT)

        self.play(TransformMatchingShapes(proof, conclusion))
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

        