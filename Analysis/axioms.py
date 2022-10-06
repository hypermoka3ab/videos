from manim import *


class Axioms(Scene):
    def construct(self):
        axioms = VGroup(
            Tex(
                r"Il existe un ensemble \(\mathbb{R}\) muni de deux lois de compositions\\ internes ",
                r"\(+, \cdot\) et d'une relation binaire \(\le\) tels que:", tex_environment=None
            ),
            Tex(r"I. \((\mathbb{R}, +, \cdot)\) est un corps commutatif."),
            Tex(r"II. \(\le\) est une relation d'ordre sur \(\mathbb{R}\)."),
            Tex(r"III. \(\le\) est compatible avec l'addittion et la multiplication."),
            Tex(r"On dit donc \((\mathbb{R}, +, \cdot, \le)\) est un corps commutatif ordonée.")
        ).arrange(DOWN, aligned_edge=LEFT).shift(UP)

        for axiom in axioms:
            self.play(FadeIn(axiom, shift=RIGHT))
            self.wait()

        sufficient = Tex("Ça suffit?", r"\textellipsis Non.").next_to(axioms, DOWN)
        self.play(Write(sufficient[0]))
        self.wait()
        self.play(Write(sufficient[1]))
        self.wait()

        self.play(
            ReplacementTransform(
                axioms[1:],
                VGroup(
                    Tex(r"I. \((\mathbb{Q}, +, \cdot)\) est un corps commutatif."),
                    Tex(r"II. \(\le\) est une relation d'ordre sur \(\mathbb{Q}\)."),
                    Tex(r"III. \(\le\) est compatible avec l'addittion et la multiplication."),
                    Tex(r"On dit donc \((\mathbb{Q}, +, \cdot, \le)\) est un corps commutatif ordonée.")
                ).arrange(DOWN, aligned_edge=LEFT)
            ), FadeOut(sufficient), FadeOut(axioms[0])
        )
        self.wait()




# addition = [
#     r"\forall x, y, z \in \mathbb{R},\ x + (y + z) = (x + y) + z",
#     r"\exists x \in \mathbb{R}\ \forall y \in  \mathbb{R},\ x + y = y + x = y",
#     r"\forall x \in \mathbb{R}\ \exists y \in \mathbb{R},\ x + y = y + x = 0",
#     r"\forall x, y \in \mathbb{R},\ x + y = y + x",
# ]  

# multiplication = [    
#     r"\forall x, y, z \in \mathbb{R},\ x \cdot (y \cdot z) = (x \cdot y) \cdot z",
#     r"\exists x \in \mathbb{R}\ \forall y \in  \mathbb{R},\ x \cdot y = y \cdot x = y",
#     r"\forall x \in \mathbb{R} \backslash \{0\}\ \exists y \in \mathbb{R},\ x \cdot y = y\cdot x = 1",
#     r"\forall x, y \in \mathbb{R},\ x \cdot y = y \cdot x",
# ]

# distrubutivity = r"\forall x, y, z \in \mathbb{R},\ x \cdot (y + x) = x\cdot y + x\cdot z"

# order = [
#     r"\forall x \in \mathbb{R},\ x \le x",
#     r"\forall x, y \in \mathbb{R},\ (x \le y \wedge y \le x) \Rightarrow x = y",
#     r"\forall x, y, z \in \mathbb{R}, (x \le y \wedge y \le z) \Rightarrow x \le z",
#     r"\forall x, y \in \mathbb{R},\ x \le y \lor y \le x",
# ]
 
# compatibilty = [ 
#     r"\forall x, y, z \in \mathbb{R},\ x \le y \Rightarrow x + z \le y + z",
#     r"\forall x, y \in \mathbb{R},\ (0 \le x \wedge 0 \le y) \Rightarrow 0 \le x\cdot y",
# ]


# completeness = r"""
#     \forall A, B \in \mathcal{P}(\mathbb{R})\backslash\{\emptyset\}, \ 
#     (\forall x \in A\ \forall y\in B,\  x \le y) 
#     \Rightarrow 
#     (\exists z \in \mathbb{R}\ \forall x \in A \ \forall y \in B, \  x \le z \le y)
# """

# everything = [
#     addition, multiplication, [distrubutivity], 
#     compatibilty, [completeness]
# ]