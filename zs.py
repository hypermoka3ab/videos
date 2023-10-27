from manim import *
from themes.dracula import dracula

dracula.set()

config.pixel_height = 600
config.pixel_width = 600
config.frame_height = 2
config.frame_width = 2


class ZS(Scene):
    def construct(self):
        zs = MathTex(r"0^\sharp", font_size=150)
        self.add(zs)
