from manim import *

class TikzMobject(TextMobject):
    CONFIG = {
        'stroke_width': 3,
        'fill_opacity': 0,
        'stroke_opacity': 1,
    }

class Introduction(Scene):
    def construct(self):
        self.QuestCeQunLangage()
        self.DefinitionsFormelles()

    def QuestCeQunLangage(self):
        questCeQunLangage = TextMobject(
            "Q: Qu'est-ce qu'un language?\\\\",
            "R: Un langage est un ensemble de mots.\\\\",
            "Q: Qu'est-ce qu'un mot?\\\\",
            r"R: Un mot est une suite \emph{finie} de lettres (symboles, caractères, $\dots$ etc).\\",
            "Q: Qu'est-ce qu'une lettre?\\\\",
            "R: Une lettre est un élément d'un alphabet.\\\\",
            "Q: Qu'est-ce qu'un alphabet?\\\\",
            "R: Un ensemble fini qu'on choisi arbitrairement.",
            alignment="\\flushleft"
        ).scale(.8)
        for line in questCeQunLangage:
            self.play(Write(line))
            self.wait()

        self.play(
            Write(
                questCeQunLangage,
                rate_func=lambda t: 1 - t
            )
        )
        self.wait()

    def DefinitionsFormelles(self):
        titre = TextMobject("Définitions:\\\\")
        definition = TextMobject(
            r"Un alphabet est un ensemble fini (souvent noté $\Sigma$) dont les éléments sont appelés des lettres.\\",
            r"Un mot $w$ sur l'alphabet $\Sigma$ est une suite $w_1w_2\cdots w_n$ des lettres de $\Sigma$.\\",
            r"L'entier $n$ est appelé la longueur du mot $w$, on le note $|w|$.\\",
            r"L'unique mot de longueur $0$ est appelé le \emph{mot vide}, on le note $\varepsilon$.\\",
            r"L'ensemble de tous les mots sur $\Sigma$ est noté $\Sigma^*$.\\",
            r"Un langage sur l'alphabet $\Sigma$ est une partie de $\Sigma^*$.",
            alignment=r"\flushleft"
        ).scale(.8)
        titre.next_to(definition, UP)
        self.play(Write(titre))
        self.wait()
        for line in definition:
            self.play(Write(line))
            self.wait()

        self.play(
            Write(
                definition,
                rate_func=lambda t: 1 - t
            ),
            Write(
                titre,
                rate_func=lambda t: 1 - t
            )
        )
        self.wait()

class OperationsRationnelles(Scene):
    def construct(self):
        #self.ConcatMots()
        self.Operations()

    def ConcatMots(self):
        uEgal = TexMobject("u", "=", r"u_1u_2\cdots u_n").shift((LEFT + UP) * 2)
        vEgal = TexMobject("v", "=", r"v_1v_2\cdots v_p").shift((RIGHT + UP) * 2)
        uvEgal = TexMobject("u", r"\cdot", "v", "=", "u", "v", "=", r"u_1u_2\cdots u_n", r"v_1v_2\cdots v_p")
        SigmaEtoile = TextMobject(r"$(\Sigma^*, \cdot)$ est un monoïde!")
        self.play(Write(uEgal))
        self.wait(.5)
        self.play(Write(vEgal))
        self.wait()
        self.play(
            ReplacementTransform(uEgal[0].copy(), uvEgal[0]),
            ReplacementTransform(vEgal[0].copy(), uvEgal[2]),
            Write(uvEgal[1]),
            Write(uvEgal[3])
        )
        self.wait(.5)
        self.play(
            ReplacementTransform(uvEgal[0].copy(), uvEgal[4]),
            ReplacementTransform(uvEgal[1].copy(), uvEgal[5]),
            Write(uvEgal[6])
        )
        self.wait()
        self.play(ReplacementTransform(uEgal[2].copy(), uvEgal[7]))
        self.wait(.5)
        self.play(ReplacementTransform(vEgal[2].copy(), uvEgal[8]))
        self.wait()
        self.play(
            *[
                Write(
                    s,
                    rate_func = lambda t : smooth(1 - t)
                ) for s in [uEgal, vEgal, uvEgal]
            ]
        )
        self.play(Write(SigmaEtoile))
        self.wait()
        self.play(
            Write(
                SigmaEtoile,
                rate_func = lambda t: smooth(1 - t)
            )
        )
        self.wait()

    def Operations(self):
        titre = TextMobject("Operations rationnelles:").to_edge(UP)
        #SoientL1L2 = TextMobject("Soient ", "$L$", ",", "$L^\prime$", r" deux langages sur $\Sigma^*$.").to_edge(LEFT).shift(UP * 2)
        Definitions = TextMobject(
            "Soient ", "$L$", ", ", "$L^\prime$", r" deux langages sur $\Sigma^*$.\\",
            "La somme: ", "$L$", "$+$", "$L^\prime$", " $:=$ ", "$L$", r"$\cup$", "$L^\prime$.\\\\",
            "La concaténation: ", "$L$", r"$\cdot$", "$L^\prime$", " $:=$ ", r"$\{uv| u \in L \wedge v \in L^\prime\}$.\\",
            "L'étoile: ", r"$L^0 := \{\varepsilon\}, \quad$", r"$L^{n+1} := LL^n, \quad$", r"$L^* := \bigcup\limits_{n \in \mathbb{N}} L^n$" , 
            alignment = r"\flushleft"
        ).to_edge(LEFT).shift(UP * 1.5)
        self.play(Write(titre))
        self.wait()
        self.play(Write(Definitions[0:5]))
        self.wait()

        # Somme
        self.play(Write(Definitions[5]))
        self.wait(.5)
        self.play(
            ReplacementTransform(Definitions[1].copy(), Definitions[6]),
            ReplacementTransform(Definitions[3].copy(), Definitions[8]),
            Write(Definitions[7])
        )
        self.wait(.5)
        self.play(Write(Definitions[9:13]))
        self.wait()
        
        # Concaténation
        self.play(Write(Definitions[13]))
        self.wait(.5)
        self.play(
            ReplacementTransform(Definitions[1].copy(), Definitions[14]),
            ReplacementTransform(Definitions[3].copy(), Definitions[16]),
            Write(Definitions[15])
        )
        self.wait(.5)
        self.play(Write(Definitions[17:19]))
        self.wait()
        
        # Étoile
        for i in range(19, 23):
            self.play(Write(Definitions[i]))
            self.wait()

        classDesLangagesRationnels = TextMobject(r"La classe \mathcal{R} des langages rationnels (sur un alphabet $\Sigma$) est la plus petite famille des langages (pour l'inclusion) qui vérifient les 3 conditions suivantes:")
        self.play(
            Write(Definitions, rate_func = lambda t: 1 - t),
            Write(titre, rate_func = lambda t: 1 - t)
        )
        self.wait()