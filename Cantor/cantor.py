from manimlib.imports import *

class Cantor(Scene):
    def construct(self):
        #self.add_sound("test")
        self.introduction()
        self.positionDuProblème()


    def introduction(self):
        Cantor = ImageMobject("cantor").scale(2)
        Russel = ImageMobject("Russel").scale(2).to_edge(LEFT)
        Godel = ImageMobject("Godel").scale(2)
        Turing = ImageMobject("Turing").scale(2).to_edge(RIGHT)

        self.play(FadeIn(Cantor))
        self.wait()
        self.play(FadeOut(Cantor))
        for o in Russel, Godel, Turing:
            self.play(FadeIn(o))
            self.wait()
        

    def positionDuProblème(self):
        pass

    def réponse(self):
        pass

    