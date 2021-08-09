from manimlib.imports import *

class PositionDuProbleme(Scene):
    def construct(self):
        self.poser_le_problem()
        self.methodes_exactes()
        
    def poser_le_problem(self):
        but = TextMobject(r"On veut résoudre dans $\mathbb{K}$ des systèmes de la forme:").to_corner(UL)
        system = TexMobject(r"""
        \left\{
            \begin{array}{c c c}
                a_{11}x_1 + a_{12}x_2 + \cdots +a_{1n}x_n & = & b_1\\
                a_{21}x_1 + a_{22}x_2 + \cdots +a_{2n}x_n & = & b_2\\
                \vdots & \vdots &\vdots\\
                a_{n1}x_1 + a_{n2}x_2 + \cdots +a_{nn}x_n & = & b_n\\
            \end{array}    
        \right.%
        """)
        self.play(Write(but))
        self.play(Write(system))
        self.wait()
        system_matrice = TexMobject(r"""
        \begin{bmatrix}
            a_{11} & a_{12} & \cdots & a_{1n}\\
            a_{21} & a_{22} & \cdots & a_{2n}\\
            \vdots & \vdots & \ddots & \vdots\\
            a_{n1} &  a_{n2}& \cdots & a_{nn}
            \end{bmatrix}    
        \begin{bmatrix}
            x_1\\ x_2\\ \vdots \\ x_n
        \end{bmatrix}  
        = \begin{bmatrix}
            b_1\\ b_2\\ \vdots \\ b_n
        \end{bmatrix}
        """)
        self.play(ReplacementTransform(system, system_matrice))
        self.wait()
        self.play(FadeOut(system_matrice))
        self.wait()
        system_mat_compact = TextMobject(r"Ou également $AX = b$ avec  $A \in M_n(\mathbb{K})$ et $X, b \in \mathbb{K}^n$").to_edge(LEFT).shift(UP * .8)
        self.play(Write(system_mat_compact))
        self.wait()
        self.play(FadeOut(but), FadeOut(system_mat_compact))

    def cramer(self):
        Cramer = TextMobject("I. La méthode de Cramer:").to_corner(UL)
        system_mat_compact = TextMobject(r"Soit le système $AX = b$ où: ").to_edge(LEFT).shift(UP*2)
        matrices = TexMobject(r"""
        A = \begin{bmatrix}
            a_{11} & a_{12} & \cdots & a_{1n}\\
            a_{21} & a_{22} & \cdots & a_{2n}\\
            \vdots & \vdots & \ddots & \vdots\\
            a_{n1} &  a_{n2}& \cdots & a_{nn}
            \end{bmatrix}, \ X = \begin{bmatrix} x_1\\ x_2\\ \vdots \\ x_n \end{bmatrix}, 
        b = \begin{bmatrix} b_1\\ b_2\\ \vdots \\ b_n \end{bmatrix}, \ \det(A) \neq 0
        """)
        self.play(Write(Cramer))
        self.wait()
        self.play(Write(system_mat_compact))
        self.play(Write(matrices))
        self.wait()
        self.play(FadeOut(system_mat_compact), FadeOut(matrices))
        FormuleDeCramer = TexMobject(r"\forall k \in \mathbb{N}_n\ x_k = {\det(C_1, C_2, \cdots, C_{k-1}, b, C_{k+1}, \cdots, C_n) \over \det(A)}")
        self.play(Write(FormuleDeCramer))
        self.wait()
        self.play(FadeOut(FormuleDeCramer))
        complexite = TextMobject("La complexité de la méthode de Cramer: ").to_edge(LEFT).shift(UP * 2)
        self.play(Write(complexite))
        grand_O = TexMobject(r"O(n^{2,375477})", r"\times", r"O(n)", "=", r"O(n^{3,375477})").scale(1.5).center()
        grand_O_pratique = TexMobject(r"O(n^{3})", r"\times", r"O(n)", "=", r"O(n^{4})").scale(1.5).center()
        self.play(Write(grand_O[0]))
        self.play(Write(grand_O[2]))
        self.wait()
        self.play(Write(grand_O[1]), Write(grand_O[3]), Write(grand_O[4]))
        self.play(*[ReplacementTransform(grand_O[i], grand_O_pratique[i]) for i in [0, 4]])


    def methodes_exactes(self):
        methodesExactes = TextMobject("Commençons par les méthodes éxactes").to_edge(UP)
        self.play(Write(methodesExactes))
        self.wait()
        self.play(FadeOutAndShift(methodesExactes, LEFT)) 
        self.cramer()   


class Test(GraphScene):
    CONFIG = {
        'graph_origin': DOWN*0.9,
        'x_min': -2,
        'x_max': 2,
        'x_labeled_nums': list(range(-2, 3)),
        'x_tick_frequency':1,
        'y_min':-2,
        'y_max': 3,
        'y_labeled_nums': list(range(-2, 4)),
        'y_tick_frequency': 1,
        'y_axis_label': "$f(x)$",
    }
    def construct(self):
        self.setup_axes(animate=True)
        C1 = self.get_graph(lambda x: x + 1, x_min=self.x_min, x_max=self.x_max)
        trou = Circle(radius=.05, fill_color=BLACK, stroke_color=C1.color, fill_opacity=1)
        trou.move_to(self.coords_to_point(1, C1.underlying_function(1)))
        self.wait()
        self.play(ShowCreation(C1))
        self.play(GrowFromCenter(trou))
        
        """f_non_def.move_to(RIGHT*3.5 + UP*.5)
        f_non_def.submobjects[0].submobjects = list(reversed(f_non_def.submobjects[0].submobjects))
        f_non_def.submobjects[1].submobjects = list(reversed(f_non_def.submobjects[1].submobjects))
        self.play(Write(f_non_def))
        #self.wait()"""
        delines = self.epsilon_delta_group(1, .5, C1.underlying_function)
        self.play(Write(delines))
    
    def epsilon_delta_group(self, x0, delta, func):
        R = DashedLine(self.coords_to_point(x0 + delta, -10), self.coords_to_point(x0 + delta, 10))
        L = DashedLine(self.coords_to_point(x0 - delta, -10), self.coords_to_point(x0 - delta, 10))
        U = DashedLine(self.coords_to_point(-10, func(x0 + delta)), self.coords_to_point(+10, func(x0 + delta)))
        D = DashedLine(self.coords_to_point(-10, func(x0 - delta)), self.coords_to_point(+10, func(x0 - delta)))

        delta_lines = VGroup(R, L)
        epsilon_lines = VGroup(U, D)
        return VGroup(delta_lines, epsilon_lines)