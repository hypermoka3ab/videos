from manimlib.imports import *

class Cantor(Scene):
    def construct(self):
        #self.add_sound("test")
        self.introduction()
        self.positionDuProblème()


    def introduction(self):
        Cantor = ImageMobject("cantor").scale(2)
        Russel = ImageMobject("Russel").scale(2).to_edge(LEFT)
        Godel = ImageMobject("Godel").scale(2)
        Turing = ImageMobject("Turing").scale(2).to_edge(RIGHT)

        self.play(FadeIn(Cantor))
        self.wait()
        self.play(FadeOut(Cantor))
        for o in Russel, Godel, Turing:
            self.play(FadeIn(o))
            self.wait()
        

    def positionDuProblème(self):
        pass

    def réponse(self):
        pass

class Thumbnail(Scene):
    def construct(self):
        grid = TexMobject(
            r"""
            \begin{array}{c c c c c c}
                0 & \rightarrow & 0 & 1 & 0 & \cdots \\
                1 & \rightarrow & 0 & 1 & 1 & \cdots \\
                2 & \rightarrow & 1 & 1 & 0 & \cdots \\
                \vdots & \vdots & \vdots & \vdots & \vdots & \ddots 
            \end{array}
            """ 
        ).set_color(BLUE).scale(2)
        for i in [0, 8, 16, 24, 25, 26]:
            grid[0][i].set_color(YELLOW)

        for i in [1, 9, 17, 27, 28, 29]:
            grid[0][i].set_color(GREEN)

        for i in [2, 11, 20, 39, 40, 41]:
            grid[0][i].set_color(RED)
        self.add(grid)
       # self.add(get_submobject_index_labels(grid[0]))
        self.wait()

class Rationnels(Scene):
    def construct(self):
        rat = VGroup(
            TexMobject(
                r"{1\over 1}", r"\quad", r"{-1\over 1}", r"\quad", r"{2\over 1}", r"\quad", r"{-2\over 1}", r"\quad", r"{3\over 1}", r"\quad", r"{-3\over 1}", r"\quad", r"\cdots"
            ),
            TexMobject(
                r"{1\over 2}", r"\quad", r"{-1\over 2}", r"\quad", r"{2\over 2}", r"\quad", r"{-2\over 2}", r"\quad", r"{3\over 2}", r"\quad", r"{-3\over 2}", r"\quad", r"\cdots"
            ),
            TexMobject(
                r"{1\over 3}", r"\quad", r"{-1\over 3}", r"\quad", r"{2\over 3}", r"\quad", r"{-2\over 3}", r"\quad", r"{3\over 3}", r"\quad", r"{-3\over 3}", r"\quad", r"\cdots"
            ),
            TexMobject(
                r"{1\over 4}", r"\quad", r"{-1\over 4}", r"\quad", r"{2\over 4}", r"\quad", r"{-2\over 4}", r"\quad", r"{3\over 4}", r"\quad", r"{-3\over 4}", r"\quad", r"\cdots"
            ),
            TexMobject(
                r"{1\over 5}", r"\quad", r"{-1\over 5}", r"\quad", r"{2\over 5}", r"\quad", r"{-2\over 5}", r"\quad", r"{3\over 5}", r"\quad", r"{-3\over 5}", r"\quad", r"\cdots"
            ),
            TexMobject(
                r"{1\over 6}", r"\quad", r"{-1\over 6}", r"\quad", r"{2\over 6}", r"\quad", r"{-2\over 6}", r"\quad", r"{3\over 6}", r"\quad", r"{-3\over 6}", r"\quad", r"\cdots"
            ),
            TexMobject(
                r"\vdots", r"\qquad", r"\vdots", r"\qquad", r"\vdots", r"\qquad", r"\vdots", r"\qquad", r"\vdots", r"\qquad", r"\vdots", r"\qquad", r"\ddots"
            )
        )
        rat.scale(.5)
        rat.shift(UP * 2)
        for i in range(7):
            rat.submobjects[i].shift(DOWN * i / 1.5)
        self.play(*[Write(rat.submobjects[i][j]) for i in range(7) for j in range(13)])
        self.wait()

class Rat2(Scene):
    def construct(self):
        ratList = []
        dx = 3/2
        dy = 3/2
        for i in range (1, 5):
            if i % 2 == 1:
                ratList.append(
                    self.col(4, i, dy).shift(RIGHT * dx * i)
                )
            else:
                ratList.append(
                    self.col(4, -i//2, dy).shift(RIGHT * dx * i)
                )

        rat = VGroup(*ratList)
        self.play(Write(rat))
        self.wait()


    def col(self, n, num, dy):
        l = []
        for i in range(1, n + 1):
            l.append(
                TexMobject(str(num) + r"\over" + str(i)).shift(DOWN * i * dy)
            )
        l.append(TexMobject(r"\vdots").shift(DOWN * (n + 1) * dy))
        return VGroup(*l).shift(UL * 3 + UP)
        

    def col_alt(self, n, num, dy):
        l = []
        for i in range(1, n + 1):
            if num >= 0:
                l.append(
                TexMobject(str(num) + r"\over" + str(i)).shift(DOWN * i * dy)
            )
            else:
                l.append(
                TexMobject("-{" + str(-num) + r"\over" + str(i) + "}").shift(DOWN * i * dy)
            )
        l.append(TexMobject(r"\vdots").shift(DOWN * (n + 1) * dy))
        return VGroup(*l).shift(UL * 3 + UP)