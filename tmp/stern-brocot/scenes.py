from manim import *
from sympy import Rational       
from bst import BST
from utils import *


    
# class SternBrocotTest(Scene):
#     def construct(self):
#         Tree(root_fraction = Fraction(1, 1), height=3).show(self)
#         self.wait()


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
                current = Rational(current.p+current.q, current.q) if int(bit) else Rational(current.p, current.p+current.q)
            yield current



    def construct(self):
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

