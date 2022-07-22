from manim import *

class State:
    def __init__(self, label='s_0', scale=1, initial=False, final=False, position=ORIGIN):
		
		# Initialiser le cercle 
        self.cercle = VGroup(
            Circle(radius = 0.5 * scale, stroke_width=1, color=WHITE),
            TexMobject(label)
        )

		# Double cercle pour un état final
        if final:
            self.cercle.add(
                Circle(radius = 0.4 * scale, stroke_width=1, color=WHITE),
            )

		# Une flèche pour un état initial
        if initial:
            fleche = TexMobject(r'\Rightarrow').rotate(-PI / 4).next_to(self.cercle, UL, buff=-0.15)
            self.cercle.add(fleche)

        # Mettre le cercle en position
        self.cercle.move_to(position)

class Union(Scene):
    def construct(self):
        #self.add_sound('Union')
        self.show_titre()
        self.demo()

    def show_titre(self):
        titre = TextMobject(r"Montrons que si $L_1$ et $L_2$ sont deux langages réguliers,\\ alors $L_1 \cup L_2$ l'est aussi").to_edge(UP)
        self.play(
            Write(titre),
            ShowCreation(Line(LEFT*6, RIGHT*6).next_to(titre, DOWN, SMALL_BUFF)),
            run_time=3
        )
        self.wait(3)

    def demo(self):
        s01 = State(r's_{01}', initial=True, position=LEFT*2.5)
        sf1 = State(r's_{f1}', final=True, position=RIGHT*2.5)
        box1 = Square()
        fleches1 = [
            Arrow(s01.cercle.get_right(), box1.get_left(), buff=0),
            Arrow(box1.get_right(), sf1.cercle.get_left(), buff=0)
        ]
        A1 = VGroup(
            s01.cercle,
            sf1.cercle,
            box1,
            *fleches1
        ).shift(UP*.5)
        b1 = VGroup(
            Brace(A1, LEFT),
            TexMobject(r'\mathcal{A}_1')
        )
        b1.submobjects[1].next_to(b1.submobjects[0], LEFT, SMALL_BUFF)
        
        s02 = State(r's_{02}', initial=True, position=LEFT*2.5)
        sf2 = State(r's_{f2}', final=True, position=RIGHT*2.5)
        box2 = Square()
        fleches2 = [
            Arrow(s02.cercle.get_right(), box2.get_left(), buff=0),
            Arrow(box2.get_right(), sf2.cercle.get_left(), buff=0)
        ]
        A2 = VGroup(
            s02.cercle,
            sf2.cercle,
            box2,
            *fleches2
        ).shift(DOWN*2)
        b2 = VGroup(
            Brace(A2, LEFT),
            TexMobject(r'\mathcal{A}_2')
        )
        b2.submobjects[1].next_to(b2.submobjects[0], LEFT, SMALL_BUFF)
        self.play(ShowCreation(A1), ShowCreation(A2), run_time=5)
        self.wait()
        self.play(Write(b1), Write(b2))
        self.wait(10)
        self.play(*[FadeOut(o) for o in [b1, b2, s01.cercle.submobjects[-1], s02.cercle.submobjects[-1]]])
        s0 = State(initial=True, position=LEFT*5 + DOWN*.75)
        fleches = [
            VGroup(
                Arrow(s0.cercle.get_right(), s01.cercle.get_left(), buff=-.4),
                TexMobject(r'\varepsilon')
            ),
            VGroup(
                Arrow(s0.cercle.get_right(), s02.cercle.get_left(), buff=-.4),
                TexMobject(r'\varepsilon')
            )
        ]
        fleches[0].submobjects[1].move_to(fleches[0].submobjects[0].get_center()+np.array([0, -0.2, 0]))
        fleches[1].submobjects[1].move_to(fleches[1].submobjects[0].get_center()+np.array([0, 0.2, 0]))

        A = VGroup(A1, A2, s0.cercle, *fleches)
        b = VGroup(
            Brace(A, LEFT),
            TexMobject(r'\mathcal{A}')
        )
        A_new = VGroup(s0.cercle, *fleches)
        b.submobjects[1].next_to(b.submobjects[0], LEFT, SMALL_BUFF)
        self.play(ShowCreation(A_new), run_time=2)
        self.wait()
        self.play(Write(b))
        self.wait(3)