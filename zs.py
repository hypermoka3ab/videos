from manim import *

config.pixel_height = 600
config.pixel_width = 600
config.frame_height = 2
config.frame_width = 2
config.background_color = "#000"

class ZS(Scene):
    def construct(self):
        zs = MathTex(r"0^\sharp", font_size=100)
        self.add(zs)
