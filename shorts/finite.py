from manim import *
from itertools import product

config.pixel_height = 1920
config.pixel_width = 1080

class Finite(Scene):

    def construct(self):
        self.add_sound("assets/sounds/finite/second.mp3")
        # self.add_sound("assets/sounds/finite/Centroid.mp3")
        template = TexTemplate()
        template.add_to_preamble("\\usepackage{stmaryrd}")

        what_is_infinite = Tex("What is ", "a", "n in", "finite ", " set", "?").scale(2)
        what_is_finite = Tex("What is ", "a", " ", "finite ", " set", "?").scale(2)
        self.add(what_is_infinite)
        self.wait(5)
        self.play(
            ReplacementTransform(what_is_infinite, what_is_finite),
        )
        self.play(FadeOut(what_is_finite))

        e_equals_list = MathTex("E", " = ", r"\{", "x_1",", ", "x_2", ", ", r"\cdots, ", "x_n", r"\}").scale(2)
        self.wait(1)
        self.play(Write(e_equals_list[:3]), Write(e_equals_list[-1]))
        for mob in e_equals_list[3:-1]:
            self.play(Write(mob))

        self.wait()

        map_to_ints = VGroup(
            *[
                MathTex(mob) for l in
                np.array(
                    [
                        ["x_1", "x_2", "\\vdots", "x_n"],
                        ["\\mapsto", "\\mapsto", "\\vdots", "\\mapsto"],
                        ["1", "2", "\\vdots", "n"],
                    ] 
                ).T.tolist() for mob in l
            ]
        ).arrange_in_grid(rows=4, cols=3, buff=MED_LARGE_BUFF).scale(2)
        
        self.play(
            *[
                ReplacementTransform(e_equals_list[i], map_to_ints[j]) for i, j in zip(
                    (3, 5, 7, 8),
                    (0, 3, 6, 9)
                ) 
            ],
            *[FadeOut(e_equals_list[i]) for i in (0, 1, 2, 4, 6, 9)]
        )
        self.wait()
        self.play(
            *[
                ReplacementTransform(map_to_ints[i*3].copy(), map_to_ints[i*3+2]) for i in range(4)
            ],
            *[GrowFromEdge(map_to_ints[i*3+1], LEFT) for i in range(4)]
        )
        self.wait()

        f_map = MathTex("f:", "E", "\\rightarrow", "\\{1, 2, \\cdots, n\\}").scale(2).to_edge(LEFT).shift(UP*5)
        self.play(Write(f_map[0]))
        self.play(
            *([
                
                ReplacementTransform(map_to_ints.submobjects[i*3+j], f_map[j+1]) for i, j in product(
                    (0, 1, 3), range(3)
                )
            ] + [FadeOut(map_to_ints[i+6]) for i in range(3)]),
        )

        f_map_interval = MathTex(
            "f:", "E", "\\rightarrow", "\\llbracket 1, n\\rrbracket",
            tex_template=template
        ).scale(2).to_edge(LEFT).shift(UP*5)
        self.play(
            ReplacementTransform(f_map[-1], f_map_interval[-1]),
        )
        self.remove(f_map)
        self.add(f_map_interval)
        self.wait()

        injective = MathTex(r"\forall i\neq j,\ ", r"f(i)\neq f(j)").scale(2).shift(UP/2)
        for mob in injective: self.play(Write(mob))

        self.wait()

        surjective = MathTex(
            r"\forall i\in\ \llbracket 1, n\rrbracket, ", r"\exists x\in\ E,\ ", r"f(x)=i",
            tex_template=template
        ).scale(2).next_to(injective, DOWN, buff=MED_LARGE_BUFF)
        for mob in surjective: 
            self.play(Write(mob))
            self.wait(.5)
        self.wait(8)

        self.play(FadeOut(injective), FadeOut(surjective))
        e_is_finite = Tex("E is finite").scale(2).to_edge(RIGHT).shift(UP*5)
        self.play(Write(e_is_finite))
        iff = MathTex(r"\Leftrightarrow").scale(2).move_to(
            (e_is_finite.get_left() + f_map_interval.get_right()) / 2
        )
        self.play(Write(iff))
        conclusion = VGroup(e_is_finite, iff, f_map_interval)
        self.play(
            conclusion.animate.move_to(ORIGIN),
            conclusion.animate.set_color(YELLOW)
        )
        
        self.wait()