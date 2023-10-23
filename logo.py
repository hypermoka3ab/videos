from itertools import product

from manim import *
from themes.dracula import dracula

dracula.set()


class Logo(Scene):
    def construct(self):
        logo = self.logo()
        logo.rotate(-PI / 2)
        self.wait()
        self.play(FadeIn(logo), logo.animate.rotate(PI / 2), run_time=2)
        self.wait()

        # point = Dot(ORIGIN)
        # segment = VGroup(
        #     Dot(RIGHT),
        #     Dot(LEFT),
        #     Line(LEFT, RIGHT)
        # )
        # square = VGroup(
        #     Dot(UR), Dot(UL), Dot(DL), Dot(DR),
        #     Line(UR, UL), Line(UL, DL),
        #     Line(DL, DR), Line(DR, UR)
        # )
        # self.play(GrowFromCenter(point))
        # self.wait()
        # self.play(ReplacementTransform(point, segment))
        # self.wait()
        # self.play(ReplacementTransform(segment, square))
        # self.wait()

    def adjascency_matrix(self, n=4):
        q = np.zeros((1, 1))
        for k in range(n):
            i = np.identity(2**k)
            q = np.hstack(
                (
                    np.vstack((q, i)),
                    np.vstack((i, q)),
                )
            )
        return q

    def logo(self):
        matrix = self.adjascency_matrix()
        order = [0, 1, 3, 7, 15, 14, 12, 8, 9, 2, 5, 11, 6, 13, 10, 4]
        dots = VGroup(
            *[Dot(ORIGIN) for _ in range(16)],
        )
        for i in range(16):
            r = 3 if i < 8 else 1
            dots[i] = Dot(
                complex_to_R3(r * np.exp(TAU * 1j * i / 8)),
                fill_opacity=1,
                fill_color="#ffb86c" if is_odd(order[i]) else "#50fa7b",
                radius=0.15,
            )
        lines = VGroup(
            *[
                Line(dots[i].get_center(), dots[j].get_center(), stroke_color="#bd93f9")
                for i, j in product(range(16), range(16))
                if matrix[order[i], order[j]]
            ]
        ).set_z_index(-1)

        return VGroup(lines, dots)


def is_odd(n):
    parity = 0
    while n:
        parity = ~parity
        n = n & (n - 1)
    return parity == 0
