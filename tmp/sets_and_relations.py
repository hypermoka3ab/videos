from manim import *

class Logic(Scene):
    
    
    def construct(self):
        self.define_proposition()
        self.introduce_truth_tables()

    def define_proposition(self):
        """
        Introdction, intuitive explanation of the notion of a proposition and truth value, and hook for truth tables
        """
        # Ask what is a proposition?
        question = Text("C'est quoi Une proposition ?").to_edge(UP)
        self.play(Write(question))
        self.wait(2)


    def introduce_truth_tables(self):
        pass