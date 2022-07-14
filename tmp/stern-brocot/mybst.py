from utils import *

class Node(VGroup):
    def __init__(self, value:str="1/1", font_size=DEFAULT_FONT_SIZE) -> None:
        value = Rational(value)
        self.value = value
        self._tex = MathTex(*(latex(value).split(' ')), font_size=font_size)
        self._circle = Circle(color=WHITE).surround(self._tex)
        
        VGroup.__init__(self, self._tex, self._circle)

    def __lt__(self, other):
        return self.value < other.value
    def __ge__(self, __o) -> bool:
        return not self.__lt__(__o)
    def __getitem__(self, value):
        return self._tex[value]

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
        for i in range(3):
            self.add(Node(font_size=30)[i])
            self.wait() 