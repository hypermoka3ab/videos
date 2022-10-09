from manim import *
from theorems import TheoremAndDefinition

class Axioms(Scene):
    def construct(self):
        exists = Tex(
            r"Il existe un ensemble \(\mathbb{R}\) muni de deux lois de compositions\\ internes ",
            r"\(+, \cdot\) et d'une relation binaire \(\le\) tels que:", tex_environment=None
        ).to_corner(UL)
        
        self.play(Write(exists))
        self.wait()

        self.addition()

        multiplication = VGroup(
            MathTex(r"\forall x, y, z \in \mathbb{R},\ x \cdot (y \cdot z) = (x \cdot y) \cdot z"),
            MathTex(r"\exists x \in \mathbb{R}\ \forall y \in  \mathbb{R},\ x \cdot y = y \cdot x = y"),
            MathTex(r"\forall x \in \mathbb{R} \backslash \{0\}\ \exists y \in \mathbb{R},\ x \cdot y = y\cdot x = 1"),
            MathTex(r"\forall x, y \in \mathbb{R},\ x \cdot y = y \cdot x"),
        ).arrange(DOWN, aligned_edge=LEFT)
        
        self.play(FadeIn(multiplication))
        self.wait()

        distrubitive = MathTex(r"\forall x, y, z \in \mathbb{R},\ x \cdot (y + z) = x\cdot y + x\cdot z")

        self.play(
            FadeOut(multiplication, shift=DOWN),
            FadeIn(distrubitive, shift=DOWN)
        )

        self.wait()

        order = VGroup(
            MathTex(r"\forall x \in \mathbb{R},\ x \le x"),
            MathTex(r"\forall x, y \in \mathbb{R},\ (x \le y \wedge y \le x) \Rightarrow x = y"),
            MathTex(r"\forall x, y, z \in \mathbb{R},\ (x \le y \wedge y \le z) \Rightarrow x \le z"),
            MathTex(r"\forall x, y \in \mathbb{R},\ x \le y \lor y \le x"),
        ).arrange(DOWN, aligned_edge=LEFT)

        self.play(
            FadeOut(distrubitive, shift=DOWN),
            FadeIn(order, shift=DOWN)
        )
        self.wait()

        compatible = VGroup(
            MathTex(r"\forall x, y, z \in \mathbb{R},\ x \le y \Rightarrow x + z \le y + z"),
            MathTex(r"\forall x, y \in \mathbb{R},\ (0 \le x \wedge 0 \le y) \Rightarrow 0 \le x\cdot y"),
        ).arrange(DOWN, aligned_edge=LEFT)

        self.play(
            FadeOut(order, shift=DOWN),
            FadeIn(compatible, shift=DOWN)
        )

        self.wait()

        result = Tex(
            r"\((\mathbb{R}, +, \cdot, \le)\) ",
            "est un corps commutatif totalement ordonée.",
            tex_environment=None
        )

        
        self.play(
            FadeOut(compatible, shift=DOWN),
            FadeIn(result, shift=DOWN)
        )

        self.wait()

        alternative = Tex(
            r"\((\mathbb{Q}, +, \cdot, \le)\) ",
            "est un corps commutatif totalement ordonée.",
            tex_environment=None
        )

        self.play(TransformMatchingTex(result, alternative))
        self.wait()


    def addition(self):
        associative = MathTex(r"\forall x, y, z \in \mathbb{R},\ x + (y + z) = (x + y) + z")
        self.play(FadeIn(associative, shift=DOWN))
        self.wait()

        zero = MathTex(r"\exists x \in \mathbb{R}\ \forall y \in  \mathbb{R},\ x + y = y + x = y")
        self.play(FadeOut(associative, shift=DOWN), FadeIn(zero, shift=DOWN))
        self.wait()

        zero_uniqueness = TheoremAndDefinition(
            title="Unicité de \(0\)",
            body=Tex(
                r"L'élèment qui vérifie l'axiome 2 est unique.\\", 
                "On l'appelle ``zero'' ", 
                "et on le note \(0\).",
                tex_environment=None
            )
        )
        self.play(FadeOut(zero, shift=DOWN), FadeIn(zero_uniqueness.title, shift=DOWN))
        self.wait()
        for part in zero_uniqueness.body:
            self.play(Write(part), run_time=1)
            self.wait(.5)

        proof = [
            MathTex(
                r"{{0^\prime}} = {{0^\prime + 0^{\prime\prime} }}"
            ).next_to(zero_uniqueness, DOWN, buff=MED_LARGE_BUFF),
            MathTex(
                r"{{0^\prime}} = {{0^{\prime\prime}}}"
            ).next_to(zero_uniqueness, DOWN, buff=MED_LARGE_BUFF)
        ]

        self.play(Write(proof[0][:2]))
        self.wait()
        self.play(TransformMatchingShapes(proof[0][0].copy(), proof[0][2]))
        self.wait()
        self.play(TransformMatchingTex(proof[0], proof[1]))
        self.wait()

        opposite = MathTex(r"\forall x \in \mathbb{R}\ \exists y \in \mathbb{R},\ x + y = y + x = 0")
        self.play(
            FadeOut(zero_uniqueness, proof[1], shift=DOWN),
            FadeIn(opposite, shift=DOWN)
        )
        self.wait()

        opposite_uniqueness = TheoremAndDefinition(
            title="Unicité de l'opposé",
            body=Tex(
                r"Pour tout \(x\) dans \(\mathbb{R}\), l'élément qui vérifie l'axiome 3 est unique.\\",
                "On l'appelle ``l'opposé de \(x\)'' ",
                "et on le note \(-x\).",
                tex_environment=None
            )
        )
        self.play(FadeOut(opposite, shift=DOWN), FadeIn(opposite_uniqueness.title, shift=DOWN))
        self.wait()
        
        for part in opposite_uniqueness.body:
            self.play(Write(part), run_time=1)
            self.wait(.5)

        commutative = MathTex(r"\forall x, y \in \mathbb{R},\ x + y = y + x")
        self.play(FadeOut(opposite_uniqueness, shift=DOWN), FadeIn(commutative, shift=DOWN))
        self.wait()
        self.play(FadeOut(commutative, shift=DOWN))
        



# completeness = r"""
#     \forall A, B \in \mathcal{P}(\mathbb{R})\backslash\{\emptyset\}, \ 
#     (\forall x \in A\ \forall y\in B,\  x \le y) 
#     \Rightarrow 
#     (\exists z \in \mathbb{R}\ \forall x \in A \ \forall y \in B, \  x \le z \le y)
# """