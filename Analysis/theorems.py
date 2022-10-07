from manim import *


chapter = ""
class Theorem(VGroup):
    count = 0
    CONFIG = {
        "align": DOWN
    }
    def __init__(self, body, title=None):
        Theorem.count += 1
        self.body = body
        self.title = Tex(f"Théorème {chapter}.{Theorem.count} ({title})." if title else f"Théorème {chapter}.{Theorem.count}.")
        # create down arranged theorem
        VGroup.__init__(
            self, 
            VGroup(
                self.title,
                self.body
            ).arrange(DOWN, aligned_edge=LEFT)
        )

class Lemma(Theorem):
    def __init__(self, body, title=None):
        Theorem.count += 1
        self.body = body
        self.title = Tex(f"Lémme {chapter}.{Theorem.count} ({title})." if title else f"Lémme {chapter}.{Theorem.count}.")
        # create down arranged theorem
        VGroup.__init__(
            self, 
            VGroup(
                self.title,
                self.body
            ).arrange(DOWN, aligned_edge=LEFT)
        )

class Corollary(Theorem):
    def __init__(self, body, title=None):
        Theorem.count += 1
        self.body = body
        self.title = Tex(f"Corollaire {chapter}.{Theorem.count} ({title})." if title else f"Corollaire {chapter}.{Theorem.count}.")
        # create down arranged theorem
        VGroup.__init__(
            self, 
            VGroup(
                self.title,
                self.body
            ).arrange(DOWN, aligned_edge=LEFT)
        )

class TheoremAndDefinition(Theorem):
    def __init__(self, body, title=None):
        Theorem.count += 1
        self.body = body
        self.title = Tex(
            f"Théorème et définition {chapter}.{Theorem.count} ({title})." 
            if title else f"Corollaire {chapter}.{Theorem.count}."
        )
        # create down arranged theorem
        VGroup.__init__(
            self, 
            VGroup(
                self.title,
                self.body
            ).arrange(DOWN, aligned_edge=LEFT)
        )