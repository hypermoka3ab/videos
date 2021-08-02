from manimlib.imports import *
from collections import deque
class Fraction(object):
    """
    TODO : Refactor to inherit from Mobject
    A fraction of two strictly positive integers
    """

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator
    
    def __repr__(self):
        return "{} \\over {}".format(self.numerator, self.denominator)

    def __index__(self, i):
        if i > 1:
            raise IndexError("Fraction index out of range")
        return self.numerator if i == 0 else self.denominator 
     
class Node(object):
    
    """
    Binary tree node
    """
    def __init__(self, fraction: Fraction, left=None, right=None, parent=None):
        self.fraction = Fraction(1, 1) if fraction is None else fraction 
        self.left = left
        self.right = right
        self.parent = parent

    def get_fraction(self):
        return self.fraction
    
    def set_left(self, left):
        self.left = left
        left.parent = self

    def set_right(self, right):
        self.right = right
        right.parent = self

    # getters for parent, left, right and fraction
    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def get_fraction(self):
        return self.fraction

class Tree(object):
    """
    Stern-brocot tree
    TODO : Refactor to inherit from Mobject
    """

    def __init__(self, root_fraction: Fraction=None, height: int=0, position: type(UP)=UP*2, width: float=4):
        """
            constructs Stern-Brocot tree of height 'height' and root label 'root_fraction'
            TODO : Refactor and rewrite comments
        """
        self.left = None
        self.right = None
        # root step
        self.root = Node(root_fraction)
        self.fraction = self.root.fraction
        self.height = height
        self.position = position
        self.width = width
        self.texFraction = TexMobject(*str(self.fraction).split(" ")).move_to(self.position)
        
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
        t = Tree(root_fraction = Fraction(1, 1), height=3)
        print()
        self.showTree(t)

        self.wait()

    def showTree(self, tree):
        """
        Traverse the tree and play(Write) each fraction
        """
        if tree is None:
            return
        fraction = tree.texFraction
        self.play(Write(fraction))
        if tree.height > 0:
            self.play(
                Write(tree.left.texFraction),
                Write(tree.right.texFraction),
                Write(Line(tree.position, tree.left.position, buff=SMALL_BUFF)),
                Write(Line(tree.position, tree.right.position, buff=SMALL_BUFF))
            )
        self.showTree(tree.left)
        self.showTree(tree.right)
        

