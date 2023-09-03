from manim import *

BACKGROUND_COLOR = "#282a36"
FOREGROUND_COLOR = "#f8f8f2"
HIGHLIGHT_COLOR1 = "#bd93f9"
HIGHLIGHT_COLOR2 = "#ffb86c"
HIGHLIGHT_COLOR3 = "#50fa7b"
HIGHLIGHT_COLOR4 = "#ff5555"
HIGHLIGHT_COLOR5 = "#f1fa8c"
HIGHLIGHT_COLOR6 = "#bd93f4"


def set_theme():
    config.background_color = BACKGROUND_COLOR
    Mobject.set_default(color=FOREGROUND_COLOR)
    VMobject.set_default(
        stroke_color=FOREGROUND_COLOR, fill_color=FOREGROUND_COLOR, fill_opacity=0.3
    )
