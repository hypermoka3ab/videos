from manimlib.imports import *
from scipy import misc
class Test(GraphScene):
    CONFIG = {
        'graph_origin': LEFT * 3,
        'x_min': 0,
        'x_max': 3,
        'x_tick_frequency': 1,
        'x_labeled_nums': [1, 2, 3],
        'y_min': -2,
        'y_max': 2,
        'y_tick_frequency': 1,
        'y_labeled_nums': [-1, 0, 1],
        "exclude_zero_label": False,
    }

    def construct(self):
        self.setup_axes(animate=True)
        self.wait()
        Cf = self.get_graph(lambda x : (x ** 2 - 2) / 2)
        self.play(ShowCreation(Cf))
        self.wait()
        self.play(
            ShowCreation(self.Tangent2F(Cf, 2.5, 1e-6))
        )
        self.wait()

    def Tangent2F(self, courbe, x0, dx):
        return self.get_graph(
            lambda x: misc.derivative(courbe.underlying_function, x0, dx) * 
            (x - x0) + courbe.underlying_function(x0) 
        )