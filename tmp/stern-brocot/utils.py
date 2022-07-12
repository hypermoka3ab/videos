from manim import *
from sympy import Rational
from bst import Node


def get_edge_list(root: Node):
    edges = []
    if root is not None: 
        if root.left is not None: edges.append((latex(root.value), latex(root.left.value)))
        if root.right is not None: edges.append((latex(root.value), latex(root.right.value)))
        edges += get_edge_list(root.left) + get_edge_list(root.right)
    return edges

def latex(r: Rational):
    return f'{r.numerator} \\over {r.denominator}'


class Label(MathTex):
    def __init__(self, label):
        super().__init__(label, font_size=20)

class CogMobject(VGroup):
    def __init__(self, radius=1, tooth_size=.1, n_teeth=None, color=WHITE):
        n_teeth = int(radius * 20) if n_teeth is None else n_teeth
        outer = ParametricFunction(
            lambda t: (np.array([np.cos(t), np.sin(t), 0])) * (radius + np.tanh(np.sin(t*n_teeth)/tooth_size)*tooth_size),
            t_range=[0, TAU], fill_opacity=1, fill_color=color, stroke_width=0
        )
        inner = Circle(.2, color=WHITE, fill_color=BLACK, fill_opacity=1)
        VGroup.__init__(self, outer, inner)