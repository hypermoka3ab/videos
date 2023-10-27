import mpmath

from manim import *
from themes.dracula import dracula

# 4k resolution
config.pixel_height = 2160
config.pixel_width = 3840

dracula.set()
VMobject.set_default(fill_opacity=0)


def zeta(z):
    max_norm = config.frame_x_radius
    try:
        return complex(mpmath.zeta(z))
    except:
        return complex(max_norm, 0)


class Inversion(Scene):
    def construct(self):
        bg = ComplexPlane()
        fg = ComplexPlane(
            x_range=(-20, 20),
            y_range=(-60, 60),
            axis_config={"stroke_width": 0},
            faded_line_ratio=5,
            background_line_style={
                "stroke_color": dracula.highlight2,
                "stroke_width": 1,
            },
            # faded_line_style={"stroke_color": dracula.highlight1},
        )
        self.add(bg, fg)
        fg.prepare_for_nonlinear_transform()
        self.play(
            fg.animate.apply_complex_function(
                lambda s: 2 / s if s != 0 else complex(config.frame_x_radius, 0)
            ),
            run_time=0.5,
        )
        self.wait()
