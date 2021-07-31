from manimlib.imports import *
import binarytree as bt


class SternBrocot(Scene):
    def construct(self):
        pass

    
    def tree(self, height, root_fraction = TexMobject(r"1 \over 1")):
        """
            construct stern-brocot tree of height 'height > 0' and root 'root_fraction'
        """
        
        # Initiate the tree
        root = bt.Node(root_fraction)