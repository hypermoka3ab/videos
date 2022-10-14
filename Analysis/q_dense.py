from manim import *

class QDense(Scene):
    def construct(self):
        real_line = NumberLine([-2, 2], 15) # real line
        line_label = always_redraw( # R label
            lambda: 
                MathTex(r"\mathbb{R}").move_to(real_line.number_to_point(-1.8) + UP * 0.5)    
        )
        x_tracker = ValueTracker(.2) # x tracker
        y_tracker = ValueTracker(.7) # y tracker
        x_label = always_redraw( # x label
            lambda: VGroup(
                MathTex("x", font_size=30).next_to(real_line.number_to_point(x_tracker.get_value()), UP, buff = SMALL_BUFF),
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point(x_tracker.get_value()), DOWN, buff=0)
            )
        )
        y_label = always_redraw( # y label
            lambda: VGroup(
                MathTex("y", font_size=30).next_to(real_line.number_to_point(y_tracker.get_value()), UP, buff = SMALL_BUFF),
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point(y_tracker.get_value()), DOWN, buff=0)
            ) 
        )
        not_q = int(np.abs(1 / (y_tracker.get_value() - x_tracker.get_value())))
        qx_label = always_redraw(
            lambda: VGroup(
                MathTex(
                    "qx", font_size=30, tex_to_color_map={"q":YELLOW}
                ).next_to(real_line.number_to_point(not_q * x_tracker.get_value()), UP, buff = SMALL_BUFF),
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point(x_tracker.get_value() * not_q), DOWN, buff=0)
            )
        )
        qy_label = always_redraw(
            lambda: VGroup(
                MathTex(
                    "qy", font_size=30, tex_to_color_map={"q": YELLOW}
                ).next_to(real_line.number_to_point(not_q * y_tracker.get_value()), UP, buff = SMALL_BUFF),
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point(y_tracker.get_value() * not_q), DOWN, buff=0)
            )
        )
        p_label = always_redraw(
            lambda: MathTex("p", font_size=30).set_color(YELLOW).next_to(real_line.number_to_point(int(not_q * y_tracker.get_value())), UP, buff = SMALL_BUFF)
        )
        p_over_q_label = always_redraw(
            lambda: VGroup(
                Triangle(stroke_width=0, fill_color=WHITE, fill_opacity=1).scale(.1).set_color(YELLOW),
                MathTex(r"p\over q", font_size=30).set_color(YELLOW)
            ).arrange(DOWN, buff=SMALL_BUFF).next_to(real_line.number_to_point(int(not_q * y_tracker.get_value()) / not_q), DOWN, buff=0)
        )

        inQ = always_redraw(
            lambda: MathTex(r"\in \mathbb{Q}", font_size=30).next_to(p_over_q_label, RIGHT, buff=SMALL_BUFF)
        )

        q_exists = MathTex(
            r"\exists q \in \mathbb{N}\ ", "q", "(", "y", "-", "x", ")", "> 1",
            r"& \Rightarrow ", "q", "y", "-", "q", "x", "> 1", 
            r"\\ & \Rightarrow", r"\exists p \in \mathbb{Z}\ ", "q", "x", "<", "p", "<", "q", "y",
            r"\\ & \Rightarrow", r"x", "<", "{p \over q}",  "<",  "y", r"\ \square",
        ).to_corner(UL)

        yellows = [1, 9, 12, 17, 20, 22, 27]
        for i in yellows:
            q_exists[i].set_color(YELLOW)
        q_exists[0][1].set_color(YELLOW)
        q_exists[16][1].set_color(YELLOW)

        changes = [
            [
                (1, 3, 4, 1, 5, 7),
                (9, 10, 11, 12, 13, 14)
            ],
            [
                (17, 18, 19, 20, 22),
                (25, 26, 27, 28, 29)
            ]
        ]
        self.play(
            Write(real_line),
            Write(line_label),
        )
        self.wait()
        self.play(
            Write(x_label[0]),
            GrowFromCenter(x_label[1]),
            Write(y_label[0]),
            GrowFromCenter(y_label[1])
        )
        self.play(Write(q_exists[:8]))
        self.wait()
        self.play(Write(q_exists[8]))
        self.play(
            ReplacementTransform(x_label, qx_label),
            ReplacementTransform(y_label, qy_label),
            *[
                ReplacementTransform(q_exists[pre].copy(), q_exists[post])
                for pre, post in zip(*changes[0])
            ]
        )
        self.wait()
        self.play(Write(p_label), Write(q_exists[15:24]))
        self.wait()
        self.play(
            ReplacementTransform(p_label, p_over_q_label),
            ReplacementTransform(qx_label, x_label),
            ReplacementTransform(qy_label, y_label),
            Write(q_exists[24]),
            *[
               ReplacementTransform(q_exists[pre].copy(), q_exists[post])
                for pre, post in zip(*changes[1])
            ],    
        )
        self.play(Write(inQ))
        self.play(Write(q_exists[-1]))
        self.wait()


