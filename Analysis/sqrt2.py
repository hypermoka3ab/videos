from manim import *

class Sqrt2IsNotRational(Scene):
    def construct(self):
        hyothesis = MathTex(
            r"\text{Soient }", r"p ,q \in \mathbb{N} \text{ tels que }", "{p", "^2", r"\over",  "q", "^2}", "=", "2",
            r"\text{ et }", "p", r"\wedge", "q", "=", "1"
        ).to_corner(UL)
        
        proof_p_even =  MathTex(
            "{p", "^2", r"\over",  "q", "^2}", "=", "2", r"&\Rightarrow", "p", "^2", "=", "2", "q", "^2", 
            r"\\ &\Rightarrow", "2", "|", "p", "^2", 
            r"\\ &\Rightarrow", "2", "|", "p", 
            r"\\ &\Rightarrow", "p", "=", "2", "k", r",\ k \in \mathbb{N}", 
        ).next_to(hyothesis, DOWN).to_edge(LEFT)
        
        proof_q_even =  MathTex(
            "p", "^2", "=", "2", "q", "^2", r"&\Rightarrow", "(", "2", "k", ")", "^2", "=", "2", "q", "^2",
            r"\\ &\Rightarrow", "4", "k", "^2", "=", "2", "q", "^2",
            r"\\ &\Rightarrow", "2", "k", "^2", "=", "q", "^2",
            r"\\ &\Rightarrow", "2", "|", "q", "^2",
            r"\\ &\Rightarrow", "2", "|", "q",
        ).next_to(hyothesis, DOWN).to_edge(RIGHT)

        p_q_even =  MathTex(
            "2", "|", "p", r"\wedge", "2", "|", "q",
            r"\Rightarrow", "2", "|", "p", r"\wedge", "q",
            r"\Rightarrow", "2", "|", "1"
        ).next_to(hyothesis, DOWN).to_edge(LEFT)

        changes_to_p = [
            [
                tuple(range(2, 10)),
                tuple(range(7)),
            ],
            [
                (0, 1, 3, 4, 5, 6),
                (8, 9, 12, 13, 10, 11)
            ],
            [
                (11, 8, 9),
                (15, 17, 18)
            ],
            [
                (15, 16, 17),
                (20, 21, 22)
            ],
            [
                (20, 22),
                (26, 24)
            ]
        ]

        changes_to_q = [
            [
                (8, 9, 12, 13, 10, 11),
                tuple(range(6))
            ],
            [
                (0, 0, 1, 2, 3, 4, 5),
                (7, 10, 11, 12, 13, 14, 15)
            ],
            [
                (-3, -2),
                (8, 9)
            ],
            [
                (8, 9, 11, 12, 13, 14, 15),
                tuple(range(17, 24))
            ],
            [
                (17, 18, 19, 20, 22, 23),
                (25, 26, 27, 28, 29, 30)
            ],
            [
                (25, 29, 30),
                (32, 34, 35)
            ],
            [
                (32, 33, 34),
                (37, 38, 39)
            ]
        ]

        changes_to_qp = [
            [
                [21, 22, 23], 
                [0, 1, 2]
            ],
            [
                (37, 38, 39),
                (4, 5, 6)
            ],
            [
                (0, 4, 1, 5, 2, 3, 6),
                (8, 9, 8, 9, 10, 11, 12)
            ],
            [
                (8, 9, 10, 11, 12),
                (14, 15, 16, 16, 16)
            ]
        ]
        self.play(Write(hyothesis))
        self.wait()
        self.play(
            *[
                ReplacementTransform(hyothesis[pre].copy(), proof_p_even[post])
                for pre, post in zip(*changes_to_p[0])
            ]
        )
        self.wait()
        self.play(Write(proof_p_even[7]))
        self.play(
            *[
                ReplacementTransform(proof_p_even[pre].copy(), proof_p_even[post])
                for pre, post in zip(*changes_to_p[1])
            ]
        )
        self.wait()
        self.play(Write(proof_p_even[14]))
        self.play(
            *[
                ReplacementTransform(proof_p_even[pre].copy(), proof_p_even[post])
                for pre, post in zip(*changes_to_p[2])
            ],
            Write(proof_p_even[16])
        )
        self.wait()
        self.play(Write(proof_p_even[19]))
        self.play(
            *[
                ReplacementTransform(proof_p_even[pre].copy(), proof_p_even[post])
                for pre, post in zip(*changes_to_p[3])
            ]
        )
        self.wait()
        self.play(Write(proof_p_even[23]))
        self.play(
            *[
                ReplacementTransform(proof_p_even[pre].copy(), proof_p_even[post])
                for pre, post in zip(*changes_to_p[4])
            ],
            Write(proof_p_even[25]), Write(proof_p_even[27])
        )
        self.play(Write(proof_p_even[28:]))
        self.wait()
        self.play(
            *[
                ReplacementTransform(proof_p_even[pre].copy(), proof_q_even[post])
                for pre, post in zip(*changes_to_q[0])
            ]
        )
        self.wait()
        self.play(Write(proof_q_even[6]))
        self.play(
            *[
                ReplacementTransform(proof_q_even[pre].copy(), proof_q_even[post])
                for pre, post in zip(*changes_to_q[1])
            ],
            *[
                ReplacementTransform(proof_p_even[pre].copy(), proof_q_even[post])
                for pre, post in zip(*changes_to_q[2])
            ]
        )
        self.wait()
        self.play(Write(proof_q_even[16]))
        self.play(
            *[
                ReplacementTransform(proof_q_even[pre].copy(), proof_q_even[post])
                for pre, post in zip(*changes_to_q[3])
            ]
        )
        self.wait()
        self.play(Write(proof_q_even[24]))
        self.play(
            *[
                ReplacementTransform(proof_q_even[pre].copy(), proof_q_even[post])
                for pre, post in zip(*changes_to_q[4])
            ]
        )
        self.wait()
        self.play(Write(proof_q_even[31]))
        self.play(
            *[
                ReplacementTransform(proof_q_even[pre].copy(), proof_q_even[post])
                for pre, post in zip(*changes_to_q[5])
            ],
            Write(proof_q_even[33])
        )
        self.wait()
        self.play(Write(proof_q_even[36]))
        self.play(
            *[
                ReplacementTransform(proof_q_even[pre].copy(), proof_q_even[post])
                for pre, post in zip(*changes_to_q[6])
            ]
        )
        self.wait()

        self.play(
            FadeOut(proof_q_even),
            FadeOut(proof_p_even),
            *[
                ReplacementTransform(proof_p_even[pre].copy(), p_q_even[post])
                for pre, post in zip(*changes_to_qp[0])
            ],
            *[
                ReplacementTransform(proof_q_even[pre].copy(), p_q_even[post])
                for pre, post in zip(*changes_to_qp[1])
            ]
        )
        self.play(Write(p_q_even[3]))
        self.wait()
        self.play(Write(p_q_even[7]))
        self.play(
            *[
                ReplacementTransform(p_q_even[pre].copy(), p_q_even[post])
                for pre, post in zip(*changes_to_qp[2])
            ]
        )
        self.wait()
        self.play(Write(p_q_even[13]))
        self.play(
            *[
                ReplacementTransform(p_q_even[pre].copy(), p_q_even[post])
                for pre, post in zip(*changes_to_qp[3])
            ]
        )
        self.wait()