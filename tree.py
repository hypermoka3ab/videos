from manim import *

class TreeMobject(VGroup):
    CONFIG = {
        "neuron_radius": 0.15,
        "neuron_to_neuron_buff": MED_SMALL_BUFF,
        "layer_to_layer_buff": LARGE_BUFF,
        "neuron_stroke_color": BLUE,
        "neuron_stroke_width": 3,
        "neuron_fill_color": GREEN,
        "edge_color": LIGHT_GREY,
        "edge_stroke_width": 2,
        "edge_propogation_color": YELLOW,
        "edge_propogation_time": 1,
        "max_shown_neurons": 16,
        "brace_for_large_layers": True,
        "average_shown_activation_of_large_layer": True,
        "include_output_labels": False,
    }

    def __init__(self, neural_network, size=.15):
        VGroup.__init__(self)
        self.layer_sizes = neural_network
        self.neuron_radius = size
        self.neuron_radius= 0.15
        self.neuron_to_neuron_buff= MED_SMALL_BUFF
        self.layer_to_layer_buff= LARGE_BUFF
        self.neuron_stroke_color= BLUE
        self.neuron_stroke_width= 3
        self.neuron_fill_color= GREEN
        self.edge_color= LIGHT_GREY
        self.edge_stroke_width= 2
        self.edge_propogation_color= YELLOW
        self.edge_propogation_time= 1
        self.max_shown_neurons = 16
        self.brace_for_large_layers= True
        self.average_shown_activation_of_large_layer= True
        self.include_output_labels= False
        self.add_neurons()
        self.add_edges()

    def add_neurons(self):
        layers = VGroup(*[
            self.get_layer(size)
            for size in self.layer_sizes
        ])
        layers.arrange_submobjects(RIGHT, buff=self.layer_to_layer_buff)
        self.layers = layers
        self.add(self.layers)
        if self.include_output_labels:
            self.add_output_labels()

    def get_layer(self, size):
        layer = VGroup()
        n_neurons = size
        if n_neurons > self.max_shown_neurons:
            n_neurons = self.max_shown_neurons
        neurons = VGroup(*[Circle(
                radius=self.neuron_radius,
                stroke_color=self.neuron_stroke_color,
                stroke_width=self.neuron_stroke_width,
                fill_color=self.neuron_fill_color,
                fill_opacity=0,
            ) for _ in range(n_neurons)])
        neurons.arrange_submobjects(
            DOWN, buff=self.neuron_to_neuron_buff
        )
        for neuron in neurons:
            neuron.edges_in = VGroup()
            neuron.edges_out = VGroup()
        layer.neurons = neurons
        layer.add(neurons)

        if size > n_neurons:
            dots = MathTex("\\vdots")
            dots.move_to(neurons)
            VGroup(*neurons[:len(neurons) // 2]).next_to(
                dots, UP, MED_SMALL_BUFF
            )
            VGroup(*neurons[len(neurons) // 2:]).next_to(
                dots, DOWN, MED_SMALL_BUFF
            )
            layer.dots = dots
            layer.add(dots)
            if self.brace_for_large_layers:
                brace = Brace(layer, LEFT)
                brace_label = brace.get_tex(str(size))
                layer.brace = brace
                layer.brace_label = brace_label
                layer.add(brace, brace_label)

        return layer

    def add_edges(self):
        self.edge_groups = VGroup()
        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            for i, n1 in enumerate(l1.neurons):
                n2 = l2.neurons[2*i]
                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
                n1.edges_out.add(edge)
                n2.edges_in.add(edge)
                n2 = l2.neurons[2*i+1]
                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
                n1.edges_out.add(edge)
                n2.edges_in.add(edge)
            self.edge_groups.add(edge_group)
        self.add_to_back(self.edge_groups)

    def get_edge(self, neuron1, neuron2):
        return Line(
            neuron1.get_center(),
            neuron2.get_center(),
            buff=self.neuron_radius,
            stroke_color=self.edge_color,
            stroke_width=self.edge_stroke_width,
        )

    def add_input_labels(self):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[0].neurons):
            label = MathTex(f"x_{n + 1}")
            label.set_height(0.3 * neuron.get_height())
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    def add_labels(self, layer, labels):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[layer].neurons):
            label = MathTex(labels[n])
            label.set_height(0.3 * neuron.get_height())
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    def add_branch_labels(self, labels, move=(RIGHT, LEFT)):
        weight_group = VGroup()

        for n, i in enumerate(self.layers[1].neurons):
            edge = self.get_edge(i, self.layers[0].neurons[0])
            text = Tex(labels[n], color=RED)
            text.move_to(edge, move[n] * 2)
            weight_group.add(text)
        self.add(weight_group)


class Demo(Scene):
    def construct(self):
        title = Tex("Expected value", color=GOLD)
        title.scale(1.5)
        title.shift(3 * UP)

        title2 = Tex("Expected value", "= predicted outcome", tex_to_color_map={
                             "Expected value": GOLD})
        title2.scale(1.5)
        title2.shift(3 * UP)

        self.play(FadeIn(title))
        self.wait()

        self.play(Transform(title, title2[0]))
        self.play(FadeIn(title2[1]))

        srect = ScreenRectangle(height=5).shift(0.5*DOWN)

        self.play(Write(srect))
        self.wait()

        tree = TreeMobject(neural_network=[1, 2])
        tree.add_labels(1, [r"\text{H}", r"\text{T}"])
        tree.scale(3)
        tree.shift(4 * LEFT + 0 * DOWN)

        lbl1 = MathTex(r"x_1 = + \$ 10", r"\cdot p_1 = 0.5", tex_to_color_map={
                          r"x_1": BLUE, r"+ \$ 10": GREEN, r"p_1": ORANGE, r"0.5": GREEN})
        lbl1.scale(1)
        lbl1.shift(1 * UP + 1 * RIGHT)

        lbl2 = MathTex(r"x_2 = - \$ 5", r"\cdot p_2 = 0.5", tex_to_color_map={
                          r"x_2": BLUE, r"- \$ 5": GREEN, r"p_2": ORANGE, r"0.5": GREEN})
        lbl2.scale(1)
        lbl2.shift(1 * DOWN + 1 * RIGHT)

        self.play(Uncreate(srect))
        self.play(Write(tree))
        self.wait()

        self.play(FadeIn(lbl1))
        self.play(FadeIn(lbl2))
        self.wait()


class NewTree(Scene):
    def construct(self):
        tree = Graph(
            vertices=[1, 2, 3, 4, 5, 6, 7],
            edges=[(1, 2), (1, 3), (2, 5), (2, 4), (3, 6), (3, 7)],
            layout="tree",
            labels=True,
            root_vertex=1,
            label_fill_color=BLACK            
        )

        self.play(Write(tree))
        self.wait()