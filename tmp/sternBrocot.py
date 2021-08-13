from manim import *
class Fraction(MathTex):
    """
    A fraction of two strictly positive integers
    """

    def __init__(self, numerator, denominator):
        if not (numerator > 0 and denominator > 0):
            raise ValueError("Both arguments must be positive integers")
        self.numerator = numerator
        self.denominator = denominator
        MathTex.__init__(self, *("{} \over {}".format(numerator, denominator).split(" ")))
       

class Node(object):
    
    """
    Binary tree node
    """
    def __init__(self, fraction: Fraction, left=None, right=None, parent=None):
        self.fraction = Fraction(1, 1) if fraction is None else fraction 
        self.left = left
        self.right = right
        self.parent = parent    
    
    def set_left(self, left):
        self.left = left
        left.parent = self

    def set_right(self, right):
        self.right = right
        right.parent = self

class Tree(object):
    """
    Stern-brocot tree
    TODO: Refactor to inherit from Mobject
    """

    def __init__(
        self, 
        root_fraction: Fraction = None, 
        height: int = 0, 
        position: np.ndarray = UP*3, 
        width: float = 3.5
    ):
        """
            constructs Stern-Brocot tree of height 'height' and root label 'root_fraction'
            TODO: Refactor and rewrite comments
        """
        self.left = None
        self.right = None
        # root step
        self.root = Node(root_fraction)
        self.fraction = self.root.fraction
        self.height = height
        self.position = position
        self.width = width
        self.texFraction = TexMobject(*str(self.fraction).split(" ")).scale(.4).move_to(self.position)
        
        # Stop at leaf leaf
        if height == 0:
            return

        # left step:

        left = Tree(
            root_fraction = Fraction(
                numerator = self.fraction.numerator,
                denominator = self.fraction.numerator + self.fraction.denominator
            ),
            height = self.height - 1,
            position = self.position + LEFT * self.width + DOWN * 1.5,
            width = self.width / 2
        )

        # right step:
        right = Tree(
            root_fraction = Fraction(
                numerator = self.fraction.numerator + self.fraction.denominator,
                denominator = self.fraction.denominator
            ),
            height=self.height - 1,
            position = self.position + RIGHT * self.width + DOWN * 1.5,
            width = self.width / 2
        )

        # set left and right children
        self.root.set_left(left)
        self.left = left
        self.root.set_right(right)
        self.right = right


    
    
class SternBrocotTest(Scene):
    def construct(self):
        t = Tree(root_fraction = Fraction(1, 1), height=2)
        print()
        self.showTree(t)
        self.play()
        self.wait()

    def showTree(self, tree):
        """
        Traverse the tree and play(Write) each fraction
        """
        if tree is None:
            return
        fraction = tree.texFraction
        self.play(
            Write(fraction),
            ShowCreation(Circle(arc_center = fraction.get_center(), radius = 0.3, color = WHITE))
        )
        if tree.height > 0:
            self.play(
                Write(Line(tree.position, tree.left.position, buff=SMALL_BUFF)),
                Write(Line(tree.position, tree.right.position, buff=SMALL_BUFF))
            )
        self.showTree(tree.left)
        self.showTree(tree.right)
        

class show(Scene):
    def construct(self):
        print(type(UP))