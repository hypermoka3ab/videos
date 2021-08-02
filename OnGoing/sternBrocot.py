from manimlib.imports import *
from collections import deque
class Fraction(object):
    """
    A fraction of two strictly positive integers
    """

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator
    
    def __repr__(self):
        return "{}\\over {}".format(self.numerator, self.denominator)

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
    """

    def __init__(self, root_fraction: Fraction=None, height: int=0):
        """
            constructs Stern-Brocot tree of height 'height' and root label 'root_fraction'
        """
        if height != 0:
            # root step
            self.root = Node(root_fraction)
            self.fraction = self.root.fraction
            self.height = height
            
            # left step:

            left = Tree(
                root_fraction = Fraction(
                    numerator = self.fraction.numerator,
                    denominator = self.fraction.numerator + self.fraction.denominator
                ),
                height = self.height - 1
            )

            # right step:
            right = Tree(
                root_fraction = Fraction(
                    numerator = self.fraction.numerator + self.fraction.denominator,
                    denominator = self.fraction.denominator
                ),
                height=self.height - 1
            )

            # set left and right children
            self.root.set_left(left)
            self.left = left
            self.root.set_right(right)
            self.right = right

    
    
class SternBrocotTest(Scene):
    def construct(self):
        t = Tree(root_fraction = Fraction(1, 1), height=3)
        self.showTree(t)

        self.wait()

    def showTree(self, tree):
        """
        Traverse the tree and play(Write) each fraction
        """
        if tree is None:
            return
        fraction = tree.fraction
        self.play(Write(TexMobject(fraction)))
        self.play(
            Write(TexMobject(tree.left.fraction).move_to(DOWN + LEFT)),
            Write(TexMobject(tree.right.fraction).move_to(DOWN + RIGHT)),
        )
       

