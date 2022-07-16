import itertools
from utils import *
import networkx as nx

def fractions(root=Rational(0, 1), height=3, order="stern-brocot"):
    # ε = np.identity(2)
    # L = np.array([[1, 0], [1, 1]])
    # R = np.array([[1, 1], [1, 0]])

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

class Node(MathTex):
    def __init__(self, value:str="1/1", font_size=DEFAULT_FONT_SIZE, *args, **kwargs) -> None:
        value = Rational(value)
        self.value = value
        self._tex = MathTex.__init__(self, *(latex(value).split(' ')), font_size=font_size)
        # self._circle = Circle(color=WHITE).surround(self._tex)
        
        # VGroup.__init__(self, self._tex, self._circle, *args, **kwargs)

    def __lt__(self, other):
        return self.value < other.value
    def __ge__(self, __o) -> bool:
        return not self.__lt__(__o)
    def __getitem__(self, value):
        return self._tex[value]


class BinaryTree(Graph):
    def __init__(self, height=4, spacing=(1.8, 2)):
        
        graph = nx.Graph() # empty graph

        # populate with fractions
        nodes = [f"{f.p}/{f.q}" for f in fractions(height=height)]
        print(nodes)
        for node in nodes:
            graph.add_node(node)

        # add edges
        for level in range(height - 1):
            for i, j in itertools.product(range(2 ** level), range(2)):
                graph.add_edge(nodes[i + 2**level - 1], nodes[i*2 + j + 2**(level+1) - 1])


        Graph.__init__(
            self, list(graph.nodes), list(graph.edges), labels=True,
            vertex_mobjects={node: Node(node, font_size=30) for node in graph.nodes},
            layout="tree", root_vertex=nodes[0], layout_config={'vertex_spacing': spacing},
            edge_config={"buff":MED_LARGE_BUFF}
        )

        

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
                print()
        



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
