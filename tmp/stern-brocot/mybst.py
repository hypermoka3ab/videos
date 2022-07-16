from utils import *
from sympy import continued_fraction, continued_fraction_reduce

def fractions(root=Rational(0, 1), height=3, order="stern-brocot"):

    if order == "wlof-klein":
        for i in range(1, 2 ** height):
            current = root
            ibin = format(i, 'b')
            for bit in ibin:
                current = Rational(current.p, current.p+current.q) if int(bit) else Rational(current.p+current.q, current.q)

            yield current
    elif order == "stern-brocot":
        ε = np.identity(2)
        L = np.array([[1, 0], [1, 1]])
        R = np.array([[1, 1], [0, 1]])
        for i in range(1, 2 ** height):
            matrix = ε
            ibin = format(i, 'b')[1:]
            for bit in ibin:
                matrix = np.dot(matrix, R if int(bit) else L)
            yield Rational(*matrix.dot([1, 1]))


def get_left_right(r:str):
    r = Rational(r)
    one, other = continued_fraction(r), continued_fraction(r)
    one[-1] += 1
    one = Rational(continued_fraction_reduce(one))

    other[-1] -= 1
    other.append(2)
    other = Rational(continued_fraction_reduce(other))

    return string(min(one, other)), string(max(one, other))

def string(r:Rational) -> str:
    return f"{r.p}/{r.q}"

class Node(MathTex):
    def __init__(self, value:str="1/1", font_size=DEFAULT_FONT_SIZE, *args, **kwargs) -> None:
        self.value = Rational(value)
        self._tex = MathTex.__init__(self, *(latex(self.value).split(' ')), font_size=font_size)
        self.left = None
        self.right = None
        
        # self._circle = Circle(color=WHITE).surround(self._tex)        
        # VGroup.__init__(self, self._tex, self._circle, *args, **kwargs)

    def __lt__(self, other):
        return self.value < other.value
    def __ge__(self, __o) -> bool:
        return not self.__lt__(__o)
    def __getitem__(self, value):
        return self._tex[value]


class BinaryTree(Graph):
    def __init__(self, height=4, root_position=UP*3, spacing=(2.5, 1.5), scale=1):
        
        # populate with fractions
        nodes = ["1/1"]
        node_positions = [root_position]

        level = 0
        while level < height - 1:

            # nodes for which to add descendents (ignore nodes above level)
            level_nodes = nodes[2**level - 1:2**(level+1) - 1]
            level_positions = node_positions[2**level - 1:2**(level+1) - 1]

            for node, pos in zip(level_nodes, level_positions):
                # add left node and position
                left, right = get_left_right(Rational(node))
                nodes.append(left)
                node_positions.append(pos  + DOWN * spacing[1] + LEFT * spacing[0] / 2**level)

                # add right node and position
                nodes.append(right)
                node_positions.append(pos  + DOWN * spacing[1] + RIGHT * spacing[0] / 2**level)

            level += 1

        # edges
        edges = []
        for node in nodes[:2**level - 1]:
            left, right = get_left_right(Rational(node))
            edges.extend(((node, left), (node, right)))

        # layout
        lt = dict(zip(nodes, node_positions))
        
        Graph.__init__(
            self, nodes, edges, labels=True, 
            vertex_mobjects={node: Node(node, font_size=30) for node in nodes},
            edge_config = {"buff": MED_LARGE_BUFF},
            layout=lt
        )
        for node in nodes:
            left, right = get_left_right(Rational(node))
            self.vertices[node].left = left
            self.vertices[node].right = right
        self.scale(scale)

    def get_node_mobjects(self):
        return self.submobjects[:len(self.vertices)]
    
    def get_edge_mobjects(self):    
        return self.submobjects[len(self.vertices):]
        
    def show_growth(self, scene:Scene):
        # loop over levels from 1 to height
        
        for level in range(int(np.log2(len(self.vertices) + 1))):    
            # create nodes of the level
            scene.play(*[Write(node) for node in self.get_node_mobjects()[2**(level) - 1:2**(level+1) - 1]])
            scene.wait()

            # create the edges for all layers except for the last
            if level < np.log2(len(self.vertices) + 1) - 1:
                scene.play(*[Create(edge) for edge in self.get_edge_mobjects()[2**(level+1) - 2:2**(level+2) - 2]])




class BST:
    def __init__(self) -> None:
        self.root = None
        

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        if self.root < node:
            self.root.left = node
            node.parent = self.root
        if self.root > node:
            node.parent = self.root
            self.root.right = node 
        else:
            raise f"Cant insert {value}"

    def get_edge_list(self):
        edges = []
        if self is not None: 
            if self.left is not None: edges.append((latex(self.value), latex(self.left.value)))
            if self.right is not None: edges.append((latex(self.value), latex(self.right.value)))
            edges += self.left.get_edge_list() + self.right.get_edge_list()
        return edges

    
class Test(Scene):
    def construct(self):
        tree = BinaryTree()
        tree.show_growth(self)
        self.wait()

