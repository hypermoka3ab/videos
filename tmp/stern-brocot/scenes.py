from itertools import product
from manim import *
from utils import *

class MinkowskiQuestionMark(Scene):

    def continued_fraction(self, x:float, n_levels:int=10) -> list:
        q = np.floor(x)
        result = [q]
        x -= q
        for _ in range(n_levels):
            if x == 0: break
            q = np.floor(1/x)
            result.append(q)
            x = 1 / x - q
        return result

    def question_mark(self, x:float, n_levels:int) -> float:
        a = self.continued_fraction(x, n_levels)
        return a[0] + sum(
            (-1) ** (n + 1) / 2 ** sum(a[:n+1]) for n in range(1, len(a)+1)
        ) * 2

    def construct(self):
        n_levels = 1
        ax = Axes([-.2, 1, .2], [-.2, 1, .2], tips=False, axis_config={'include_numbers': True})
        self.play(Write(ax))
        qst = ax.plot(lambda t: self.question_mark(t, n_levels), [.0001, .9999, .0001], color=RED)
        self.play(Create(qst))
        for _ in range(10):
            n_levels += 1
            self.play(Transform(qst, ax.plot(lambda t: self.question_mark(t, n_levels), [.01, .99, .001], stroke_width=1, color=RED)))
            self.wait()


class RationalGrid(Scene):
    def construct(self):
        grid = NumberPlane([-3, 12], [-3, 6], axis_config={"include_numbers": True})
        self.play(Create(grid))
        self.wait()
        
        lattice_points = VGroup(
            *[
                Dot(grid.c2p(x, y), color=YELLOW, radius=.06)
                for x, y in product(
                    range(grid.x_range[1]), range(grid.y_range[1])
                )
            ]
        )
        self.play(*[GrowFromCenter(point) for point in lattice_points])
        self.play(
            DrawBorderThenFill(
                Parallelogram((3, 2), (2, 1), coord_system=grid, stroke_width=2, fill_opacity=.2)
            )
        )
        self.wait()