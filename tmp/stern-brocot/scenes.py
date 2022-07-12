from manim import *
from sympy import Rational       
from bst import BST
from utils import *





    
# class SternBrocotTest(Scene):
#     def construct(self):
#         Tree(root_fraction = Fraction(1, 1), height=3).show(self)
#         self.wait()

class CogMobject(VGroup):
    def __init__(self, radius=1, tooth_size=.1, n_teeth=None, color=WHITE):
        n_teeth = int(radius * 20) if n_teeth is None else n_teeth
        outer = ParametricFunction(
            lambda t: (np.array([np.cos(t), np.sin(t), 0])) * (radius + np.tanh(np.sin(t*n_teeth)/tooth_size)*tooth_size),
            t_range=[0, TAU], fill_opacity=1, fill_color=color, stroke_width=0
        )
        inner = Circle(.2, color=WHITE, fill_color=BLACK, fill_opacity=1)
        VGroup.__init__(self, outer, inner)

class TreeTest(Scene):
    def fractions(self, root=Rational(0, 1), height=3):
        # ε = np.identity(2)
        # L = np.array([[1, 0], [1, 1]])
        # R = np.array([[1, 1], [1, 0]])
        for i in range(1, 2 ** height):
            current = root
            ibin = format(i, 'b')
            for bit in ibin:
                # print(ibin)
                current = Rational(current.numerator+current.denominator, current.denominator) if int(bit) else\
                    Rational(current.numerator, current.numerator+current.denominator)
            yield current



    def construct(self):
        # tree = Graph(
        #     vertices=list(range(5)),
        #     vertex_type=Label,
        #     labels={
        #         0: "Optimization methods",
        #         1: "Exact", 
        #         2: "Approximate",
        #         3: "Heuristic",
        #         4: "Metaheuristic"
        #     },
        #     edges=[(0, 1), (0, 2), (2, 3), (2, 4)],
        #     layout='tree',
        #     root_vertex=0,
        #     edge_type=Arrow
        # )
        # c = CogMobject().shift(RIGHT*1.3)
        # c2 = CogMobj2ect(2, color=RED).shift(LEFT*1.8)
        # self.add(c, c2)
        # self.wait()
        # c.add_updater(lambda mob, dt: mob.rotate(-TAU*dt/3))
        # c2.add_updater(lambda mob, dt: mob.rotate(TAU*dt/6))

        # self.wait(10)
        tree = BST()
        for f in self.fractions(height=4):
            tree.insert(f)


        graph = Graph(
            vertices=[latex(f) for f in tree.traverse()],
            layout_config={'vertex_spacing': (2, 2)},
            labels=True,
            root_vertex=latex(tree.traverse()[0]),
            layout="tree",
            edges=get_edge_list(tree.root),
        ).scale(.6)
        
        self.add(graph)
        self.wait()

def stern_brocot_sqrt2():
    from math import sqrt
    from matplotlib import pyplot as plt
    left = (1, 1)
    right = (2, 1)
    errors = []
    # print(f'approximation = {left[0]}/{left[1]}≤√2≤{right[0]}/{right[1]}')
    # print(f'error = {min(abs(sqrt(2)-a[0]/a[1]) for a in [left, right])}')
    for _ in range(40):
        middle = (left[0] + right[0], left[1] + right[1])
        if middle[0] ** 2 > 2 * middle[1] ** 2:
            right = middle
        else:
            left = middle
        errors.append(min(abs(sqrt(2)-a[0]/a[1]) for a in [left, right]))
        # errors.append(abs(left[0]/left[1] - right[0]/right[1]))
        # print(f'{left[0]}/{left[1]}≤√2≤{right[0]}/{right[1]}')
    plt.semilogy()
    plt.plot(errors)
    plt.show()

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

