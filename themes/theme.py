from manim import Mobject, VMobject, config
from colour import Color


class Theme:
    def __init__(
        self,
        foreground: Color | str,
        background: Color | str,
        highlight1: Color | str,
        highlight2: Color | str,
        highlight3: Color | str,
        highlight4: Color | str,
        highlight5: Color | str,
        highlight6: Color | str,
    ):
        self.foreground = Color(foreground)
        self.background = Color(background)
        self.highlight1 = Color(highlight1)
        self.highlight2 = Color(highlight2)
        self.highlight3 = Color(highlight3)
        self.highlight4 = Color(highlight4)
        self.highlight5 = Color(highlight5)
        self.highlight6 = Color(highlight6)

    def set(self):
        config.background_color = self.background
        Mobject.set_default(color=self.foreground)
        VMobject.set_default(
            stroke_color=self.foreground, fill_color=self.foreground, fill_opacity=0.3
        )