class QDense2(Scene):
    def construct(self):
        Axy_definition = MathTex(r"A_{x, y} = ", r"\{", r"r \in \mathbb{Q}| x < r < y", r"\}").to_corner(UL)
        Axy_finite = MathTex(r"A_{x, y} = ", r"\{", "r_1",  "<",  "r_2", "<", r"\cdots", "<", "r_n", r"\}").to_corner(UL)
        s = MathTex("s", "=", r"{r_1",  "+",  "r_2",  r"\over 2}").next_to(Axy_finite, DOWN).to_edge(LEFT)
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{stmaryrd}")
        s_in_A = MathTex(
            "x < ", "r_1", "<", "s", "<", "r_2", "< y", r"&\Rightarrow", r"s\in A_{x, y}",
            r"\\ & \Rightarrow", r"s = r_i", r"\text{ pour un certain }", r"i \in \llbracket 1, n \rrbracket",
            tex_template=template
        ).next_to(s, DOWN).to_edge(LEFT)

        s_between_xy = MathTex("r_1", "<", "s", "<", "r_2").next_to(s_in_A, DOWN).to_edge(LEFT)
        r_between_xy = MathTex(
            "r_1", "<", "r_i", "<", "r_2",
            r"\Rightarrow", "1", "<", "i", "<", "2", r"\ \square"
        ).next_to(s_in_A, DOWN).to_edge(LEFT)
       
        self.play(Write(Axy_definition))
        self.wait()
        self.play(
            ReplacementTransform(Axy_definition[1], Axy_finite[1]),
            ReplacementTransform(Axy_definition[2], Axy_finite[2:9:2]),
            ReplacementTransform(Axy_definition[-1], Axy_finite[-1]),
        )
        self.wait()
        self.play(*[GrowFromCenter(mob) for mob in Axy_finite[3:9:2]])
        self.wait()
        self.play(
            ReplacementTransform(Axy_finite[2].copy(), s[2]),
            ReplacementTransform(Axy_finite[4].copy(), s[4]),
            GrowFromCenter(s[3]),
        )
        self.play(Write(s[5]))
        self.wait()
        self.play(Write(s[:2]))
        self.wait()
        self.play(
            ReplacementTransform(s[0].copy(), s_in_A[3]),
            ReplacementTransform(Axy_finite[2:4].copy(), s_in_A[1:3]),
            ReplacementTransform(Axy_finite[3:5].copy(), s_in_A[4:6]),
        )
        self.wait()
        self.play(Write(s_in_A[0]), Write(s_in_A[6]))
        self.wait()
        self.play(Write(s_in_A[7:]))
        self.wait()
        self.play(ReplacementTransform(s_in_A[1:6].copy(), r_between_xy[:5]))
        self.wait()
        # self.play(
        #     ReplacementTransform(s_in_A[10].copy(), r_between_xy[2]),
        #     ReplacementTransform(s_between_xy[2], r_between_xy[2], run_time=1.5),
        #     Write(r_between_xy)
        # )
        # self.wait()

        self.play(Write(r_between_xy[5:]))
        self.wait()

        

    def illustrate_many_rationals(self):
        real_line = NumberLine([-2, 2], 15) # real line
        line_label = always_redraw( # R label
            lambda: 
                MathTex(r"\mathbb{R}").move_to(real_line.number_to_point(-1.8) + UP * 0.5)    
        )
        x_tracker = ValueTracker(.1) # x tracker
        y_tracker = ValueTracker(.9) # y tracker
        x_label = always_redraw( # x label
            lambda: VGroup(
                MathTex("x", font_size=30).next_to(real_line.number_to_point(x_tracker.get_value()), UP, buff = SMALL_BUFF),
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point(x_tracker.get_value()), DOWN, buff=0)
            )
        )
        y_label = always_redraw( # y label
            lambda: VGroup(
                MathTex("y", font_size=30).next_to(real_line.number_to_point(y_tracker.get_value()), UP, buff = SMALL_BUFF),
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point(y_tracker.get_value()), DOWN, buff=0)
            ) 
        )

        r_label = always_redraw( # r label
            lambda: VGroup(
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point((x_tracker.get_value() + y_tracker.get_value()) / 2), DOWN, buff=0),
                MathTex(r"r", font_size=30),
            ).arrange(DOWN, buff=SMALL_BUFF).next_to(real_line.number_to_point((x_tracker.get_value() + y_tracker.get_value()) / 2), DOWN, buff=0)
        )

        r_prime_label = always_redraw( # r' label
            lambda: VGroup(
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point((x_tracker.get_value() + y_tracker.get_value()) / 2), DOWN, buff=0),
                MathTex(r"r^{\prime}", font_size=30),
            ).arrange(DOWN, buff=SMALL_BUFF).next_to(real_line.number_to_point(0.7), DOWN, buff=0)
        )

        r_2prime_label = always_redraw( # r" label
            lambda: VGroup(
                Triangle(
                    stroke_width=0, fill_color=WHITE, fill_opacity=1
                ).scale(.1).next_to(real_line.number_to_point((x_tracker.get_value() + y_tracker.get_value()) / 2), DOWN, buff=0),
                MathTex(r"r^{\prime\prime}", font_size=30),
            ).arrange(DOWN, buff=SMALL_BUFF).next_to(real_line.number_to_point(0.3), DOWN, buff=0)
        )

        self.add(real_line, line_label, x_label, y_label)
        self.wait()
        self.play(
            GrowFromCenter(r_label[0]),
            Write(r_label[1])
        )
        self.wait()
        self.play(
            Indicate(y_label),
            Indicate(r_label),
        )
        self.play(
            GrowFromCenter(r_prime_label[0]),
            Write(r_prime_label[1])
        )
        self.wait()
        self.play(
            Indicate(x_label),
            Indicate(r_label),
        )
        self.play(
            GrowFromCenter(r_2prime_label[0]),
            Write(r_2prime_label[1])
        )
        self.wait()
        self.play(
            *[
                FadeOut(mob) for mob in self.mobjects
            ]
        )
        self.wait()